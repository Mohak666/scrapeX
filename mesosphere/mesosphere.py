import requests
import bs4

url  = 'https://mesosphere.com/careers/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'careers-view__jobs-item'})

file = open("mesosphere-jobs.txt",'a+')
# print(jobs[0])
for job in jobs:
    link = job.find('a')['href']
    title = job.find('span',{'class':'careers-view__job-item-title'}).get_text()
    location = job.find('span',{'class':'careers-view__job-item-location text-color-gray-light small flush-bottom'}).get_text()
    title = title.split('-')
    # print(link)
    if(len(title)>1):
        file.write("Title: "+title[0]+"\n")
        file.write("Speciality/Area: "+title[1]+"\n")
    else:
        file.write("Title: "+title[0]+"\n")
    file.write("Location: "+location+"\nDescription: \n")

    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    container = bs1.find('div',{'id':'content'})
    entities = container.find_all('span',{'style':"font-weight: 400;"})
    for entity in entities:
        file.write("\t\t"+entity.get_text()+"\n")
        # print('done')
    file.write("\n\n")
file.close()
