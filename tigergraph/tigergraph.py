import bs4
import requests
from urllib.request import Request, urlopen

print("\nscraping jobs at tigergraph")
site= "https://boards.greenhouse.io/tigergraph"
hdr = {'User-Agent': 'Mozilla/5.0','Accept-Language':'en-US,en;q=0.5'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")
jobs = bs.find_all('div',{'class':'opening'})
# print(len(jobs))
open('tigergraph-jobs.txt','w').close()
file = open('tigergraph-jobs.txt','a+')
for job in jobs:
    link = 'https://boards.greenhouse.io'+job.find('a')['href']
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    title = bs1.find('h1',{'class':'app-title'}).get_text()
    location = bs1.find('div',{'class':'location'}).get_text().strip("\n").strip(" ")
    description = bs1.find('div',{'id':'content'}).get_text()
    # print(title,location)
    file.write("Title: "+title+"\nLocation: "+location+"\nDescription: "+description)
    file.write("\n--------------------------------\n")
file.close()
print("tigergraph jobs scraped successfully")
