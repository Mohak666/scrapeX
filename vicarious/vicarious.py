import bs4
from urllib.request import Request, urlopen

site= "https://www.vicarious.com/careers/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")
jobs = bs.find_all('div',{'class':'job-posting'})
open('vicarious-jobs.txt','w').close()
file = open('vicarious-jobs.txt','a+')

for job in jobs:
    title = job.find('div',{'class':'job-title'}).get_text()
    title = title.strip('\n').lstrip('\t').strip('\n')
    # print(title)
    description = job.find('div',{'class':'job-description'}).get_text()
    file.write('Title: '+title+"\nDescription: "+description)
    file.write("\n---------------------------\n")
