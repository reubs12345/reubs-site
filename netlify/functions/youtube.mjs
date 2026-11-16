// Latest Stacked Up videos from the public YouTube feed (no API key needed).
const CHANNEL_ID = "UC40LDToSibgzdKlKdGSzMig"; // youtube.com/@reubsbtc

export default async () => {
  try {
    const r = await fetch(`https://www.youtube.com/feeds/videos.xml?channel_id=${CHANNEL_ID}`);
    if (!r.ok) throw new Error(`YouTube ${r.status}`);
    const xml = await r.text();
    const videos = [...xml.matchAll(/<entry>([\s\S]*?)<\/entry>/g)].map(([, e]) => ({
      id: (e.match(/<yt:videoId>(.*?)<\/yt:videoId>/) || [])[1],
      title: ((e.match(/<title>([\s\S]*?)<\/title>/) || [])[1] || "")
        .replace(/&amp;/g, "&").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">"),
      published: (e.match(/<published>(.*?)<\/published>/) || [])[1],
      short: /\/shorts\//.test((e.match(/<link rel="alternate" href="(.*?)"/) || [])[1] || ""),
    })).filter((v) => v.id);
    return Response.json(
      { updated: new Date().toISOString(), videos },
      {
        headers: {
          "Cache-Control": "public, max-age=300",
          "Netlify-CDN-Cache-Control": "public, durable, s-maxage=1800, stale-while-revalidate=86400",
        },
      }
    );
  } catch (e) {
    return Response.json({ error: String(e), videos: [] }, { status: 502 });
  }
};

export const config = { path: "/api/youtube" };
