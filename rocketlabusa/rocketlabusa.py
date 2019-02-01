import requests
import bs4

url  = 'https://www.rocketlabusa.com/careers/positions/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('a',{'class':'job'})
# print(jobs)

file = open('rocketlabusa-jobs.txt','a+')
file.write("\n\n\t\t\t ROCKETLABUSA\n\n")
for job in jobs:
    title = job.find('h3').get_text()
    location = job.find('h5').get_text()

    file.write('Title: '+title+"\n")
    file.write('Location: '+location+"\n\n")

file.close()
