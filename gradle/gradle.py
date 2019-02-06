import bs4
import requests
from urllib.request import Request, urlopen

print("\nscraping jobs at gradle")
site= "https://boards.greenhouse.io/gradle"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")
jobs = bs.find_all('div',{'class':'opening'})
print(len(jobs))
open('gradle-jobs.txt','w').close()
file = open('gradle-jobs.txt','a+')
for job in jobs:
    link = 'https://boards.greenhouse.io'+job.find('a')['href']
    # print(link)
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    title = bs1.find('h1',{'class':'app-title'}).get_text()
    location = bs1.find('div',{'class':'location'}).get_text().strip("\n").strip(" ")
    description = bs1.find('div',{'id':'content'}).get_text()
    # print(title,location)
    file.write("Title: "+title+"\nLocation: "+location+"\nDescription: "+description)
    file.write("\n--------------------------------\n")
file.close()
print("gradle jobs scraped successfully")
