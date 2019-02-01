import requests
import bs4

url  = 'https://boards.greenhouse.io/interana'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'opening'})
# print(jobs)
file = open('interana-jobs.txt','a+')
file.write("\n\n\t\t\t\t\t INTERANA JOBS\n\n")
for job in jobs:
    link = job.find('a')['href']
    link = "https://boards.greenhouse.io"+link
    title = job.find('a').get_text()
    location = job.find('span').get_text()
    file.write("Title: "+title+"\n")
    file.write("Location: "+location+"\n\n")
    file.write("Description: \n")
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'id':'content'}).get_text()
    containers = bs1.find_all('div',{'class':'section page-centered'})
    print(len(containers))
    if(len(containers)>0):
        for container in containers:
            file.write("\t\t"+container.get_text()+"\n")
    else:
        file.write("\t\t"+content+"\n")
    file.write("\n\n---------------------------\n")
file.write("\n\n")
file.close()
