
# Copyright 2017 Anant Sujatanagarjuna <anant.essen@gmail.com>
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

