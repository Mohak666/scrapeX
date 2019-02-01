import requests
import bs4

url  = 'https://checkr.com/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"lxml")

jobs = bs.find_all('a',{'class':'career question kitchensink'})
# print(jobs)
file = open('checr-jobs.txt','a+')
file.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
for job in jobs:
    title = job.find('span').get_text()
    file.write("Title: "+title+"\n")
file.write("\n\n")
file.close()
