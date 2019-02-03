import requests
import bs4
import re
url  = 'https://jobs.jobvite.com/sentinelone/jobs'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('td',{'class':'jv-job-list-name'})
# print(len(jobs))
open("sentinelone-jobs.txt",'w').close()
file = open("sentinelone-jobs.txt",'a+')
for job in jobs:
    item = job.find('a')
    link = "https://jobs.jobvite.com"+item['href']
    title = item.get_text()
    # print(title,link)
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    department = bs1.find('p',{'class':'jv-job-detail-meta'}).get_text().strip(' ')
    location = bs1.find('span',{'class':'jv-inline-separator'}).get_text().strip('\n')
    description = bs1.find('div',{'class':'jv-job-detail-description'}).get_text()

    file.write("Title: +"+title+"\nDetails: "+department+"\n"+description)
    file.write("\n----------------------\n")
file.close()
