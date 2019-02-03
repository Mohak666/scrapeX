import bs4
from urllib.request import Request, urlopen

site= "https://boards.greenhouse.io/haven"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")

jobs = bs.find_all('div',{'class':'opening'})
open('haven-jobs.txt','w').close()
file = open('haven-jobs.txt','a+')
file.write("\n\n\t\t\t HAVEN JOBS\n\n")
for job in jobs:
    item = job.find('a')
    link = "https://boards.greenhouse.io"+item['href']
    title = item.get_text()
    location = job.find('span').get_text()

    req1 = Request(link,headers=hdr)
    descriptionHTML = urlopen(req1)
    bs1 = bs4.BeautifulSoup(descriptionHTML,"html.parser")
    description = bs1.find('div',{'id':'content'}).get_text()
    file.write('Title: '+title+"\nLocation: "+location+"\nDescription: \n\t"+description)
    file.write('\n-----------------------------\n')
file.close()
