import json
import urllib.request
import os
import datetime 

searchItem = input("enter name\n")
n = input("enter number\n") 
url = "https://thenounproject.com/search/json/icon/?q=" + searchItem + "&page=1&limit=" + n + "&raw_html=false"
resp = json.loads(urllib.request.urlopen(url).read())

directory = searchItem +  '{0:%H-%M-%S}'.format(datetime.datetime.now())
os.makedirs(directory)

i = 0
for icon in resp["icons"]:
    link = icon["preview_url"]  # you can choose another with specific size
    g = urllib.request.urlopen(link)
    with open( "./" + directory + "/" + str(i) + ".png", 'b+w') as f:
        f.write(g.read())    
    i = i + 1

