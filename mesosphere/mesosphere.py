import requests
import bs4

url  = 'https://mesosphere.com/careers/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'careers-view__job-item-info'})

file = open("mesosphere-jobs.txt",'a+')
for job in jobs:
    title = job.find('span',{'class':'careers-view__job-item-title'}).get_text()
    location = job.find('span',{'class':'careers-view__job-item-location text-color-gray-light small flush-bottom'}).get_text()
    title = title.split('-')
    if(len(title)>1):
        file.write("Title: "+title[0]+"\n")
        file.write("Speciality/Area: "+title[1]+"\n")
    else:
        file.write("Title: "+title[0]+"\n")
    file.write("Location: "+location+"\n\n\n")

file.close()
