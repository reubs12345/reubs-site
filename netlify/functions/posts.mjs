// Live posts from Typefully for reubs.link
// Needs TYPEFULLY_API_KEY set in Netlify → Site configuration → Environment variables.
// Returns the latest published X posts for each account below, cached at Netlify's CDN.

const API = "https://api.typefully.com/v2";
const ACCOUNTS = ["reubs_btc", "tenero_io", "LeoCoinSTX", "StackedUpStream"]; // usernames as connected in Typefully
const PER_ACCOUNT = 12;

const headers = () => ({
  Authorization: `Bearer ${process.env.TYPEFULLY_API_KEY}`,
  Accept: "application/json",
});

async function getJSON(url) {
  const r = await fetch(url, { headers: headers() });
  if (!r.ok) throw new Error(`${r.status} ${url}`);
  return r.json();
}

async function socialSets() {
  const out = {};
  let url = `${API}/social-sets?limit=50`;
  while (url) {
    const j = await getJSON(url);
    for (const s of j.results || []) {
      const xUser = s.platforms?.x?.username || s.username;
      out[(xUser || "").toLowerCase()] = s.id;
      out[(s.username || "").toLowerCase()] = s.id;
    }
    url = j.next;
  }
  return out;
}

async function postsFor(id, username) {
  const list = await getJSON(
    `${API}/social-sets/${id}/drafts?status=published&order_by=-published_at&limit=${PER_ACCOUNT}`
  );
  const items = (list.results || []).filter((d) => d.x_published_url);
  const full = await Promise.all(
    items.map(async (d) => {
      try {
        const f = await getJSON(`${API}/social-sets/${id}/drafts/${d.id}?exclude_comment_markers=true`);
        const posts = f.platforms?.x?.posts || [];
        return {
          url: d.x_published_url,
          date: d.published_at,
          title: d.draft_title || null,
          text: posts[0]?.text || d.preview || "",
          thread: posts.slice(1).map((p) => p.text).join("\n\n"),
          account: username,
        };
      } catch {
        return { url: d.x_published_url, date: d.published_at, title: d.draft_title || null,
                 text: d.preview || "", thread: "", account: username };
      }
    })
  );
  return full;
}

export default async () => {
  if (!process.env.TYPEFULLY_API_KEY) {
    return Response.json({ error: "TYPEFULLY_API_KEY not set" }, { status: 500 });
  }
  try {
    const sets = await socialSets();
    const accounts = {};
    await Promise.all(
      ACCOUNTS.map(async (u) => {
        const id = sets[u.toLowerCase()];
        accounts[u] = id ? await postsFor(id, u) : [];
      })
    );
    return Response.json(
      { updated: new Date().toISOString(), accounts },
      {
        headers: {
          "Cache-Control": "public, max-age=300",
          "Netlify-CDN-Cache-Control": "public, durable, s-maxage=900, stale-while-revalidate=86400",
        },
      }
    );
  } catch (e) {
    return Response.json({ error: String(e) }, { status: 502 });
  }
};

export const config = { path: "/api/posts" };
