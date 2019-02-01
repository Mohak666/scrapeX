import requests
import bs4

file = open('all-jobs.txt','w')
file.write('')
file.close()
file = open('all-jobs.txt','a+')


# scraping for Aporeto jobs
file1 = open('aporeto-jobs.txt','w')
file1.write('')
file1.close()
file1=open('aporeto-jobs.txt','a+')
print("Scraping aporeto jobs")
url  = 'https://www.aporeto.com/job-listings/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'job-listing__text'})
# print(jobs)
file.write("\t\t\t\t\t APORETO JOBS\n\n")
file1.write("\t\t\t\t\t APORETO JOBS\n\n")
for job in jobs:
    title = job.find('h2').get_text()
    location = job.find('h4').get_text()
    description = job.find('p').getText()

    file.write("Title:"+ title +"\n")
    file.write("Location:"+ location +"\n")
    file.write("Description:"+ description +"\n")
    file.write("\n\n")
    file1.write("Title:"+ title +"\n")
    file1.write("Location:"+ location +"\n")
    file1.write("Description:"+ description +"\n")
    file1.write("\n\n")
print("Aporeto jobs scraped successfully")
file1.close()


# scraping for descartes jobs
file1 = open('descartes-jobs.txt','w')
file1.write('')
file1.close()
file1=open('descartes-jobs.txt','a+')
print('\nScraping jobs at descartes')
file.write("\n\n\t\t\t\t\t DESCARTES JOBS\n\n")
file1.write("\n\n\t\t\t\t\t DESCARTES JOBS\n\n")
url  = 'https://jobs.lever.co/descarteslabs.com/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")
jobs = bs.find_all('a',{"class":"posting-title"})

for job in jobs:
    link = job['href']
    title = job.find('h5').get_text()
    location = job.find('span',{"class":"sort-by-location posting-category small-category-label"}).get_text()
    positionCategory = job.find("span",{"class":"sort-by-team posting-category small-category-label"}).get_text()
    commitment = job.find("span",{"class":"sort-by-commitment posting-category small-category-label"}).get_text()

    file.write("Title: "+title+"\n")
    file.write("Location: "+location+"\n")
    file.write("Category: "+ positionCategory+"\n")
    file.write("Commitment: "+commitment+"\n")
    file.write("Description:\n")
    file1.write("Title: "+title+"\n")
    file1.write("Location: "+location+"\n")
    file1.write("Category: "+ positionCategory+"\n")
    file1.write("Commitment: "+commitment+"\n")
    file1.write("Description:\n")
    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    entities = bs1.find_all('div',{'class':'section page-centered'})
    try:
        headPara = entities[0].find('span').get_text()
        file.write("\t"+headPara+"\n")
        file1.write("\t"+headPara+"\n")
        del entities[0]
        for entity in entities:
            heading = entity.find('h3').get_text()
            listItems = entity.find_all('li')
            file.write("\n\t"+heading+"\n")
            file1.write("\n\t"+heading+"\n")
            for item in listItems:
                file.write("\t\t->"+item.get_text()+"\n")
                file1.write("\t\t->"+item.get_text()+"\n")
    except:
        file.write("\t\tnone")
        file1.write("\t\tnone")

    file.write("\n\n\n\n")
    file1.write("\n\n\n\n")
print("Descartes jobs scraped successfully")
file1.close()


# scraping for mesosphere jobs
file1 = open('mesosphere-jobs.txt','w')
file1.write('')
file1.close()
file1=open('mesosphere-jobs.txt','a+')
print("\nScraping for mesosphere jobs")
file.write("\n\n\t\t\t\t\t MESOSPHERE JOBS\n\n")
file1.write("\n\n\t\t\t\t\t MESOSPHERE JOBS\n\n")
url  = 'https://mesosphere.com/careers/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")
jobs = bs.find_all('div',{'class':'careers-view__jobs-item'})

for job in jobs:
    link = job.find('a')['href']
    title = job.find('span',{'class':'careers-view__job-item-title'}).get_text()
    location = job.find('span',{'class':'careers-view__job-item-location text-color-gray-light small flush-bottom'}).get_text()
    title = title.split('-')
    # print(link)
    if(len(title)>1):
        file.write("Title: "+title[0]+"\n")
        file.write("Speciality/Area: "+title[1]+"\n")
        file1.write("Title: "+title[0]+"\n")
        file1.write("Speciality/Area: "+title[1]+"\n")
    else:
        file.write("Title: "+title[0]+"\n")
        file1.write("Title: "+title[0]+"\n")
    file.write("Location: "+location+"\n")
    file.write("Description: \n")
    file1.write("Location: "+location+"\n")
    file1.write("Description: \n")

    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    container = bs1.find('div',{'id':'content'})
    entities = container.find_all('span',{'style':"font-weight: 400;"})
    for entity in entities:
        file.write("\t\t"+entity.get_text()+"\n")
        file1.write("\t\t"+entity.get_text()+"\n")
        # print('done')
    file.write("\n\n")
    file1.write("\n\n")
print("mesosphere jobs scraped succesfully")
file1.close()


# scraping for rocketlabusa jobs
file1 = open('rocketlabusa-jobs.txt','w')
file1.write('')
file1.close()
file1=open('rocketlabusa-jobs.txt','a+')
print("\nScraping for rocketlabusa jobs")
url  = 'https://www.rocketlabusa.com/careers/positions/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"lxml")

jobs = bs.find_all('a',{'class':'job'})
# print(jobs)

file.write("\n\n\t\t\t ROCKETLABUSA JOBS\n\n")
file1.write("\n\n\t\t\t ROCKETLABUSA JOBS\n\n")
for job in jobs:
    link = job['href']
    link = "https://www.rocketlabusa.com"+link
    title = job.find('h3').get_text()
    location = job.find('h5').get_text()

    file.write('Title: '+title+"\n")
    file.write('Location: '+location+"\n")
    file.write('Description: \n')
    file1.write('Title: '+title+"\n")
    file1.write('Location: '+location+"\n")
    file1.write('Description: \n')
    # print(link)
    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    text = bs1.find('div',{'class':'job__info-subtitle'}).get_text()
    file.write("\t\t"+text+"\n\n\n")
    file1.write("\t\t"+text+"\n\n\n")
print("rocketlabusa jobs scraped succesfully")
file1.close()


# scraping for checkr jobs
file1 = open('checkr-jobs.txt','w')
file1.write('')
file1.close()
file1=open('checkr-jobs.txt','a+')
print("\nscraping for checkr jobs")
url  = 'https://checkr.com/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('a',{'class':'career question kitchensink'})
file.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
file1.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
for job in jobs:
    title = job.find('span').get_text()
    file.write("Title: "+title+"\n")
    file1.write("Title: "+title+"\n")
file.write("\n\n")
file1.write("\n\n")
print("checkr jobs scraped succesfully")



# scraping for interana jobs
file1 = open('interana-jobs.txt','w')
file1.write('')
file1.close()
file1=open('interana-jobs.txt','a+')
print("\nscraping for interana jobs")
url  = 'https://boards.greenhouse.io/interana'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'opening'})
# print(jobs)
file.write("\n\n\t\t\t\t\t INTERANA JOBS\n\n")
file1.write("\n\n\t\t\t\t\t INTERANA JOBS\n\n")
for job in jobs:
    link = job.find('a')['href']
    link = "https://boards.greenhouse.io"+link
    title = job.find('a').get_text()
    location = job.find('span').get_text()
    file.write("Title: "+title+"\n")
    file.write("Location: "+location+"\n\n")
    file.write("Description: \n")
    file1.write("Title: "+title+"\n")
    file1.write("Location: "+location+"\n\n")
    file1.write("Description: \n")

    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'id':'content'}).get_text()
    containers = bs1.find_all('div',{'class':'section page-centered'})
    if(len(containers)>0):
        for container in containers:
            file.write("\t\t"+container.get_text()+"\n")
            file1.write("\t\t"+container.get_text()+"\n")
    else:
        file.write("\t\t"+content+"\n")
        file1.write("\t\t"+content+"\n")
    file.write("\n\n---------------------------\n")
    file1.write("\n\n---------------------------\n")
file.write("\n\n")
file1.write("\n\n")

print("interana jobs scraped successfully")
file1.close()
file.close()
