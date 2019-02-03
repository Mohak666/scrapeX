import requests
import bs4

url  = 'https://www.pluribusnetworks.com/company/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'career'})
# print(len(jobs))
open('pluribus-jobs.txt','w').close()
file = open('pluribus-jobs.txt','a+')
file.write("\n\n\t\t\t\t\t PLURIBUSNETWORKS JOBS\n\n")
for job in jobs:
    item = job.find('a')
    link = item['href']
    title = item.get_text()
    location = job.find('strong',{'class':'career-location'}).get_text()
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'class':'career'}).get_text()
    content = content.split('|')

    content = content[1]
    file.write("Title: "+title+"\n"+"Location: "+location+"\n Description: \n")
    file.write("\t"+content+"\n------------------\n")
file.close()
