"""Generate Stacks / Tenero / Stacked Up subpages for reubs.link.
Usage: python3 build_pages.py <site_dir>
Content lives in the DATA dict below — edit it weekly.
"""
import html, re, sys, pathlib

SITE = pathlib.Path(sys.argv[1])
home = (SITE / "index.html").read_text()
SPRITE = re.search(r'<svg width="0" height="0".*?</svg>', home, re.S).group(0)

def esc(t):
    return html.escape(t)

def hl(t):
    return re.sub(r'(@[A-Za-z0-9_]+|\$[A-Za-z][A-Za-z0-9_]*)', r'<span class="hl">\1</span>', esc(t))

# ---------------------------------------------------------------- content
DATA = {
 "stacks": {
  "title": "Stacks", "logo": "stacks.png", "role": "Ecosystem Growth & Marketing",
  "tagline": "Building Bitcoin Capital Markets.",
  "live": ("reubs_btc", "stacks"),
  "intro": "Stacks is the Bitcoin L2 bringing capital markets to Bitcoin — BTC staking with yield paid in bitcoin, DeFi and a clear roadmap toward privacy and post-quantum security.",
  "links": [("x", "@Stacks", "https://x.com/Stacks"), ("web", "stacks.co", "https://www.stacks.co/")],
  "stats_big": ("3,125+", "BTC deployed"),
  "stats": [("4,200+", "BTC distributed"), ("1.6M", "Activated users"), ("493M", "STX locked"), ("3", "Staking bonds sold out")],
  "asof": "Source: stacks.co · Nov 2026",
  "feature": ("stacks-site.jpg", "https://www.stacks.co/", "stacks.co"),
  # Hand-picked @Stacks posts — update weekly: (date, url, short summary)
  "official": [
   ("Nov 5", "https://x.com/Stacks/status/2118374509757845952", "Bitcoin staking Bond 3 fills with 1,005 BTC, with Bullish and 21Shares taking part."),
   ("Nov 3", "https://x.com/Stacks/status/2117647454002954485", "BitGo clients can now access Bitcoin staking on Stacks without moving their BTC."),
   ("Oct 16", "https://x.com/Stacks/status/2110841794959470594", "Stacks Q3 recap: 735 BTC across Bonds 1 & 2, staked STX up 25%+ and DEX volume at a 12-month high."),
  ],
  "bridges": [
   ("sBTC Bridge", "Bring your BTC to Stacks as sBTC — 1:1 Bitcoin you can use in DeFi.", "https://sbtc.stacks.co/", "sbtc.stacks.co"),
   ("USDC Bridge", "Move USDC from Ethereum to Stacks as USDCx.", "https://bridge.stacks.co/usdc/eth/stx", "bridge.stacks.co"),
  ],
  "podcasts": [
   ("New Era Finance Podcast", "@new_era_finance", "Nov 12", "https://x.com/new_era_finance/status/2120939689515610454",
    "Muneeb Ali: \"I think the bottom is in\"",
    ["Why negative news stopped moving the price", "The quantum question and self-custody", "Bitcoin as an income-generating asset"], "pod-new-era.jpg"),
   ("The White Papers · The Block", "@TheBlockCo", "Nov 10", "https://x.com/TheBlockCo/status/2120212634914238747",
    "Muneeb on turning bitcoin into productive capital",
    ["How Stacks bonds pay bitcoin holders 3% in BTC", "Stacks vs. Lightning", "The quantum threat and Satoshi's coins"], "pod-the-block.jpg"),
   ("The Wolf Of All Streets", "@scottmelker", "Nov 9", "https://x.com/scottmelker/status/2119859166600990761",
    "Bitcoin's Biggest \"Bond\" Yet Just Sold Out — What Do Institutions Know?",
    ["Why Muneeb is returning to lead Stacks", "Bullish joins the 1,000 BTC Stacks bond", "How Bitcoin yield could drive value to STX"], "pod-wolf.jpg"),
  ],
  "pillars_title": "The roadmap",
  "pillars": [("01", "Bitcoin Capital Markets", "Live now — BTC staking, bonds and DeFi."),
              ("02", "Privacy", "Bitcoin privacy, targeted for 2027."),
              ("03", "Post Quantum", "Quantum-secure Bitcoin, targeted for 2027.")],
  "news": [
   ("reubs", "Nov 11", "https://x.com/reubs_btc/status/2120555045070704644",
    "This sounds... erm... like a big deal\n\nFirst ever post-quantum Bitcoin transfer on @Stacks has just occurred"),
   ("reubs", "Nov 10", "https://x.com/reubs_btc/status/2120141138879496317",
    "The Stacks roadmap: Bitcoin Capital Markets → Privacy → Post Quantum\n\nBTC staking is live today with ~1,740 BTC bonded by institutions like @Bullish, @21shares, @HashKeyCloud & @nakamoto"),
   ("reubs", "Nov 9", "https://x.com/reubs_btc/status/2119835843926049212",
    "Institutions have locked ~1,740 BTC into @Stacks bonds, and every one of those bonds needs $STX\n\nCapacity is set to grow by roughly 1,000 BTC per month"),
   ("reubs", "Nov 5", "https://x.com/reubs_btc/status/2118374851207684584",
    "Stacks Bitcoin staking bond 3 is filled: 1,005 BTC!\n\n@Bullish participating, @21shares in all 3 bonding periods, and @BitGo integration now live"),
   ("reubs", "Nov 3", "https://x.com/reubs_btc/status/2117650519959462315",
    "Another BIG building block falls into place for @Stacks\n\n@BitGo clients can now access Bitcoin staking without moving their BTC to a new provider"),
   ("reubs", "Oct 16", "https://x.com/reubs_btc/status/2111028498647417269",
    "Stacks had a BIG Q3 - here are the headlines\n\n→ 735 BTC across Bonds 1 & 2\n→ Staked $STX up 25%+\n→ @ZestProtocol hits ATH TVL"),
  ],
 },
 "tenero": {
  "title": "Tenero", "logo": "tenero.png", "role": "Co-founder",
  "tagline": "Trade. Earn. Explore.",
  "live": ("tenero_io", ""),
  "intro": "Tenero is the analytics and trading hub for Stacks and Bitcoin DeFi — every Stacks token live, in-app swaps, a DeFi yield hub and portfolio tracking.",
  "links": [("web", "tenero.io", "https://tenero.io/"), ("x", "@tenero_io", "https://x.com/tenero_io")],
  "stats_big": ("V2", "Launched Oct 2026"),
  "stats": [("$42.45M", "Stacks DEX volume · Oct"), ("5,310", "Active traders · Oct"), ("184K+", "Trades · Oct"), ("76", "V2 bounty submissions")],
  "pillars_title": "What's inside",
  "pillars": [("01", "Live market data", "Every Stacks token, live — charts, holders and volume."),
              ("02", "In-app swaps", "Powered by Zest Protocol CLMM liquidity."),
              ("03", "Earn & portfolio", "DeFi yield hub, Google/Privy STX wallet and portfolio view.")],
  "news": [
   ("tenero", "Nov 11", "https://x.com/tenero_io/status/2120444463273382358",
    "Tenero is now featured on the @xverse explore page!\n\nAccess Tenero's analytics without leaving your wallet. Every @Stacks token, live, at tenero.io"),
   ("tenero", "Nov 10", "https://x.com/tenero_io/status/2120163003064848407",
    "Tenero's in-app swaps are proudly powered by @ZestProtocol\n\nTenero now taps into Zest CLMM liquidity, giving users tighter spreads and more efficient trades"),
   ("tenero", "Nov 9", "https://x.com/tenero_io/status/2119718951974502770",
    "Stacks: 7 day snapshot\n\n→ DEX Volume: $4.13M\n→ Active Traders: 1,539 (+1% WoW)\n→ Trades: 47,770"),
   ("tenero", "Oct 26", "https://x.com/tenero_io/status/2114642890861531258",
    "Stacks ecosystem - October Overview\n\n→ DEX Volume: $42.45M\n→ Active Traders: 5,310 (+225% MoM)\n→ Trades: 184,660 (+10% MoM)"),
   ("tenero", "Oct 22", "https://x.com/tenero_io/status/2113245363905929349",
    "Congratulations to the winners of our Tenero V2 Launch bounty on @zeroauthdao!\n\n76 submissions, 93k+ views and 5.6k+ engagements"),
   ("reubs", "Oct 7", "https://x.com/reubs_btc/status/2107843259146105146",
    "Tenero V2 is LIVE\n\n→ In-app swaps powered by @ZestProtocol\n→ @Stacks DeFi yield hub\n→ Google/Privy $STX wallet\n→ Updated UI, Portfolio & more"),
  ],
 },
 "stacked-up": {
  "title": "Stacked Up", "logo": "stackedup.png", "role": "Host",
  "tagline": "Weekly livestream on Stacks, Bitcoin and the market.",
  "intro": "Live every Wednesday, 2pm UK / 9am EST — the week in Bitcoin and Stacks, market data from Tenero, DeFi strategies and community spotlights.",
  "links": [("yt", "YouTube", "https://www.youtube.com/@reubsbtc"), ("x", "@StackedUpStream", "https://x.com/StackedUpStream"), ("tt", "TikTok", "https://www.tiktok.com/@stackedupcrypto")],
  "stats_big": ("9", "Episodes so far"),
  "stats_big_live": "episodes",
  "stats": [("Weekly", "Every Wednesday"), ("2pm UK", "9am EST"), ("3", "Platforms: YouTube, X, TikTok"), ("Shorts", "On TikTok & YouTube")],
  # episodes: (num, date, watch_url, recap_url, bullets)
  "episodes": [
   ("9", "Nov 18", "https://youtu.be/bgWcma1NQHo", "https://x.com/reubs_btc/status/2123081247853605236",
    ["$BTC drops 12% to $65k", "$STX steady at $0.28, 5th on CMC over 90 days", "Xverse launches multisig", "Zest airdrop claims open Nov 19"]),
   ("8", "Nov 11", "https://youtu.be/CDSTaj74gbU", "https://x.com/reubs_btc/status/2120545704024383632",
    ["$BTC drops below $74k into the fear zone", "Stacks BTC staking bond 3 fills with 1,005 BTC", "Zest Protocol launches CLMM", "Tenero x Xverse integration"]),
   ("7", "Nov 4", "https://youtu.be/fyjzeKex4Cc", "https://x.com/reubs_btc/status/2118009105009070238",
    ["$STX #1 7 day gainer on CMC", "$BTC back to $80k", "BTC staking bond 3 opens", "BitGo institutional integration live"]),
   ("6", "Oct 29", "https://youtu.be/Z8vEWlaf8S8", "https://x.com/reubs_btc/status/2115814661295923297",
    ["$BTC ETF inflows +$420M over 3 days", "Stacks market data from Tenero", "StackingDao stBTC & 10%+ APY for STX stakers", "National Cat Day for $LEO"]),
   ("5", "Oct 21", None, "https://x.com/reubs_btc/status/2112917333497008284",
    ["$STX +7% to $0.37", "$BTC inflows hit a 1-month high at $550M", "Tenero V2 live swap", "Zest Protocol hits ATH TVL"]),
   ("4", "Oct 14", None, "https://x.com/reubs_btc/status/2110385139738161482",
    ["$STX hit #1 on CMC, pushed to $0.43", "BTC Staking Bond 2 fills adding ~500 BTC", "Muneeb's Stacks 2030 vision at Token2049", "Tenero V2 market data + live swap"]),
   ("3", "Oct 7", None, "https://x.com/reubs_btc/status/2107871192434847846",
    ["Tenero V2 walkthrough", "Muneeb back as Stacks CEO, $STX surges", "BTC Staking Bond 2 filled", "Zest looping vault adds +80 BTC"]),
  ],
 },
}

DATA["leo"] = {
  "title": "LEO", "logo": "leo.png", "role": "Cat Executive Officer",
  "tagline": "The cat on Stacks.",
  "intro": "$LEO, Muneeb's cat, living on the Stacks blockchain. Growing $STX one cat at a time.",
  "live": ("LeoCoinSTX", ""),
  "notice": "$LEO is a community memecoin with no utility and no intrinsic value. Nothing on this page is financial advice.",
  "links": [("x", "@LeoCoinSTX", "https://x.com/LeoCoinSTX"),
            ("dc", "Join the Discord", "https://discord.gg/dPFx9YDwr9"),
            ("tg", "Join on Telegram", "https://t.me/+8rJPgGVtGxA4NTE1"),
            ("x", "Join the X chat", "https://x.com/i/chat/group_join/g2077334179189321894/N858ckC90k"),
            ("web", "Trade on Tenero", "https://tenero.io/stacks/swap?from=STX&to=SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token"),
            ("web", "Trade on Zest", "https://app.zestprotocol.com/swap/stx-to-leo"),
            ("web", "Trade on Bitflow", "https://app.bitflow.finance/pools/dlmm/SM1FKXGNZJWSTWDWXQZJNF7B5TV5ZB235JTCXYXKD.dlmm-pool-leo-stx-v-1-bps-50"),
            ("web", "Buy Leo Cats on Gamma", "https://gamma.io/stacks/collections/leo-cats/items"),
            ("web", "Buy Leo Cats on FakFun", "https://fak.fun/m/nfts/leo")],
  "stats_big": ("20%+", "of supply given to the Stacks community since 2024"),
  "stats": [("10K", "Leo Cats, minted out"), ("4,200", "STX top Leo Cat sale"), ("125K", "STX Leo Cats volume"), ("2023", "Launched on Stacks, Dec")],
  "asof": "From @LeoCoinSTX posts",
  "contract": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
  "timeline": [
   ("Dec 2023", "Leo comes on-chain", "$LEO launches on Stacks, named for Muneeb Ali's real cat, first introduced to the world in a 2011 tweet about two kittens, Leo and Parker. It becomes one of the earliest community memecoins on the network.", "https://x.com/LeoCoinSTX/status/1741095662156955930"),
   ("Jan 2024", "Airdrop tour", "Rather than one big drop, $LEO seeds its holder base by airdropping straight into Stacks NFT communities: Megapont Ape Club first, then 0.5% of supply across active BNS holders, then a surprise drop for Honey Badgers, among several other community airdrops.", "https://x.com/MegapontNFT/status/1743682303090446378"),
   ("Jan 2024", "Onto the exchanges", "$LEO lists on CoinGecko within days of launch, and the last of the early community airdrops go out on January 20.", "https://x.com/LeoCoinSTX/status/1742276728947433685"),
   ("Feb 2024", "MEXC Kickstarter", "Leo becomes the first Dextools-listed project on Stacks and wins a MEXC Kickstarter vote. The same week, $LEO cracks CoinGecko's top 1000.", "https://x.com/LeoCoinSTX/status/1762084705267302507"),
   ("Mar 2024", "A week of firsts", "Featured twice on Stacks' own website, live value inside the Xverse wallet, and Muneeb joins the team on the Stacks DeFi show, all in one week.", "https://x.com/LeoCoinSTX/status/1764313678361629108"),
   ("Mar 10, 2024", "The biggest airdrop in Stacks history", "$LEO airdrops 5% of its supply, worth about $1.35m at the time, to STX holders, and burns another 5% alongside it.", "https://x.com/LeoCoinSTX/status/1766776687411552426"),
   ("Mar 13, 2024", "Listed on CoinMarketCap", "$LEO goes live on CoinMarketCap.", "https://x.com/LeoCoinSTX/status/1767837464801001512"),
   ("Apr 23, 2024", "Happy birthday, Leo", "Muneeb marks the day himself: \"Happy birthday to Leo, the cat,\" the same date he first introduced Leo and Parker back in 2011.", "https://x.com/muneeb/status/1782795324366438829"),
   ("Sep 2024", "Leo Cats mint out", "The 10,000-piece Leo Cats collection mints out on September 30, the first 10k PFP collection to sell out on Stacks. The \"LEO Origins\" mini-documentary follows weeks later.", "https://x.com/LeoCoinSTX/status/1840809152257372545"),
   ("Oct 31, 2024", "Halloween Leo", "A free Halloween Leo Bitcoin art mint on Gamma.", "https://x.com/LeoCoinSTX/status/1851934000148803949"),
   ("Dec 2024", "12 days of Christmas", "Daily games and $LEO prizes, plus the free LEO Ordinals Art Pass by @ReeceSwanepoel, making holders eligible for future artist drops.", "https://x.com/LeoCoinSTX/status/1866856778954141899"),
   ("Dec 2024", "Community first", "After the \"Goat\" token rug pull, the team reimburses 70m+ $LEO to affected holders from the team wallet. Leo holders land the 6th largest community allocation of the Pizza Pets airdrop, and the project turns one on December 29.", "https://x.com/LeoCoinSTX/status/1863618061779026254"),
   ("Feb 2025", "Native Xverse swaps", "Xverse adds direct STX to SIP-10 swaps in the wallet, with $LEO among the first Stacks memecoins featured.", ""),
   ("Feb 18, 2025", "First Bitcoin art drop", "Leo's first Bitcoin art drop goes out free on Gamma for Art Pass holders, with artwork from Stacks OG @GPSC_STX.", "https://x.com/LeoCoinSTX/status/1891850625379397694"),
   ("Jul 2025", "Meow Mondays", "Weekly bounties and holder giveaways kick off through Zero Authority DAO, with 1.25m $LEO up for grabs in the first week alone.", "https://x.com/LeoCoinSTX/status/1944654228477427798"),
   ("Aug 1, 2025", "Feline Fridays", "A second weekly bounty series launches, with at least 25m $LEO committed to reward Stacks content creators.", "https://x.com/LeoCoinSTX/status/1951259444073079206"),
   ("Aug 2025", "FPL league, year 3", "The $LEO Fantasy Premier League goes live for a third straight season, with 2.5m $LEO in prizes plus bonus Leo Cats rewards.", "https://x.com/LeoCoinSTX/status/1955175749792808961"),
   ("Dec 2025", "Two years on", "Leo marks two years on Stacks: \"what a wild ride this year has been.\"", "https://x.com/LeoCoinSTX/status/2005894416045650190"),
   ("Jun 2026", "Leo Cats NFT momentum", "Leo Cats get permanent on-chain inscriptions, top Gamma's 30-day volume leaderboard with 25k STX traded and land on Gamma's homepage.", "https://x.com/LeoCoinSTX/status/2071168323677769892"),
   ("Jul 2026", "Zest swap spotlight", "$LEO is featured in Zest Protocol's swap launch, celebrated with a Leo Cat NFT giveaway and an LP strategies bootcamp.", "https://x.com/LeoCoinSTX/status/2080257985474081263"),
   ("Jul 27, 2026", "HODLMM pool goes live", "The LEO/STX HODLMM pool on Bitflow opens to trading after a community-controlled launch, with 30m $LEO in trader rewards, capping a July where $LEO finished up 20%.", "https://x.com/LeoCoinSTX/status/2081788219692404872"),
   ("Jul 30, 2026", "Stacks 4.0", "Leo cheers on the Stacks 4.0 announcement with the rest of the ecosystem.", "https://x.com/LeoCoinSTX/status/2082757014032122280"),
   ("Aug 2026", "Feed the Cat", "feedthecat.app tracks $LEO buys and trader rewards. The campaign drives $20k in net buys and $200k+ in volume in its first 30 days.", "https://x.com/LeoCoinSTX/status/2092255382001668387"),
   ("Aug 23, 2026", "No foundation, no games", "The team confirms there's no \"Leo foundation\", less than 1% of supply sits in the team wallet, and over 20% has been given to the Stacks community since 2024.", "https://x.com/LeoCoinSTX/status/2091424274934345892"),
   ("Sep 2026", "New look, LEO₿", "A visual refresh and a new \"cat tags\" feature, both built with @boostx_app.", "https://x.com/LeoCoinSTX/status/2096893018230128947"),
   ("Sep 15, 2026", "Leo Cats by the numbers", "16th all-time in Stacks NFT volume, 2nd all-time in secondary sales and the most unique holders of any PFP collection on Stacks.", "https://x.com/LeoCoinSTX/status/2099842841489154339"),
   ("Oct 2026", "Swap on Tenero", "$LEO becomes swappable directly on Tenero, and 30m $LEO (~$3,000) in Feed the Cat rewards are distributed to traders.", "https://x.com/LeoCoinSTX/status/2112495669651124708"),
   ("Ongoing", "Growing Stacks, one cat at a time!", "Beyond the milestones, Leo keeps a steady drumbeat of community activity: sponsored events, ecosystem partnerships and recurring poker tournaments among them.", ""),
  ],
  "news": [
   ("leo", "Oct 29", "https://x.com/LeoCoinSTX/status/2115764194796810397", "Happy International Cat Day 🐱\n\nFrom your favourite cat on @Stacks - $LEO"),
   ("leo", "Oct 24", "https://x.com/LeoCoinSTX/status/2113934796992995819", "Happy Caturday! 🐱\n\nLEO trivia is live on STX.BUZZ, 5 questions a day for the next 7 days"),
   ("leo", "Oct 20", "https://x.com/LeoCoinSTX/status/2112495669651124708", "30M (~$3000) in $LEO rewards have been distributed to eligible wallets for the @bitflow 'Feed the Cat' campaign"),
   ("leo", "Oct 18", "https://x.com/LeoCoinSTX/status/2111939543935164519", "$LEO is @muneeb's pet cat\n$LEO launched at $5k market cap ~3 years ago\n$LEO started the airdrop meta…"),
   ("leo", "Oct 15", "https://x.com/LeoCoinSTX/status/2110654489615282265", "$LEO is @muneeb's pet cat living on the @Stacks blockchain\n\nBeing bullish on $STX = being bullish on $LEO…"),
   ("leo", "Oct 7", "https://x.com/LeoCoinSTX/status/2107848804808663418", "$LEO looks good on @tenero_io\n\nYou can now swap there too!"),
  ],
}

DATA["stx-legion"] = {
  "title": "STX Legion", "logo": "legion.jpg", "role": "Founder",
  "tagline": "The $STX Legion is open! 🟧",
  "intro": ["The best place to keep up with Stacks news (like the Bitcoin staking bonds), project updates and the wider market.",
            "Live X feeds, KOL channel, a dedicated Korean channel and much more.",
            "Builders, creators, founders and community members welcome! We also run weekly content bounties on Zero Authority DAO, rewarding creators for spreading the word about Stacks."],
  "links": [("tg", "Join on Telegram", "https://t.me/+wcOPrJbqGfxiMTY0"),
            ("x", "Join the X chat", "https://x.com/i/chat/group_join/g2094436853315182765/9m6NFbUJ3Q"),
            ("web", "Bounties on Zero Authority", "https://zeroauthoritydao.com/bounty-hub/72bc33ef-ada8-4d1a-bc68-551df2032f0d")],
  "stats_big": ("630K", "Impressions from bounty posts"),
  "stats": [("12", "Bounties hosted"), ("670", "Total entries"), ("37.9K", "Total engagements"), ("6,000", "STX reward pools")],
  # Current open bounty: (title, url, pool, posted, ends). Set to None when nothing is live.
  "live_bounty": ("Stacks Clipping Bounty for New Era, Wolf of All Streets and The Block", "https://zeroauthoritydao.com/bounty/9e2ca501-3465-4fb8-962a-3b4b1a6e74fe", 500, "Nov 13", "Nov 20"),
  "asof": "Zero Authority bounties · Aug–Nov 2026",
  # Bounties — update weekly from the Notion "STX Legion Bounty Tracker": (week, title, url, entries, impressions, engagement, pool)
  "bounties": [
   ("Nov 5", "Stacks Bitcoin Staking Bond 3 fills 1,005 BTC with Bullish and 21Shares participating", "https://zeroauthoritydao.com/bounty/07833f29-8601-4255-90bd-825e1f0d3748", 83, 129284, 7336, 500),
   ("Oct 16", "Stacks Q3 Ecosystem Report", "https://zeroauthoritydao.com/bounty/b7dee382-f4bc-4239-b95f-43cfb2e5057d", 59, 59076, 4458, 500),
   ("Oct 9", "The Frontier of Bitcoin and Stacks 2030 Vision", "https://zeroauthoritydao.com/bounty/ddf6413a-22ff-45d5-8a39-81e394dfbb9a", 73, 54597, 4363, 500),
   ("Oct 2", "Muneeb is the new Stacks CEO, Bitcoin's Next Frontier", "https://zeroauthoritydao.com/bounty/8699cc4e-35cf-4afe-aefd-c3fbcc82e167", 88, 61018, 4496, 500),
   ("Sep 25", "Anchorage Institutional BTC Staking on Stacks", "https://zeroauthoritydao.com/bounty/cdf5e946-0add-4cef-9b6e-109b73c57b57", 84, 49794, 3388, 500),
   ("Sep 18", "Stacks Sats DeFi Incentives Campaign with Zest and Bitflow", "https://zeroauthoritydao.com/bounty/2cad62ed-c51d-4a75-b17d-d5da5a396fe4", 34, 19978, 1415, 500),
   ("Sep 11", "Stacks Genesis Bond", "https://zeroauthoritydao.com/bounty/a43b34ec-828a-4ac5-a833-7e1981bab634", 50, 49227, 2217, 500),
   ("Sep 4", "$STX Institutional Adoption", "https://zeroauthoritydao.com/bounty/ebd1b063-e01d-4149-a963-625ae45f551a", 46, 46983, 2206, 500),
   ("Aug 28", "$STX is THE beta to $BTC", "https://zeroauthoritydao.com/bounty/2aebc6d7-d769-47bb-9370-cd6f4ff37278", 41, 80206, 2981, 500),
   ("Aug 21", "Stacks (STX) is Building Bitcoin Native Finance", "https://zeroauthoritydao.com/bounty/c650793d-beeb-40f4-a020-ed99c99e5d2f", 71, 46595, 3278, 500),
   ("Aug 14", "STX: Powering Productive Bitcoin Capital", "https://zeroauthoritydao.com/bounty/a4243163-91ea-47a9-81b7-0e81edd490ed", 41, 33100, 1746, 500),
  ],
}

COVER_PHOTO = {"stacks": "../assets/cover-stacks.jpg", "tenero": "../assets/cover-tenero.jpg", "stacked-up": "../assets/cover-stacked-up.jpg", "leo": "../assets/cover-leo.jpg"}  # others get a generated brand cover
COVER_WORD = {"stx-legion": "Legion", "stacked-up": "Stacked Up", "leo": "$LEO"}

def cover_html(key, title, img):
    if key in COVER_PHOTO:
        return f'<div class="cover photo" style="background-image:url(\'{COVER_PHOTO[key]}\')"></div>'
    word = esc(COVER_WORD.get(key, title))
    return (f'<div class="cover gen" aria-hidden="true"><span class="cover-word">{word}</span>'
            f'<img class="cover-art blur" src="{img}" alt=""><img class="cover-art" src="{img}" alt=""></div>')

ORDER = [("stacks", "Stacks"), ("tenero", "Tenero"), ("stacked-up", "Stacked Up"), ("stx-legion", "STX Legion"), ("leo", "LEO")]
NAV = ORDER + [("contact", "Contact")]
AUTHORS = {"reubs": ("reubs", "@reubs_btc", "../assets/me.png", True),
           "tenero": ("Tenero", "@tenero_io", "../assets/tenero.png", False),
           "leo": ("LEO", "@LeoCoinSTX", "../assets/leo.png", False)}
ICON = {"x": "i-x", "web": "i-web", "yt": "i-yt", "tt": "i-tt", "ig": "i-ig", "tg": "i-tg", "dc": "i-dc", "cmc": "i-verified"}

PAGE_CSS = """
  .back{display:inline-flex;align-items:center;gap:6px;font-size:14px;font-weight:600;color:var(--muted);margin-bottom:28px}
  .back:hover{color:var(--orange)}
  .page-logo{width:84px;height:84px;border-radius:22px;box-shadow:0 14px 34px -14px rgba(12,12,13,.45);margin-bottom:22px;display:block}
  .page-hero h1{font-size:clamp(48px,8vw,84px)}
  .page-hero .role-pill{display:inline-block;font-size:13px;font-weight:600;color:var(--orange);background:var(--orange-soft);padding:6px 12px;border-radius:999px;margin-bottom:14px}
  .intro{font-size:17px;color:var(--muted);max-width:620px;margin-top:14px}
  .pillars{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  @media(max-width:860px){.pillars{grid-template-columns:1fr}}
  .pillar{background:#fff;border:1px solid rgba(252,100,50,.12);border-radius:var(--radius);padding:24px;box-shadow:0 1px 2px rgba(12,12,13,.04),0 10px 30px -14px rgba(12,12,13,.14)}
  .pillar .n{font-size:13px;font-weight:700;color:var(--orange);letter-spacing:.08em}
  .pillar h3{font-size:20px;font-weight:800;letter-spacing:-.02em;margin:8px 0 6px}
  .pillar p{color:var(--muted);font-size:15px}
  .eps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  @media(max-width:960px){.eps{grid-template-columns:repeat(2,1fr)}}
  @media(max-width:640px){.eps{grid-template-columns:1fr}}
  .ep{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:0 1px 2px rgba(12,12,13,.04),0 10px 30px -16px rgba(12,12,13,.14);transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}
  .ep:hover{transform:translateY(-3px);border-color:var(--orange);box-shadow:0 20px 40px -18px rgba(252,100,50,.4)}
  .ep-thumb{aspect-ratio:16/9;background:radial-gradient(circle at 30% 20%,rgba(252,100,50,.45),transparent 60%),#0C0C0D;background-size:cover;background-position:center;position:relative;display:flex;align-items:flex-end;padding:14px}
  .ep-thumb .tag{background:var(--orange);color:#fff;font-weight:800;font-size:13px;padding:4px 10px;border-radius:6px;letter-spacing:.02em}
  .ep-body{padding:18px 20px 20px;display:flex;flex-direction:column;flex:1}
  .ep-date{font-size:13px;color:var(--muted);margin-bottom:8px}
  .ep ul{list-style:none;font-size:14px;line-height:1.5;flex:1}
  .ep li{padding-left:16px;position:relative;margin-bottom:4px}
  .ep li::before{content:"→";position:absolute;left:0;color:var(--orange)}
  .ep-links{display:flex;gap:8px;margin-top:14px;flex-wrap:wrap}
  .band-dark .chip{background:rgba(255,255,255,.08);color:#fff}
  .notice{margin-top:18px;max-width:620px;font-size:14px;line-height:1.5;color:#7a3a1c;background:var(--orange-soft);border:1px solid rgba(252,100,50,.25);border-radius:12px;padding:12px 14px}
  .posts.official{grid-template-columns:repeat(3,1fr)}
  @media(max-width:860px){.posts.official{grid-template-columns:1fr}}
  .bounties{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
  @media(max-width:760px){.bounties{grid-template-columns:1fr}}
  .bounty{display:flex;flex-direction:column;gap:10px;background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:20px 22px;box-shadow:0 1px 2px rgba(12,12,13,.04),0 10px 30px -16px rgba(12,12,13,.14);transition:transform .2s ease,border-color .2s ease}
  .bounty:hover{transform:translateY(-3px);border-color:var(--orange)}
  .b-top{display:flex;justify-content:space-between;align-items:center;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
  .b-week{color:var(--orange)}
  .b-pool{background:var(--ink);color:#fff;border-radius:999px;padding:4px 10px;letter-spacing:0}
  .bounty h3{font-size:17px;font-weight:700;line-height:1.35;flex:1}
  .b-stats{display:flex;gap:14px;flex-wrap:wrap;font-size:13px;color:var(--muted)}
  .b-stats b{color:var(--ink)}
  .tl{position:relative;padding-left:28px}
  .tl::before{content:"";position:absolute;left:7px;top:6px;bottom:6px;width:2px;background:linear-gradient(180deg,var(--orange),rgba(252,100,50,.15))}
  .tl-item{position:relative;display:block;padding:0 0 26px}
  .tl-item::before{content:"";position:absolute;left:-27px;top:4px;width:14px;height:14px;border-radius:50%;background:#fff;border:3px solid var(--orange)}
  .tl-item .when{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--orange)}
  .tl-item h3{font-size:20px;font-weight:800;letter-spacing:-.02em;margin:4px 0}
  .tl-item p{color:var(--muted);font-size:15px;max-width:640px}
  .tl-item:hover h3{color:var(--orange)}
  .ca{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-top:22px;font-size:13px;color:var(--muted)}
  .ca code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 12px;color:var(--ink);word-break:break-all}
  .ca-link{font-weight:600;color:var(--orange)}
  .ca button{font:inherit;font-weight:600;border:0;background:var(--ink);color:#fff;border-radius:999px;padding:8px 14px;cursor:pointer}
  .feature{display:block;border-radius:22px;overflow:hidden;border:1px solid var(--line);box-shadow:0 30px 70px -30px rgba(252,100,50,.5);transition:transform .25s ease,box-shadow .25s ease;position:relative}
  .feature:hover{transform:translateY(-4px);box-shadow:0 40px 80px -30px rgba(252,100,50,.6)}
  .feature img{display:block;width:100%;height:auto}
  .feature .bar{display:flex;align-items:center;gap:8px;padding:12px 16px;background:#F6F6F7;border-bottom:1px solid var(--line);font-size:13px;color:var(--muted)}
  .feature .bar i{width:10px;height:10px;border-radius:50%;background:#E2E2E5;display:inline-block}
  .feature .bar span{margin-left:10px;background:#fff;border:1px solid var(--line);border-radius:999px;padding:3px 14px}
  .feature .bar b{margin-left:auto;color:var(--orange);font-weight:600}
  .bridges{display:grid;grid-template-columns:1fr 1fr;gap:16px}
  @media(max-width:760px){.bridges{grid-template-columns:1fr}}
  .bridge{display:flex;flex-direction:column;gap:10px;padding:26px;border-radius:var(--radius);background:linear-gradient(135deg,#0C0C0D,#2a1a14);color:#fff;transition:transform .2s ease,box-shadow .2s ease}
  .bridge:hover{transform:translateY(-3px);box-shadow:0 20px 40px -18px rgba(252,100,50,.55)}
  .bridge .k{font-size:12px;font-weight:700;letter-spacing:.08em;color:var(--orange);text-transform:uppercase}
  .bridge h3{font-size:24px;font-weight:800;letter-spacing:-.02em}
  .bridge p{color:rgba(255,255,255,.7);font-size:15px;flex:1}
  .bridge .go{display:inline-flex;align-self:flex-start;align-items:center;gap:8px;margin-top:8px;background:var(--orange);color:#fff;font-weight:600;font-size:14px;padding:10px 16px;border-radius:999px}
  .pods{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  @media(max-width:860px){.pods{grid-template-columns:1fr}}
  .pod{display:flex;flex-direction:column;gap:10px;background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:22px;box-shadow:0 1px 2px rgba(12,12,13,.04),0 10px 30px -16px rgba(12,12,13,.14);transition:transform .2s ease,border-color .2s ease}
  .pod:hover{transform:translateY(-3px);border-color:var(--orange)}
  .pod-thumb{position:relative;margin:-10px -10px 4px;border-radius:14px;overflow:hidden;aspect-ratio:16/9;background:#0C0C0D}
  .pod-thumb img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s ease}
  .pod:hover .pod-thumb img{transform:scale(1.04)}
  .pod-play{position:absolute;right:12px;bottom:12px;width:44px;height:44px;border-radius:50%;background:var(--orange);color:#fff;display:grid;place-items:center;box-shadow:0 8px 20px -6px rgba(0,0,0,.6)}
  .pod-play svg{width:20px;height:20px;margin-left:2px}
  .pod .mic{width:44px;height:44px;border-radius:12px;background:var(--orange-soft);color:var(--orange);display:grid;place-items:center}
  .pod .mic svg{width:22px;height:22px}
  .pod .who{font-size:13px;color:var(--muted)}
  .pod h3{font-size:17px;font-weight:700;line-height:1.35}
  .pod-list{list-style:none;font-size:14px;color:var(--muted);line-height:1.5;flex:1}
  .pod-list li{padding-left:16px;position:relative;margin-bottom:4px}
  .pod-list li::before{content:"→";position:absolute;left:0;color:var(--orange)}
"""

MENU = [("", "Home", "me.png"), ("stacks/", "Stacks", "stacks.png"), ("tenero/", "Tenero", "tenero.png"),
        ("stacked-up/", "Stacked Up", "stackedup.png"), ("stx-legion/", "Legion", "legion.jpg"), ("leo/", "LEO", "leo.png"), ("contact/", "Contact", "me.png")]

def mobile_nav(base, active):
    """Hamburger button + dropdown + fixed bottom tab bar. base='' for home, '../' for subpages."""
    btn = '<button class="menu-btn" type="button" aria-label="Menu" onclick="document.body.classList.toggle(\'menu-open\')"><span></span><span></span><span></span></button>'
    menu = "".join(f'<a href="{(base + h) or './'}"{" class=\"on\"" if h == active else ""}><img src="{base}assets/{img}" alt="">{t}<span class="arr">→</span></a>' for h, t, img in MENU)
    tabs = "".join(f'<a href="{(base + h) or './'}"{" class=\"on\"" if h == active else ""}><img src="{base}assets/{img}" alt="">{t}</a>' for h, t, img in MENU[:6])
    return btn, f'<div class="mobile-menu">{menu}</div>', f'<div class="tabbar" role="navigation" aria-label="Sections">{tabs}</div>'

def nav(active):
    act = ' style="color:var(--ink)"'
    links = "".join(f'<a href="../{k}/"{act if k == active else ""}>{t}</a>' for k, t in NAV)
    btn, menu, tabs = mobile_nav("../", active + "/")
    return f"""<nav>
  <div class="wrap">
    <a href="../" class="logo"><img src="../assets/me.png" alt="">reubs</a>
    <div class="nav-links">{links}</div>
    {btn}
  </div>
  {menu}
</nav>
{tabs}"""

def news_cards(items):
    out = []
    for who, date, url, text in items:
        name, handle, img, verified = AUTHORS[who]
        out.append(f"""      <a class="post" href="{url}" target="_blank" rel="noopener">
        <div class="post-head"><img src="{img}" alt=""><div><b>{esc(name)}</b><span>{handle} · {date}</span></div><svg><use href="#i-x"/></svg></div>
        <p>{hl(text)}</p>
        <span class="post-more">Read on X →</span>
      </a>""")
    return "\n".join(out)

def stats_html(d):
    big = d["stats_big"]
    live_attr = f' data-live-stat="{d["stats_big_live"]}"' if d.get("stats_big_live") else ""
    small = "".join(f'<div class="stat"><div class="num">{esc(n)}</div><div class="lbl">{esc(l)}</div></div>' for n, l in d["stats"])
    return f"""<aside class="stats" aria-label="Highlights">
      <div class="stat stat-big"><div class="num"{live_attr}>{esc(big[0])}</div><div class="lbl">{esc(big[1])}</div></div>
      {small}
      <div class="asof">{esc(d.get("asof", "As of Nov 2026"))}</div>
    </aside>"""

def static_eps_json(eps):
    import json
    return json.dumps([{"num": n, "date": f"{dt}, 2026", "yt": yt, "recap": rc, "bullets": b, "static": True} for n, dt, yt, rc, b in eps])

def k(n):
    return f"{n/1000:.1f}K".replace(".0K", "K") if n >= 1000 else str(n)

def live_bounty_html(lb):
    if not lb:
        return ""
    t, u, pool, posted, ends = lb
    return f'''<a class="b-live" href="{u}" target="_blank" rel="noopener">
      <div class="b-live-main">
        <div class="b-live-tags"><span class="live-tag"><i></i>Live</span><span>Posted {esc(posted)} · Ends {esc(ends)}</span></div>
        <h3>{hl(t)}</h3>
        <p>Clip Muneeb's recent interviews on New Era, Wolf of All Streets and The Block, and share them on X.</p>
      </div>
      <div class="b-live-side"><b>{pool}</b><span>STX reward pool</span><span class="b-live-cta">Enter the bounty →</span></div>
    </a>'''

def bounties_html(items):
    return "".join(f'''<a class="bounty" href="{u}" target="_blank" rel="noopener">
        <div class="b-top"><span class="b-week">Week of {esc(w)}</span><span class="b-pool">{pool} STX</span></div>
        <h3>{hl(t)}</h3>
        <div class="b-stats"><span><b>{e}</b> entries</span><span><b>{k(i)}</b> impressions</span><span><b>{k(g)}</b> engagements</span></div>
        <span class="post-more">View bounty →</span></a>''' for w, t, u, e, i, g, pool in items)

TL_ICONS = {
 "rocket": "M5 15c-1.5 1.5-2 5-2 5s3.5-.5 5-2M14 4c3-1 6-1 6-1s0 3-1 6l-6 6-5-5 6-6zM9 10l-3 1-2 3 4 1M14 15l-1 3-3 2-1-4",
 "gift": "M3 8h18v4H3zM5 12v9h14v-9M12 8v13M12 8S10 3 7.5 4 9 8 12 8zm0 0s2-5 4.5-4S15 8 12 8",
 "chart": "M3 17l6-6 4 4 8-8M15 7h6v6",
 "image": "M4 4h16v16H4zM9 10.5a1.5 1.5 0 1 0-.01 0M20 15l-5-5-9 10",
 "users": "M16 20v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 10a4 4 0 1 0 0-8 4 4 0 0 0 0 8M22 20v-2a4 4 0 0 0-3-3.9M16 2.1a4 4 0 0 1 0 7.8",
 "swap": "M7 7h13l-4-4M17 17H4l4 4",
 "cake": "M4 21h16v-8H4zM4 16c2 1.5 4 1.5 6 0s4-1.5 6 0 4 1.5 4 0M12 13V9M12 6a1.5 1.5 0 0 0 1.5-1.5C13.5 3 12 2 12 2s-1.5 1-1.5 2.5A1.5 1.5 0 0 0 12 6",
 "palette": "M12 3a9 9 0 1 0 0 18c1 0 1.5-.8 1.5-1.5 0-1.2-1-1.5-1-2.5s.8-1.5 2-1.5H17a4 4 0 0 0 4-4c0-4.4-4-8.5-9-8.5zM7.5 11.5h.01M10 7.5h.01M15 7.5h.01",
 "trophy": "M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0zM17 5h3v2a3 3 0 0 1-3 3M7 5H4v2a3 3 0 0 0 3 3",
 "shield": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z",
 "heart": "M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z",
 "spark": "M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z",
}
# title -> (icon, optional (big stat, stat label)) for the LEO timeline
TL_META = {
 "Leo comes on-chain": ("rocket", ("$5K", "launch market cap")),
 "Airdrop tour": ("gift", None), "Onto the exchanges": ("chart", None), "MEXC Kickstarter": ("trophy", None),
 "A week of firsts": ("spark", None),
 "The biggest airdrop in Stacks history": ("gift", ("5%", "of supply airdropped to STX holders")),
 "Listed on CoinMarketCap": ("chart", None), "Happy birthday, Leo": ("cake", None),
 "Leo Cats mint out": ("image", ("10K", "Leo Cats minted out")),
 "Halloween Leo": ("palette", None), "12 days of Christmas": ("gift", None), "Community first": ("heart", None),
 "Native Xverse swaps": ("swap", None), "First Bitcoin art drop": ("palette", None), "Meow Mondays": ("users", None),
 "Feline Fridays": ("users", None), "FPL league, year 3": ("trophy", None), "Two years on": ("cake", None),
 "Leo Cats NFT momentum": ("image", None), "Zest swap spotlight": ("swap", None), "HODLMM pool goes live": ("swap", None),
 "Stacks 4.0": ("spark", None), "Feed the Cat": ("chart", None),
 "No foundation, no games": ("shield", ("20%+", "of supply given to the Stacks community")),
 "New look, LEO₿": ("spark", None), "Leo Cats by the numbers": ("image", None), "Swap on Tenero": ("swap", None),
 "Growing Stacks, one cat at a time!": ("heart", None),
}

def timeline_html(items, rich=False):
    if not rich:
        out = ""
        for w, t, p, u in items:
            inner = f'<div class="when">{esc(w)}</div><h3>{esc(t)}</h3><p>{hl(p)}</p>'
            out += f'<a class="tl-item" href="{u}" target="_blank" rel="noopener">{inner}</a>' if u else f'<div class="tl-item">{inner}</div>'
        return f'<div class="tl">{out}</div>'
    out, year, side = "", None, 0
    for w, t, p, u in items:
        m = re.search(r"20\d\d", w)
        y = m.group(0) if m else "Now"
        if y != year:
            year = y
            out += f'<div class="ltl-year"><span>{y}</span></div>'
        icon, stat = TL_META.get(t, ("spark", None))
        svg = f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{TL_ICONS[icon]}"/></svg>'
        st = f'<div class="ltl-stat"><b>{esc(stat[0])}</b><span>{esc(stat[1])}</span></div>' if stat else ""
        more = '<span class="ltl-more">View on X ↗</span>' if u else ""
        inner = f'<div class="when">{esc(w)}</div><h3>{esc(t)}</h3>{st}<p>{hl(p)}</p>{more}'
        card = (f'<a class="ltl-card" href="{u}" target="_blank" rel="noopener">{inner}</a>' if u
                else f'<div class="ltl-card">{inner}</div>')
        cls = ("l" if side % 2 == 0 else "r") + (" feat" if stat else "")
        out += f'<div class="ltl-row {cls}"><div class="ltl-dot">{svg}</div>{card}</div>'
        side += 1
    return f'<div class="ltl"><img class="ltl-cap" src="../assets/leo.png" alt="">{out}</div>'

def episodes_html(eps):
    out = []
    for i, (num, date, yt, recap, bullets) in enumerate(eps):
        thumb = ""
        if yt:
            vid = yt.rsplit("/", 1)[-1]
            thumb = f' style="background-image:url(\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\')"'
        if i == 0:
            thumb = ' style="background-image:url(\'../episode-thumbnail.jpg\')"'
        watch = (f'<a class="chip" href="{yt}" target="_blank" rel="noopener"><svg><use href="#i-yt"/></svg>Watch</a>' if yt
                 else f'<a class="chip" href="{recap}" target="_blank" rel="noopener"><svg><use href="#i-x"/></svg>Watch on X</a>')
        lis = "".join(f"<li>{hl(b)}</li>" for b in bullets)
        out.append(f"""      <div class="ep">
        <div class="ep-thumb"{thumb}><span class="tag">EP.{num}</span></div>
        <div class="ep-body">
          <div class="ep-date">{date}, 2026</div>
          <ul>{lis}</ul>
          <div class="ep-links">{watch}<a class="chip" href="{recap}" target="_blank" rel="noopener"><svg><use href="#i-x"/></svg>Recap</a></div>
        </div>
      </div>""")
    return "\n".join(out)

def notice_html(d):
    if "notice" not in d:
        return ""
    return f'\n      <div class="notice"><b>Heads up:</b> {esc(d["notice"])}</div>'

def ca_html(d):
    if "contract" not in d:
        return ""
    c = esc(d["contract"])
    return f"""
      <div class="ca">Contract <code id="ca">{c}</code><a class="ca-link" href="https://explorer.hiro.so/txid/{c}?chain=mainnet" target="_blank" rel="noopener">Explorer ↗</a><button type="button" onclick="(function(b){{try{{navigator.clipboard.writeText(document.getElementById('ca').textContent);b.textContent='Copied';}}catch(e){{}}}})(this)">Copy</button></div>"""

def page(key):
    d = DATA[key]
    links = "".join(
        f'<a class="btn {"btn-primary" if i == 0 else "btn-ghost"}" href="{u}" target="_blank" rel="noopener"><svg><use href="#{ICON[k]}"/></svg>{esc(t)}</a>'
        for i, (k, t, u) in enumerate(d["links"]))
    body = ""
    if key == "stacked-up":
        ep = d["episodes"][0]
        vid = ep[2].rsplit("/", 1)[-1]
        body += f"""
<section id="latest" class="band-dark">
  <div class="wrap">
    <div class="label">Latest episode</div>
    <h2 data-live-episode-title>EP.{ep[0]} · {ep[1]}</h2>
    <div class="episode" id="episode" data-live-episode>
      <a class="facade" id="facade" data-video="{vid}" href="{ep[2]}" target="_blank" rel="noopener" style="background-image:url('../episode-thumbnail.jpg')">
        <div class="play"><svg viewBox="0 0 24 24"><path fill="#fff" d="M6 4l14 8-14 8z"/></svg></div>
      </a>
    </div>
  </div>
</section>

<section id="episodes" class="band-warm">
  <div class="wrap">
    <div class="label">Archive</div>
    <h2>Episodes</h2>
    <div class="eps" id="eps">
{episodes_html(d["episodes"])}
    </div>
    <a class="chip more-posts" href="https://www.youtube.com/@reubsbtc" target="_blank" rel="noopener"><svg><use href="#i-yt"/></svg>All episodes on YouTube</a>
  </div>
</section>
<section class="band-light" data-hide-empty hidden>
  <div class="wrap">
    <div class="label">On X</div>
    <h2>Latest from @StackedUpStream</h2>
    <div class="posts" data-live="StackedUpStream" data-count="4"></div>
  </div>
</section>
<script>window.STATIC_EPISODES = {static_eps_json(d["episodes"])};</script>"""
    else:
        extra_top = extra_mid = ""
        if "feature" in d:
            img, url, label = d["feature"]
            extra_top = f"""
<section>
  <div class="wrap">
    <a class="feature" href="{url}" target="_blank" rel="noopener">
      <div class="bar"><i></i><i></i><i></i><span>{label}</span><b>Visit {label} ↗</b></div>
      <img src="../assets/{img}" alt="{esc(d['title'])} website" loading="lazy">
    </a>
  </div>
</section>"""
        if "bridges" in d:
            br = "".join(f'<a class="bridge" href="{u}" target="_blank" rel="noopener"><div class="k">Bridge</div><h3>{esc(t)}</h3><p>{esc(p)}</p><span class="go">Open {esc(lbl)} ↗</span></a>' for t, p, u, lbl in d["bridges"])
            extra_top += f"""

<section class="band-warm">
  <div class="wrap">
    <div class="label">Get started</div>
    <h2>Bring assets to Stacks</h2>
    <div class="bridges">{br}</div>
  </div>
</section>"""
        if "podcasts" in d:
            mic = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/></svg>'
            play = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M8 5.5v13l11-6.5z"/></svg>'
            pc = "".join(f'<a class="pod" href="{u}" target="_blank" rel="noopener"><div class="pod-thumb"><img src="../assets/{img}" alt="{esc(show)} episode" loading="lazy"><span class="pod-play">{play}</span></div><div class="who"><b style="color:var(--ink)">{esc(show)}</b><br>{h} · {dt}</div><h3>{hl(t)}</h3><ul class="pod-list">{"".join(f"<li>{hl(x)}</li>" for x in bl)}</ul><span class="post-more">Watch on X →</span></a>' for show, h, dt, u, t, bl, img in d["podcasts"])
            extra_mid = f"""

<section class="band-warm">
  <div class="wrap">
    <div class="label">Listen</div>
    <h2>Recent Stacks podcasts</h2>
    <div class="pods">{pc}</div>
  </div>
</section>"""
        official = ""
        if "official" in d:
            oc = "".join(f'<a class="post" href="{u}" target="_blank" rel="noopener"><div class="post-head"><img src="../assets/stacks.png" alt=""><div><b>Stacks</b><span>@Stacks · {dt}</span></div><svg><use href="#i-x"/></svg></div><p>{hl(t)}</p><span class="post-more">View on X →</span></a>' for dt, u, t in d["official"])
            official = f"""

<section>
  <div class="wrap">
    <div class="label">Official</div>
    <h2>From @Stacks</h2>
    <div class="posts official">{oc}</div>
    <a class="chip more-posts" href="https://x.com/Stacks" target="_blank" rel="noopener"><svg><use href="#i-x"/></svg>Follow @Stacks</a>
  </div>
</section>"""
        mid = ""
        if "pillars" in d:
            pills = "".join(f'<div class="pillar"><div class="n">{n}</div><h3>{esc(t)}</h3><p>{esc(p)}</p></div>' for n, t, p in d["pillars"])
            mid = f"""
<section{' class="band-warm"' if not extra_top else ''}>
  <div class="wrap">
    <h2>{esc(d["pillars_title"])}</h2>
    <div class="pillars">{pills}</div>
  </div>
</section>"""
        if "bounties" in d:
            mid += f"""
<section class="band-legion">
  <div class="wrap">
    <div class="label">Zero Authority DAO</div>
    <h2>Bounties</h2>
    {live_bounty_html(d.get("live_bounty"))}
    <div class="b-sub">Previous bounties</div>
    <div class="bounties">{bounties_html(d["bounties"])}</div>
    <a class="chip more-posts" href="https://zeroauthoritydao.com/bounty-hub/72bc33ef-ada8-4d1a-bc68-551df2032f0d" target="_blank" rel="noopener"><svg><use href="#i-web"/></svg>All bounties on Zero Authority</a>
  </div>
</section>"""
        if "timeline" in d:
            mid += f"""
<section class="{"band-leotl" if key == "leo" else "band-warm"}">
  <div class="wrap">
    <div class="label">The story so far</div>
    <h2>Timeline</h2>
    {timeline_html(d["timeline"], rich=(key == "leo"))}
  </div>
</section>"""
        la, lf = d.get("live", ("", ""))
        live = f' data-live="{la}" data-count="6"' + (f' data-filter="{lf}"' if lf else "") if la else ""
        news_sec = "" if "news" not in d else f"""

<section id="news"{ {"leo": ' class="band-leo"', "tenero": ' class="band-tenero"'}.get(key, "") }>
  <div class="wrap">
    <div class="label">Latest news</div>
    <h2>What's happening</h2>
    <div class="posts"{live}>
{news_cards(d["news"])}
    </div>
  </div>
</section>"""
        body += extra_top + mid + extra_mid + official + news_sec
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d["title"])} | Reubs</title>
<meta name="description" content="{esc(d["title"])}: {esc(d["tagline"])}">
<link rel="icon" href="../avatar.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<style>{PAGE_CSS}</style>
</head>
<body data-base="../">
{SPRITE}
{nav(key)}

<header class="hero page-hero">
  <div class="wrap cover-wrap{' photo-wrap' if key in COVER_PHOTO else ''}">
    <a class="back" href="../">← Back to Reubs</a>
    {cover_html(key, d["title"], "../assets/" + d["logo"])}
  </div>
  <div class="wrap hero-grid">
    <div class="hero-main">
      <img class="page-logo" src="../assets/{d["logo"]}" alt="{esc(d["title"])}">
      <div class="role-pill">{esc(d["role"])}</div>
      <h1>{esc(d["title"])}<em>.</em></h1>
      <p><strong>{esc(d["tagline"])}</strong></p>
      {"".join(f'<p class="intro">{esc(t)}</p>' for t in (d["intro"] if isinstance(d["intro"], list) else [d["intro"]]))}{notice_html(d)}
      <div class="socials">{links}</div>{ca_html(d)}
    </div>
    {stats_html(d)}
  </div>
</header>
{body}

<footer>
  <div class="wrap">
    <span>© 2026 Reubs · <a href="../">reubs.link</a>{" · $LEO is a community memecoin with no utility. Not financial advice." if key == "leo" else ""}</span>
    <div class="icons">
      <a href="https://x.com/reubs_btc" target="_blank" rel="noopener" aria-label="X"><svg><use href="#i-x"/></svg></a>
      <a href="https://www.instagram.com/reubs.btc/" target="_blank" rel="noopener" aria-label="Instagram"><svg><use href="#i-ig"/></svg></a>
      <a href="https://www.youtube.com/@reubsbtc" target="_blank" rel="noopener" aria-label="YouTube"><svg><use href="#i-yt"/></svg></a>
      <a href="https://www.tiktok.com/@stackedupcrypto" target="_blank" rel="noopener" aria-label="TikTok"><svg><use href="#i-tt"/></svg></a>
    </div>
  </div>
</footer>
<script src="../live.js" defer></script>
<script src="../motion.js" defer></script>
</body>
</html>
"""


CONTACT = [
 ("Me", [
   ("x", "X", "@reubs_btc", "https://x.com/reubs_btc", "me.png"),
   ("ig", "Instagram", "@reubs.btc", "https://www.instagram.com/reubs.btc/", "me.png"),
   ("cmc", "CoinMarketCap", "reubsbtc · verified", "https://coinmarketcap.com/community/profile/reubsbtc/", "me.png"),
 ]),
 ("Stacked Up", [
   ("yt", "YouTube", "@reubsbtc", "https://www.youtube.com/@reubsbtc", "stackedup.png"),
   ("x", "X", "@StackedUpStream", "https://x.com/StackedUpStream", "stackedup.png"),
   ("tt", "TikTok", "@stackedupcrypto", "https://www.tiktok.com/@stackedupcrypto", "stackedup.png"),
 ]),
 ("Projects", [
   ("web", "Tenero", "tenero.io", "https://tenero.io/", "tenero.png"),
   ("x", "Tenero on X", "@tenero_io", "https://x.com/tenero_io", "tenero.png"),
   ("web", "Stacks", "stacks.co", "https://www.stacks.co/", "stacks.png"),
   ("x", "Stacks on X", "@Stacks", "https://x.com/Stacks", "stacks.png"),
   ("tg", "STX Legion", "Telegram community", "https://t.me/+wcOPrJbqGfxiMTY0", "legion.jpg"),
   ("x", "$LEO", "@LeoCoinSTX", "https://x.com/LeoCoinSTX", "leo.png"),
 ]),
]

CONTACT_CSS = """
  .c-group{margin-bottom:40px}
  .c-group h2{font-size:22px;margin-bottom:14px}
  .c-list{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
  @media(max-width:860px){.c-list{grid-template-columns:1fr}}
  .c-item{display:flex;align-items:center;gap:14px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 16px;box-shadow:0 1px 2px rgba(12,12,13,.04),0 8px 24px -16px rgba(12,12,13,.18);transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease}
  .c-item:hover{transform:translateY(-2px);border-color:var(--orange);box-shadow:0 16px 32px -18px rgba(252,100,50,.45)}
  .c-item img{width:44px;height:44px;border-radius:12px;flex-shrink:0}
  .c-item div{flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.3}
  .c-item b{font-size:15px}
  .c-item span{font-size:13px;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .c-item svg{width:18px;height:18px;color:var(--ink);flex-shrink:0}
  .c-item .arr{color:var(--orange);font-weight:700}
"""

def contact_page():
    groups = ""
    for title, items in CONTACT:
        cards = "".join(f'<a class="c-item" href="{u}" target="_blank" rel="noopener"><img src="../assets/{img}" alt=""><div><b>{esc(n)}</b><span>{esc(h)}</span></div><svg><use href="#{ICON[k]}"/></svg><span class="arr">↗</span></a>' for k, n, h, u, img in items)
        groups += f'<div class="c-group"><h2>{esc(title)}</h2><div class="c-list">{cards}</div></div>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contact | Reubs</title>
<meta name="description" content="All of Reubs' links in one place.">
<link rel="icon" href="../avatar.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
<style>{PAGE_CSS}{CONTACT_CSS}</style>
</head>
<body data-base="../">
{SPRITE}
{nav("contact")}

<header class="hero page-hero">
  <div class="wrap">
    <a class="back" href="../">← Back to Reubs</a>
    {cover_html("contact", "Contact", "../avatar.png")}
    <h1 style="margin-top:28px">Contact<em>.</em></h1>
    <p>All my links in one place. The quickest way to reach me is a DM on <a href="https://x.com/reubs_btc" target="_blank" rel="noopener" style="color:var(--orange);font-weight:600">X @reubs_btc</a>.</p>
  </div>
</header>

<section class="band-warm">
  <div class="wrap">
{groups}
  </div>
</section>

<footer>
  <div class="wrap">
    <span>© 2026 Reubs · <a href="../">reubs.link</a></span>
    <div class="icons">
      <a href="https://x.com/reubs_btc" target="_blank" rel="noopener" aria-label="X"><svg><use href="#i-x"/></svg></a>
      <a href="https://www.instagram.com/reubs.btc/" target="_blank" rel="noopener" aria-label="Instagram"><svg><use href="#i-ig"/></svg></a>
      <a href="https://www.youtube.com/@reubsbtc" target="_blank" rel="noopener" aria-label="YouTube"><svg><use href="#i-yt"/></svg></a>
      <a href="https://www.tiktok.com/@stackedupcrypto" target="_blank" rel="noopener" aria-label="TikTok"><svg><use href="#i-tt"/></svg></a>
    </div>
  </div>
</footer>
<script src="../live.js" defer></script>
<script src="../motion.js" defer></script>
</body>
</html>
"""

# Home page: inject mobile nav between markers
home_p = SITE / "index.html"
h = home_p.read_text()
btn, menu, tabs = mobile_nav("", "")
h = re.sub(r"\s*<!--mnav-->.*?<!--/mnav-->", "", h, flags=re.S)
h = h.replace('<div class="nav-links">', '<!--mnav-->' + '<!--/mnav-->' + '<div class="nav-links">', 1) if False else h
h = re.sub(r'(<div class="nav-links">.*?</div>)', lambda m: m.group(1) + "\n    <!--mnav-->" + btn + "<!--/mnav-->", h, count=1, flags=re.S)
h = re.sub(r'(  </div>\n</nav>)', lambda m: "  </div>\n  <!--mnav-->" + menu + "<!--/mnav-->\n</nav>\n<!--mnav-->" + tabs + "<!--/mnav-->", h, count=1)
home_p.write_text(h)

for key, _ in ORDER:
    p = SITE / key
    p.mkdir(exist_ok=True)
    (p / "index.html").write_text(page(key))
(SITE / "contact").mkdir(exist_ok=True)
(SITE / "contact" / "index.html").write_text(contact_page())
print("built", [k for k, _ in NAV])
