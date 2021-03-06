import requests
import bs4

url  = 'https://checkr.com/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('a',{'class':'career question kitchensink'})
# print(jobs)
open("checkr-jobs.txt",'w').close()
file = open('checkr-jobs.txt','a+')
file.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
for job in jobs:
    link = job['href']
    title = job.find('span').get_text().strip('\n')
    file.write("Title: "+title+"\n")

    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'id':'content'}).get_text()
    location = bs1.find('div',{'class':'location'}).get_text()
    file.write("Location: "+location+"\n")
    file.write("Description: \n")
    file.write(content)
    file.write("\n---------------------\n")
file.write("\n\n")
file.close()
