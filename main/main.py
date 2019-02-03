import requests
import bs4
from urllib.request import Request, urlopen

open('all-jobs.txt','w').close()
file = open('all-jobs.txt','a+')

# scraping for Aporeto jobs
print("scraping jobs at aporeto")
open('aporeto-jobs.txt','w').close()
file1=open('aporeto-jobs.txt','a+')
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

    file.write("Title:"+ title +"\n"+"Location:"+ location +"\n"+"Description:"+ description +"\n\n")
    file1.write("Title:"+ title +"\n"+"Location:"+ location +"\n"+"Description:"+ description +"\n\n")
file1.close()
print("Aporeto jobs scraped successfully")



# scraping for descartes jobs
print('\nscraping jobs at descartes')
open('descartes-jobs.txt','w').close()
file1=open('descartes-jobs.txt','a+')
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
file1.close()
print("Descartes jobs scraped successfully")



# scraping for mesosphere jobs
print("\nscraping jobs at mesosphere")
open('mesosphere-jobs.txt','w').close()
file1=open('mesosphere-jobs.txt','a+')
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
        file.write("Title: "+title[0]+"\n"+"Speciality/Area: "+title[1]+"\n")
        file1.write("Title: "+title[0]+"\n"+"Speciality/Area: "+title[1]+"\n")
    else:
        file.write("Title: "+title[0]+"\n")
        file1.write("Title: "+title[0]+"\n")
    file.write("Location: "+location+"\n"+"Description: \n")
    file.write("Location: "+location+"\n"+"Description: \n")

    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    container = bs1.find('div',{'id':'content'})
    entities = container.find_all('span',{'style':"font-weight: 400;"})
    for entity in entities:
        file.write("\t\t"+entity.get_text()+"\n")
        file1.write("\t\t"+entity.get_text()+"\n")
        # print('done')
    file.write("\n\n")
    file1.write("\n\n")
file1.close()
print("mesosphere jobs scraped succesfully")



# scraping for rocketlabusa jobs
print("\nscraping jobs at rocketlabusa")
open('rocketlabusa-jobs.txt','w').close()
file1=open('rocketlabusa-jobs.txt','a+')
url  = 'https://www.rocketlabusa.com/careers/positions/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

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

file1.close()
print("rocketlabusa jobs scraped succesfully")



# scraping for checkr jobs
print("\nscraping jobs at checkr")
url  = 'https://checkr.com/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('a',{'class':'career question kitchensink'})
open("checkr-jobs.txt",'w').close()
file1 = open('checkr-jobs.txt','a+')
file1.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
file.write("\n\n\t\t\t\t\t CHECKR JOBS\n\n")
for job in jobs:
    link = job['href']
    title = job.find('span').get_text().strip('\n')
    file1.write("Title: "+title+"\n")
    file.write("Title: "+title+"\n")

    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'id':'content'}).get_text()
    location = bs1.find('div',{'class':'location'}).get_text()
    file1.write("Location: "+location+"\n")
    file1.write("Description: \n")
    file1.write(content)
    file1.write("\n---------------------\n")
    file.write("Location: "+location+"\n")
    file.write("Description: \n")
    file.write(content)
    file.write("\n---------------------\n")
file1.write("\n\n")
file.write("\n\n")
file1.close()
print("checkr jobs scraped succesfully")



# scraping for interana jobs
print("\nscraping jobs at interana")
open('interana-jobs.txt','w').close()
file1=open('interana-jobs.txt','a+')

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
    file.write("Title: "+title+"\n"+"Location: "+location+"\n\n"+"Description: \n")
    file1.write("Title: "+title+"\n"+"Location: "+location+"\n\n"+"Description: \n")

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

file1.close()
print("interana jobs scraped successfully")


#scraping jobs at virtualpowersystems
print('\nscraping jobs at virtualpowersystems')
url  = 'http://www.virtualpowersystems.com/jobs//'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

open("vps-jobs.txt",'w').close()
file1 = open('vps-jobs.txt','a+')
file1.write("\n\n\t\t\t\t\t VIRTUALPOERSYSTEMS JOBS\n\n")
file.write("\n\n\t\t\t\t\t VIRTUALPOERSYSTEMS JOBS\n\n")

jobs = bs.find_all('div',{'class':'job-info'})

for job in jobs:
    link = job.find('a')['href']
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")

    title = bs1.find('span',{'class':'job-title'}).get_text()
    type  = bs1.find('div',{'class':'job-type'}).get_text()
    location = bs1.find('div',{'class':'job-location'}).get_text()
    description = bs1.find('div',{'class':'et_pb_text_inner'}).get_text()
    file.write("Title: "+title+"\n"+"Type: "+type+"\n"+"Location: "+location+"\n")
    file1.write("Title: "+title+"\n"+"Type: "+type+"\n"+"Location: "+location+"\n")
    file.write("Description: \n\t"+description+"\n\n---------------------\n")
    file1.write("Description: \n\t"+description+"\n\n---------------------\n")
file.write("\n\n")
file1.write("\n\n")
file1.close()
print("virtualpowersystems jobs scraped successfully")


#scraping jobs at pluribusnetworks
print('\nscraping jobs at pluribusnetworks')

url  = 'https://www.pluribusnetworks.com/company/careers/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'career'})
file1 = open('pluribus-jobs.txt','a+')
file.write("\n\n\t\t\t\t\t PLURIBUSNETWORKS JOBS\n\n")
file1.write("\n\n\t\t\t\t\t PLURIBUSNETWORKS JOBS\n\n")
for job in jobs:
    item = job.find('a')
    link = item['href']
    title = item.get_text()
    location = job.find('strong',{'class':'career-location'}).get_text()
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'class':'career'}).get_text()
    content = content.split('|')
    content = content[1]

    file.write("Title: "+title+"\n"+"Location: "+location+"\n Description: \n")
    file1.write("Title: "+title+"\n"+"Location: "+location+"\n Description: \n")
    file.write("\t"+content+"\n------------------\n")
    file1.write("\t"+content+"\n------------------\n")
file1.close()
print('pluribusnetworks jobs scraped succesfully')

# scraping jobs at enlitic
print("\nscraping jobs at enlitic")

url  = 'https://jobs.lever.co/enlitic/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'posting'})
open('enlitic-jobs.txt','w').close()
file1 = open('enlitic-jobs.txt','a+')
file.write("\n\n\t\t\t ENLITIC JOBS \n\n")
file1.write("\n\n\t\t\t ENLITIC JOBS \n\n")
for job in jobs:
    # print(str(job)+"\n------------------\n")
    try:
        title = job.find('h5').get_text()
        commitment = job.find('span',{'class':'sort-by-commitment posting-category small-category-label'}).get_text()
        department = job.find('span',{'class':'sort-by-team posting-category small-category-label'}).get_text()
        location = job.find('span',{'class':'sort-by-location posting-category small-category-label'}).get_text()
    except:
        pass
    file.write("Title: "+title+"\nLocation: "+location+"\nDepartment: "+department+"\nCommitment: "+commitment+"\n\n")
    file1.write("Title: "+title+"\nLocation: "+location+"\nDepartment: "+department+"\nCommitment: "+commitment+"\n\n")
    title=location=commitment=department=''
print('enlitic jobs scraped succesfully')
file1.close()



# scraping for sentinelone jobs
print('\nscraping for sentinelone jobs')
url  = 'https://jobs.jobvite.com/sentinelone/jobs'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('td',{'class':'jv-job-list-name'})

open("sentinelone-jobs.txt",'w').close()
file1 = open("sentinelone-jobs.txt",'a+')
file.write("\n\n\t\t\t SENTINELONE JOBS \n\n")
file1.write("\n\n\t\t\t SENTINELONE JOBS \n\n")
for job in jobs:
    item = job.find('a')
    link = "https://jobs.jobvite.com"+item['href']
    title = item.get_text()
    # print(title,link)
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    department = bs1.find('p',{'class':'jv-job-detail-meta'}).get_text().strip(' ')
    location = bs1.find('span',{'class':'jv-inline-separator'}).get_text().strip('\n')
    description = bs1.find('div',{'class':'jv-job-detail-description'}).get_text()

    file.write("Title: +"+title+"\nDetails: "+department+"\n"+description)
    file1.write("Title: +"+title+"\nDetails: "+department+"\n"+description)
    file.write("\n----------------------\n")
    file1.write("\n----------------------\n")
file1.close()
print('sentinelone jobs scraped succesfully')



# scraping jobs at kurbo
print('\nscraping jobs at kurbo')
site= "https://kurbo.com/careers/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")
open('kurbo-jobs.txt','w').close()
file1 = open('kurbo-jobs.txt','a+')
file.write("\n\n\t\t\t KURBO JOBS\n\n")
file1.write("\n\n\t\t\t KURBO JOBS\n\n")
# print(bd)
descriptions = bs.find_all('div',{'class':'career-content'})
titles = bs.find_all('button',{'class','button-primary'})
for i in range(len(titles)):
    file.write("Title: "+titles[i].get_text()+"\nDescription: \t"+descriptions[i].get_text())
    file1.write("Title: "+titles[i].get_text()+"\nDescription: \t"+descriptions[i].get_text())
    file.write("\n----------------------------\n")
    file1.write("\n----------------------------\n")
file1.close()
print('kurbo jobs scraped succesfully')

# scraping jobs at haveninc
print("\nscraping jobs at haven")

site= "https://boards.greenhouse.io/haven"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")

jobs = bs.find_all('div',{'class':'opening'})
open('haven-jobs.txt','w').close()
file1 = open('haven-jobs.txt','a+')
file.write("\n\n\t\t\t HAVEN JOBS\n\n")
file1.write("\n\n\t\t\t HAVEN JOBS\n\n")
for job in jobs:
    item = job.find('a')
    link = "https://boards.greenhouse.io"+item['href']
    title = item.get_text()
    location = job.find('span').get_text()

    req1 = Request(link,headers=hdr)
    descriptionHTML = urlopen(req1)
    bs1 = bs4.BeautifulSoup(descriptionHTML,"html.parser")
    description = bs1.find('div',{'id':'content'}).get_text()
    file.write('Title: '+title+"\nLocation: "+location+"\nDescription: \n\t"+description)
    file1.write('Title: '+title+"\nLocation: "+location+"\nDescription: \n\t"+description)
    file.write('\n-----------------------------\n')
    file1.write('\n-----------------------------\n')
file1.close()
print('haven jobs scraped succesfully')

file.close()
