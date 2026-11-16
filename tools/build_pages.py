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
    ["Why negative news stopped moving the price", "The quantum question and self-custody", "Bitcoin as an income-generating asset"]),
   ("The White Papers · The Block", "@TheBlockCo", "Nov 10", "https://x.com/TheBlockCo/status/2120212634914238747",
    "Muneeb on turning bitcoin into productive capital",
    ["How Stacks bonds pay bitcoin holders 3% in BTC", "Stacks vs. Lightning", "The quantum threat and Satoshi's coins"]),
   ("The Wolf Of All Streets", "@scottmelker", "Nov 9", "https://x.com/scottmelker/status/2119859166600990761",
    "Bitcoin's Biggest \"Bond\" Yet Just Sold Out — What Do Institutions Know?",
    ["Why Muneeb is returning to lead Stacks", "Bullish joins the 1,000 BTC Stacks bond", "How Bitcoin yield could drive value to STX"]),
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
  "intro": "Live every Wednesday, 3pm UK / 10am EST — the week in Bitcoin and Stacks, market data from Tenero, DeFi strategies and community spotlights.",
  "links": [("yt", "YouTube", "https://www.youtube.com/@reubsbtc"), ("x", "@StackedUpStream", "https://x.com/StackedUpStream"), ("tt", "TikTok", "https://www.tiktok.com/@stackedupcrypto")],
  "stats_big": ("8", "Episodes so far"),
  "stats_big_live": "episodes",
  "stats": [("Weekly", "Every Wednesday"), ("3pm UK", "10am EST"), ("3", "Platforms: YouTube, X, TikTok"), ("Shorts", "On TikTok & YouTube")],
  # episodes: (num, date, watch_url, recap_url, bullets)
  "episodes": [
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
  "intro": "$LEO is Muneeb's pet cat, living on the Stacks blockchain. It launched at a $5k market cap around three years ago, started the airdrop meta on Stacks and is still here.",
  "live": ("LeoCoinSTX", ""),
  "notice": "$LEO is a community memecoin with no utility and no intrinsic value. Nothing on this page is financial advice.",
  "links": [("x", "@LeoCoinSTX", "https://x.com/LeoCoinSTX"),
            ("web", "Trade on Tenero", "https://tenero.io/stacks/swap?from=STX&to=SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token"),
            ("web", "Trade on Zest", "https://app.zestprotocol.com/swap/stx-to-leo"),
            ("web", "Trade on Bitflow", "https://app.bitflow.finance/pools/dlmm/SM1FKXGNZJWSTWDWXQZJNF7B5TV5ZB235JTCXYXKD.dlmm-pool-leo-stx-v-1-bps-50")],
  "stats_big": ("$5K", "Launch market cap, ~3 years ago"),
  "stats": [("4,200", "STX — top Leo Cat sale"), ("30M", "LEO trader rewards via Bitflow"), ("125K", "STX Leo Cats all-time volume"), ("2", "ALEX DEX hacks survived")],
  "asof": "From @LeoCoinSTX posts",
  "contract": "SP1AY6K3PQV5MRT6R4S671NWW2FRVPKM0BR162CT6.leo-token",
  "timeline": [
   ("~2023", "LEO launches", "Muneeb's pet cat launches on Stacks at a $5k market cap and kicks off the airdrop meta, distributing millions to STX supporters and OGs.", "https://x.com/LeoCoinSTX/status/2111939543935164519"),
   ("2023–25", "Surviving the bear", "Survives 90%+ STX drawdowns and two ALEX DEX hacks, which hit its main liquidity pool at the time.", "https://x.com/LeoCoinSTX/status/2111939543935164519"),
   ("Jul 2025", "Meow Mondays & bounties", "Weekly community bounties launch on Zero Authority DAO, alongside LEO farming on Bitflow.", "https://x.com/LeoCoinSTX/status/1944654228477427798"),
   ("Sep 2025", "Bye bye MEXC", "LEO asks to be voluntarily delisted from MEXC — this cat will not be bossed around.", "https://x.com/LeoCoinSTX/status/1965386994714046561"),
   ("Jun 2026", "Record Leo Cat sale", "A rarity #1 Leo Cat sells for 4,200 STX, the highest sale of all time. Leo Cats can now be inscribed on Bitcoin too.", "https://x.com/LeoCoinSTX/status/2067213543565586889"),
   ("Jul 2026", "HODLMM pool on Bitflow", "The LEO/STX HODLMM pool goes live on Bitflow, with 30M LEO in trader rewards.", "https://x.com/LeoCoinSTX/status/2075637768857010576"),
   ("Sep 2026", "Leo Cats climb the charts", "Leo Cats reach 16th in all-time STX NFT volume, with 125k STX traded.", "https://x.com/LeoCoinSTX/status/2099842841489154339"),
   ("Oct 2026", "Swap on Tenero", "LEO becomes swappable directly on Tenero, and 30M LEO (~$3,000) in 'Feed the Cat' rewards are distributed.", "https://x.com/LeoCoinSTX/status/2107848804808663418"),
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
ORDER = [("stacks", "Stacks"), ("tenero", "Tenero"), ("stacked-up", "Stacked Up"), ("leo", "LEO")]
NAV = ORDER + [("contact", "Contact")]
AUTHORS = {"reubs": ("reubs", "@reubs_btc", "../assets/me.png", True),
           "tenero": ("Tenero", "@tenero_io", "../assets/tenero.png", False),
           "leo": ("LEO", "@LeoCoinSTX", "../assets/leo.png", False)}
ICON = {"x": "i-x", "web": "i-web", "yt": "i-yt", "tt": "i-tt", "ig": "i-ig", "tg": "i-tg", "cmc": "i-verified"}

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
  .pod .mic{width:44px;height:44px;border-radius:12px;background:var(--orange-soft);color:var(--orange);display:grid;place-items:center}
  .pod .mic svg{width:22px;height:22px}
  .pod .who{font-size:13px;color:var(--muted)}
  .pod h3{font-size:17px;font-weight:700;line-height:1.35}
  .pod-list{list-style:none;font-size:14px;color:var(--muted);line-height:1.5;flex:1}
  .pod-list li{padding-left:16px;position:relative;margin-bottom:4px}
  .pod-list li::before{content:"→";position:absolute;left:0;color:var(--orange)}
"""

MENU = [("", "Home", "me.png"), ("stacks/", "Stacks", "stacks.png"), ("tenero/", "Tenero", "tenero.png"),
        ("stacked-up/", "Stacked Up", "stackedup.png"), ("leo/", "LEO", "leo.png"), ("contact/", "Contact", "me.png")]

def mobile_nav(base, active):
    """Hamburger button + dropdown + fixed bottom tab bar. base='' for home, '../' for subpages."""
    btn = '<button class="menu-btn" type="button" aria-label="Menu" onclick="document.body.classList.toggle(\'menu-open\')"><span></span><span></span><span></span></button>'
    menu = "".join(f'<a href="{(base + h) or './'}"{" class=\"on\"" if h == active else ""}><img src="{base}assets/{img}" alt="">{t}<span class="arr">→</span></a>' for h, t, img in MENU)
    tabs = "".join(f'<a href="{(base + h) or './'}"{" class=\"on\"" if h == active else ""}><img src="{base}assets/{img}" alt="">{t}</a>' for h, t, img in MENU[:5])
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

def timeline_html(items):
    return "".join(f'<a class="tl-item" href="{u}" target="_blank" rel="noopener"><div class="when">{esc(w)}</div><h3>{esc(t)}</h3><p>{hl(p)}</p></a>' for w, t, p, u in items)

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
      <div class="ca">Contract <code id="ca">{c}</code><button type="button" onclick="(function(b){{try{{navigator.clipboard.writeText(document.getElementById('ca').textContent);b.textContent='Copied';}}catch(e){{}}}})(this)">Copy</button></div>"""

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
            pc = "".join(f'<a class="pod" href="{u}" target="_blank" rel="noopener"><div class="mic">{mic}</div><div class="who"><b style="color:var(--ink)">{esc(show)}</b><br>{h} · {dt}</div><h3>{hl(t)}</h3><ul class="pod-list">{"".join(f"<li>{hl(x)}</li>" for x in bl)}</ul><span class="post-more">Watch on X →</span></a>' for show, h, dt, u, t, bl in d["podcasts"])
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
        if "timeline" in d:
            mid += f"""
<section class="band-warm">
  <div class="wrap">
    <div class="label">The story so far</div>
    <h2>Timeline</h2>
    <div class="tl">{timeline_html(d["timeline"])}</div>
  </div>
</section>"""
        la, lf = d.get("live", ("", ""))
        live = f' data-live="{la}" data-count="6"' + (f' data-filter="{lf}"' if lf else "") if la else ""
        body += extra_top + mid + extra_mid + official + f"""

<section id="news">
  <div class="wrap">
    <div class="label">Latest news</div>
    <h2>What's happening</h2>
    <div class="posts"{live}>
{news_cards(d["news"])}
    </div>
  </div>
</section>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(d["title"])} — Reubs</title>
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
  <div class="wrap hero-grid">
    <div class="hero-main">
      <a class="back" href="../">← Back to Reubs</a>
      <img class="page-logo" src="../assets/{d["logo"]}" alt="{esc(d["title"])}">
      <div class="role-pill">{esc(d["role"])}</div>
      <h1>{esc(d["title"])}<em>.</em></h1>
      <p><strong>{esc(d["tagline"])}</strong></p>
      <p class="intro">{esc(d["intro"])}</p>{notice_html(d)}
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
<title>Contact — Reubs</title>
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
    <h1>Contact<em>.</em></h1>
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
