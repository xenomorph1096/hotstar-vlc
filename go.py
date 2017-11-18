import urllib2 as url
import json
import os
fullurl = raw_input("Enter Hotstar URL with ID . eg: 'http://www.hotstar.com/../../../../../2001703793' (ID at the end is important).\nAlternatively Enter just the ID.\n:> ")
id = fullurl.split("/")[-1]
print("Using ID : "+ id)
print("Fetching Stream Link ...");
jsonString = url.urlopen("http://getcdn.hotstar.com/AVS/besc?action=GetCDN&asJson=Y&channel=TABLET&id="+id+"&type=VOD").read()
print("Fetched.")
res = json.loads(jsonString)
streamLink = res["resultObj"]["src"]
print ("Open this link with an application like vlc/gnome-mplayer etc: " + streamLink)
os.system("vlc "+streamLink)

