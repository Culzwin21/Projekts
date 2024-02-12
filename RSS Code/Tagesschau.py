import feedparser


url = "https://www.tagesschau.de/infoservices/alle-meldungen-100~rss2.xml"
feed = feedparser.parse(url)

print(feed)

now = datetime.now()
time_range = timedelta(days=1)

for entry in feed.entries:
    entry_date = datetime.strptime(entry.published," %a, %d %b %Y %H:%M:%S %z")
    if now - entry_date <= time_range:
        print("tagesschau.de - Die Nachrichten der ARD",entry.title)
        print("https://www.tagesschau.de/infoservices/alle-meldungen-100.html",entry.link)
        print("Mon, 12 Feb 2024 10:05:14 +0100",entry.published)
        print("Die aktuellen Beiträge der Seite https://www.tagesschau.de/infoservices/alle-meldungen-100.html",entry.summery)

