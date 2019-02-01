import requests
import bs4

url  = 'https://www.rocketlabusa.com/careers/positions/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('a',{'class':'job'})
# print(jobs)

file = open('rocketlabusa-jobs.txt','a+')
file.write("\n\n\t\t\t ROCKETLABUSA JOBS\n\n")
for job in jobs:
    link = job['href']
    link = "https://www.rocketlabusa.com"+link
    title = job.find('h3').get_text()
    location = job.find('h5').get_text()

    file.write('Title: '+title+"\n")
    file.write('Location: '+location+"\n")
    file.write('Description: \n')
    # print(link)
    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    text = bs1.find('div',{'class':'job__info-subtitle'}).get_text()
    file.write("\t\t"+text+"\n\n\n")

file.close()
