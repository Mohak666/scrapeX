import requests
import bs4

file = open('jobs.txt','w')
file.write('')
file.close()
file = open('jobs.txt','a+')

# scraping for Aporeto jobs
url  = 'https://www.aporeto.com/job-listings/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'job-listing__text'})
# print(jobs)
file.write("\t\t\t\t\t APORETO JOBS\n\n")
for job in jobs:
    title = job.find('h2').get_text()
    location = job.find('h4').get_text()
    description = job.find('p').getText()

    file.write("Title:"+ title +"\n")
    file.write("Location:"+ location +"\n")
    file.write("Description:"+ description +"\n")
    file.write("\n\n")


# scraping for descartes jobs
file.write("\n\n\t\t\t\t\t DESCARTES JOBS\n\n")
url  = 'https://jobs.lever.co/descarteslabs.com/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")
jobs = bs.find_all('a',{"class":"posting-title"})

for job in jobs:
    title = job.find('h5').get_text()
    location = job.find('span',{"class":"sort-by-location posting-category small-category-label"}).get_text()
    positionCategory = job.find("span",{"class":"sort-by-team posting-category small-category-label"}).get_text()
    commitment = job.find("span",{"class":"sort-by-commitment posting-category small-category-label"}).get_text()

    file.write("Title: "+title+"\n")
    file.write("Location: "+location+"\n")
    file.write("Category: "+ positionCategory+"\n")
    file.write("Commitment: "+commitment+"\n")
    file.write("\n\n")


# scraping for mesosphere jobs
url  = 'https://mesosphere.com/careers/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")
jobs = bs.find_all('div',{'class':'careers-view__job-item-info'})
file.write("\n\n\t\t\t\t\t MESOSPHERE JOBS\n\n")
for job in jobs:
    title = job.find('span',{'class':'careers-view__job-item-title'}).get_text()
    location = job.find('span',{'class':'careers-view__job-item-location text-color-gray-light small flush-bottom'}).get_text()
    title = title.split('-')
    if(len(title)>1):
        file.write("Title: "+title[0]+"\n")
        file.write("Speciality/Area: "+title[1]+"\n")
    else:
        file.write("Title: "+title[0]+"\n")
    file.write("Location: "+location+"\n\n")

# scraping for rocketlabusa jobs
url  = 'https://www.rocketlabusa.com/careers/positions/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"lxml")

jobs = bs.find_all('a',{'class':'job'})
# print(jobs)

file.write("\n\n\t\t\t\t\t ROCKETLABUSA JOBS\n\n")
for job in jobs:
    title = job.find('h3').get_text()
    location = job.find('h5').get_text()

    file.write('Title: '+title+"\n")
    file.write('Location: '+location+"\n\n")

# scraping for checkr jobs
url  = 'https://checkr.com/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('a',{'class':'career question kitchensink'})
file.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
for job in jobs:
    title = job.find('span').get_text()
    file.write("Title: "+title+"\n")
file.write("\n\n")


# scraping for interana jobs
url  = 'https://boards.greenhouse.io/interana'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'opening'})
file.write("\n\n\t\t\t\t\t INTERANA JOBS\n\n")
for job in jobs:
    title = job.find('a').get_text()
    location = job.find('span').get_text()
    file.write("Title: "+title+"\n")
    file.write("Location: "+location+"\n\n")
file.write("\n")

file.close()
