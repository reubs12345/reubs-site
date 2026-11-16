// Live BTC + STX prices for the home-page ticker, from CoinGecko's free API (no key needed).
// (Tenero's public token endpoint was returning stale prices, so it isn't used here.)
const URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,blockstack&vs_currencies=usd&include_24hr_change=true";
const MAP = [["BTC", "bitcoin"], ["STX", "blockstack"]];

export default async () => {
  let tokens = [];
  try {
    const r = await fetch(URL, { headers: { accept: "application/json" } });
    if (!r.ok) throw new Error(r.status);
    const d = await r.json();
    tokens = MAP.map(([sym, id]) => ({
      sym,
      price: d[id]?.usd ?? null,
      change: d[id]?.usd_24h_change ?? null,
    }));
  } catch {
    return new Response(JSON.stringify({ error: "unavailable" }), { status: 502, headers: { "content-type": "application/json", "cache-control": "no-store" } });
  }
  return new Response(JSON.stringify({ updated: new Date().toISOString(), source: "CoinGecko", tokens }), {
    headers: {
      "content-type": "application/json",
      "cache-control": "public, max-age=60",
      "netlify-cdn-cache-control": "public, durable, s-maxage=300, stale-while-revalidate=3600",
    },
  });
};

export const config = { path: "/api/prices" };
