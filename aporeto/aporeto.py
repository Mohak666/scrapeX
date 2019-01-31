import requests
import bs4

url  = 'https://www.aporeto.com/job-listings/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'job-listing__text'})
# print(jobs)
file = open('aporeto-jobs.txt','a+')
for job in jobs:
    title = job.find('h2').get_text()
    location = job.find('h4').get_text()
    description = job.find('p').getText()

    file.write("Title:"+ title +"\n")
    file.write("Location:"+ location +"\n")
    file.write("Description:"+ description +"\n")
    file.write("\n\n")
file.close()
