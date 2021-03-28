#!/usr/bin/python3
# Instragram Video Downloader by Bar v0.2 , Thx Someone for Regex

print("++++ Instagram Video Downloader by Bar. ++++")

import sys,re,urllib,os,requests
try:
    from bs4 import BeautifulSoup as BS
except ImportError:
    print("Instal[ar]l: BeautifulSoup!")
    sys.exit(1)

if len(sys.argv) != 3:
    print("Uso: ./"+sys.argv[0]+" id_post name_local_video.")
    sys.exit(1)

id_video = sys.argv[1]
link_video = "https://www.instagram.com/p/" + id_video

content = urllib.request.urlopen(link_video)
soup = BS(content, "html.parser")
pattern = re.compile('"video_url":"([^"]+)"')
match = re.search(pattern, str(soup))
if match:
    video_url = match.group(1)
    print("[*] Link Video Found/Encontrado!")
else:
    print("No Video Link")
    sys.exit(1)

r = requests.get(video_url)
if r.status_code==200:
    print("[+] HTTP Response:" + str(r.status_code))
    print("[+] Downloading/Bajando Video!")


cwd = os.getcwd()+'/'+sys.argv[2]
with open(cwd, 'wb') as f:
    f.write(r.content)

try:
    video_bajado= open(cwd, 'r')
    print("Video in:" + cwd)
except FileNotFoundError:
    sys.exit(1)
