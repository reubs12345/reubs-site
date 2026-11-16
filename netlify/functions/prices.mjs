// Live prices for the home-page ticker, from the public Tenero API (no key needed).
const API = "https://api.tenero.io/v1/stacks/tokens/";
const TOKENS = [
  ["BTC", "SM3VDXK3WZZSA84XXFKAFAF15NNZX32CTSG82JFQ4.sbtc-token"],
  ["STX", "stx"],
  ["LEO", "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token"],
];

async function token([sym, id]) {
  try {
    const r = await fetch(API + id, { headers: { accept: "application/json" } });
    if (!r.ok) throw new Error(r.status);
    const d = (await r.json()).data || {};
    const p = d.price || {};
    let change = p.price_change_1d_pct;
    if (change == null && p.price_1d_ago > 0 && p.current_price > 0) change = (p.current_price / p.price_1d_ago - 1) * 100;
    return { sym, price: d.price_usd ?? p.current_price ?? null, change: change ?? null, holders: d.holder_count ?? null };
  } catch {
    return { sym, price: null, change: null, holders: null };
  }
}

export default async () => {
  const tokens = await Promise.all(TOKENS.map(token));
  return new Response(JSON.stringify({ updated: new Date().toISOString(), tokens }), {
    headers: {
      "content-type": "application/json",
      "cache-control": "public, max-age=60",
      "netlify-cdn-cache-control": "public, durable, s-maxage=300, stale-while-revalidate=3600",
    },
  });
};

export const config = { path: "/api/prices" };
