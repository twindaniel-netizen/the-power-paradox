"""Builds the static pages for https://twindaniel-netizen.github.io/the-power-paradox/ (GitHub Pages).
Run: py -3.12 site\\_build.py"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
UPDATED = "November 20, 2026"
YT = "https://www.youtube.com/@ThePowerParadox-f9f"
FB = "https://www.facebook.com/profile.php?id=61596781859469"

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | The Power Paradox</title><link rel="icon" href="favicon.png"><link rel="stylesheet" href="style.css"></head>
<body><main><header><img src="logo.png" alt="The Power Paradox logo"><a href="./">THE POWER PARADOX</a></header>"""
FOOT = f"""<nav><a href="./">Home</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms</a>
<a href="data-deletion.html">Data deletion</a><a href="{YT}">YouTube</a><a href="{FB}">Facebook</a></nav></main></body></html>"""

PAGES = {
    "index.html": ("Home", f"""<h1>Power, accountability, consequences.</h1>
<p>The Power Paradox is a video publication that explains decisions by President Trump and his administration, their collisions with
courts, institutions and public opinion, and their documented consequences. Every episode is built from primary documents
(court orders, filings, official records) and attributed reporting.</p>
<p>Watch on <a href="{YT}">YouTube</a> or follow the <a href="{FB}">Facebook Page</a>.</p>
<h2>Publishing tool</h2>
<p>"The Power Paradox Publisher" is the channel's own internal tool. It uploads the channel's finished videos to its own YouTube channel
and its own Facebook Page. It has no other users and does not collect data from viewers.</p>"""),
    "privacy.html": ("Privacy Policy", f"""<h1>Privacy Policy</h1><p class="muted">Last updated: {UPDATED}</p>
<p>This policy covers the website at this address and the internal publishing tool "The Power Paradox Publisher" (a Facebook/Meta app and a
YouTube API client used only by the channel's owner).</p>
<h2>What we collect</h2>
<p>Nothing from visitors. This website has no cookies, no analytics, no forms and no third-party scripts.</p>
<p>The publishing tool is used only by the channel's owner. To publish videos it stores, on the owner's own computer, an access token for
the channel's own Facebook Page and YouTube channel. It does not access, store or share any data about other people, page followers or
viewers.</p>
<h2>How the tokens are used</h2>
<p>Only to upload the channel's own videos, set their titles, descriptions, thumbnails and captions, and read the status of those uploads.
Tokens are never sold, shared or transferred.</p>
<h2>Third parties</h2>
<p>Videos are published on YouTube (Google) and Facebook (Meta), whose own privacy policies apply to anyone watching there.</p>
<h2>Retention and deletion</h2>
<p>The owner can revoke the tool's access at any time in Facebook settings (Business integrations) or in the Google account
(Third-party connections). See <a href="data-deletion.html">Data deletion</a>.</p>
<h2>Contact</h2><p>Message the <a href="{FB}">The Power Paradox Facebook Page</a>.</p>"""),
    "terms.html": ("Terms of Service", f"""<h1>Terms of Service</h1><p class="muted">Last updated: {UPDATED}</p>
<p>The content of The Power Paradox is provided for information and commentary. We work from primary documents and attribute claims;
we correct errors when they are found. Nothing here is legal advice.</p>
<p>"The Power Paradox Publisher" is an internal tool, not a public service. It is operated only by the channel's owner to publish the
channel's own videos. No one else can sign in to it.</p>
<p>Images and footage used in our videos are public domain or used under their licenses, credited in each video's description.</p>
<p>Questions: message the <a href="{FB}">Facebook Page</a>.</p>"""),
    "data-deletion.html": ("Data deletion", f"""<h1>Data deletion instructions</h1><p class="muted">Last updated: {UPDATED}</p>
<p>"The Power Paradox Publisher" does not store data about any user other than the channel's owner, and it has no other users.</p>
<p>To remove the tool's access to a Facebook account: Facebook → Settings &amp; privacy → Settings → Business integrations → select
"The Power Paradox Publisher" → Remove. The stored page token stops working immediately.</p>
<p>To remove access to a Google/YouTube account: Google Account → Security → Third-party apps with account access → remove the app.</p>
<p>For any other request, message the <a href="{FB}">Facebook Page</a>.</p>"""),
    "oauth.html": ("Authorization", """<h1>Authorization received</h1>
<p id="msg">Forwarding the authorization to the publishing tool on this computer…</p>
<script>
// Facebook redirects here after the owner approves the app. The code is handed to the local tool listening on 127.0.0.1:8769
// (only reachable from the owner's own computer). Nothing is sent anywhere else and nothing is stored on this site.
(function () {
  var q = window.location.search;
  if (!q || q.indexOf('state=') < 0) { document.getElementById('msg').textContent = 'No authorization data in this address.'; return; }
  window.location.replace('http://127.0.0.1:8769/' + q);
})();
</script>"""),
}

for name, (title, body) in PAGES.items():
    (HERE / name).write_text(HEAD.format(title=title) + body + FOOT, encoding="utf-8")
print("built", ", ".join(PAGES))
