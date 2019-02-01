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
    title = job.find('a').get_text()
    location = job.find('span').get_text()
    file.write("Title: "+title+"\n")
    file.write("Location: "+location+"\n\n")
file.write("\n")
file.close()
