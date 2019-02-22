import requests
import bs4
from urllib.request import Request, urlopen
import xlsxwriter as xl

open('all-jobs.txt','w').close()
file = open('all-jobs.txt','a+')
workbook = xl.Workbook('all-jobs.xlsx')

count = 0

def writeToExcel(name,jobs,labels):

    worksheet = workbook.add_worksheet(name)
    row = 0
    col = 0
    for x in labels:
        worksheet.write(row,col,x.upper())
        col+=1
    row+=1
    for job in jobs:
        col = 0
        for item in job:
            worksheet.write(row,col,item)
            col+=1
        row+=1


def lever(name,url):
    global count
    print('\nscraping jobs at '+name)
    filename = name+'-jobs.txt'
    open(filename,'w').close()
    file1=open(filename,'a+')
    file1.write("\n\n\t\t\t\t\t "+name.upper()+" JOBS\n\n")
    file.write("\n\n\t\t\t\t\t "+name.upper()+" JOBS\n\n")

    html = requests.get(url)

    bs = bs4.BeautifulSoup(html.text,"html.parser")
    jobs = bs.find_all('a',{"class":"posting-title"})
    xlJobs = []
    labels = ['Title','Location','positionCategory','Commitment','Description']
    for job in jobs:
        try:
            link = job['href']
            title = job.find('h5').get_text()
            location = job.find('span',{"class":"sort-by-location posting-category small-category-label"}).get_text()
            positionCategory = job.find("span",{"class":"sort-by-team posting-category small-category-label"}).get_text()
            commitment = job.find("span",{"class":"sort-by-commitment posting-category small-category-label"}).get_text()

            descriptionURL = link;
            descriptionHTML = requests.get(descriptionURL)
            bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
            content = bs1.find_all('div',{'class':'section page-centered'})
            file1.write("Title: "+title+"\nLocation: "+location+"\nCategory: "+ positionCategory+"\nCommitment: "+commitment+"\n")
            file.write("Title: "+title+"\nLocation: "+location+"\nCategory: "+ positionCategory+"\nCommitment: "+commitment+"\n")
            file1.write("Description:\n")
            file.write("Description:\n")
            description = ''
            for entity in content:
                try:
                    heading = entity.find('h3').get_text()
                    text = entity.find('ul').get_text()
                    file.write("\n"+heading+"\n"+text+"\n\n")
                    file1.write("\n"+heading+"\n"+text+"\n\n")
                    description = description + heading +'\n'+ text +'\n'
                except:
                    file1.write(entity.get_text()+"\n")
                    file.write(entity.get_text()+"\n")
                    description+= entity.getText()
            file.write("\n-----------------\n")
            file1.write("\n-----------------\n")
            # print(len(description))
            # print(description)
            # print('----------------------\n')
            description= description.replace('\r', '').replace('\n', '')
            xlJobs.append([title,location,positionCategory,commitment,description])
        except:
            pass
    file1.close()
    writeToExcel(name,xlJobs,labels)
    count+=1
    print(name+" jobs scraped successfully")



def greenhouse(name,site):
    global count
    print("\nscraping jobs at "+name)

    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    bs = bs4.BeautifulSoup(page,"html.parser")

    jobs = bs.find_all('div',{'class':'opening'})
    filename = name+'-jobs.txt'
    open(filename,'w').close()
    file1 = open(filename,'a+')
    file.write("\n\n\t\t\t "+name+" JOBS\n\n")
    file1.write("\n\n\t\t\t "+name+" JOBS\n\n")

    labels = ['Title','Location','Description']
    xlJobs = []
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
        description= description.replace('\r', '').replace('\n', '')
        xlJobs.append([title,location,description.strip('\n')])
    file1.close()
    count+=1
    writeToExcel(name,xlJobs,labels)
    print(name+' jobs scraped succesfully')



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
labels = ['Title','Location','Description']
xlJobs = []
for job in jobs:
    title = job.find('h2').get_text()
    location = job.find('h4').get_text().split(':')[1]
    description = job.find('p').getText()
    file.write("Title:"+ title +"\n"+"Location:"+ location +"\n"+"Description:"+ description +"\n\n")
    file1.write("Title:"+ title +"\n"+"Location:"+ location +"\n"+"Description:"+ description +"\n\n")
    description= description.replace('\r', '').replace('\n', '')
    xlJobs.append([title,location,description])
file1.close()
writeToExcel('aporeto',xlJobs,labels)
count+= 1
print("Aporeto jobs scraped successfully")


########### ALL LEVER JOBS HERE ###############
# scraping for descartes jobs
lever('descartes','https://jobs.lever.co/descarteslabs.com/')

# scraping jobs at enlitic
lever('enlitic','https://jobs.lever.co/enlitic/')

# scraping for primer jobs
lever('primer','https://jobs.lever.co/pri.ai')

# scraping for alation jobs
lever('alation','https://jobs.lever.co/alation')

# scraping for capeanalytics jobs
lever('capeanalytics','https://jobs.lever.co/capeanalytics')


# scraping for diassess jobs
lever('diassess','https://jobs.lever.co/diassess')


# scraping for jupiter jobs
lever('jupiter','https://jobs.lever.co/jupiterintel')


# scraping for kindred jobs
lever('kindred','https://jobs.lever.co/kindred')

# scraping for reachlabs jobs
lever('reachlabs','https://jobs.lever.co/reachlabs')







############### ALL GREENHOUSE JOBS HERE ##################

# scraping for interana jobs
greenhouse('interana','https://boards.greenhouse.io/interana')

# scraping jobs at haveninc
greenhouse('haven','https://boards.greenhouse.io/haven')

#scraping jobs at desktopmetal
greenhouse('desktopmetal','https://boards.greenhouse.io/desktopmetal')

#scraping jobs at gradle
greenhouse('gradle','https://boards.greenhouse.io/gradle')

#scraping jobs at memsql
greenhouse('memsql','https://boards.greenhouse.io/memsql')

#scraping jobs at tigergraph
greenhouse('tigergraph','https://boards.greenhouse.io/tigergraph')




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

labels = ['Title','Location','Description']
xlJobs = []

for job in jobs:
    try:
        link = job.find('a')['href']
        title = job.find('span',{'class':'careers-view__job-item-title'}).get_text()
        location = job.find('span',{'class':'careers-view__job-item-location text-color-gray-light small flush-bottom'}).get_text()
        item = [title,location]
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
        description = ''
        for entity in entities:
            file.write("\t\t"+entity.get_text()+"\n")
            file1.write("\t\t"+entity.get_text()+"\n")
            description= description + entity.get_text()
        # print(description+"\n\n----------------------------------------\n")
        description= description.replace('\r', '').replace('\n', '')
        item.append(description)
        # print(item)
        xlJobs.append(item)
        file.write("\n\n")
        file1.write("\n\n")
    except:
        pass
# print(xlJobs)
writeToExcel('mesosphere',xlJobs,labels)
file1.close()
count+=1
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
labels = ['Title','Location','Description']
xlJobs = []
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
    description = bs1.find('div',{'class':'job__info-subtitle'}).get_text()
    file.write("\t\t"+description+"\n\n\n")
    file1.write("\t\t"+description+"\n\n\n")
    description= description.replace('\r', '').replace('\n', '')
    xlJobs.append([title,location,description])
file1.close()
writeToExcel('rocketlabusa',xlJobs,labels)
count+=1
print("rocketlabusa jobs scraped succesfully")



#scraping jobs at vicariuos
print('\nscraping jobs at vicariuos')

site= "https://www.vicarious.com/careers/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")
jobs = bs.find_all('div',{'class':'job-posting'})

open('vicarious-jobs.txt','w').close()
file1 = open('vicarious-jobs.txt','a+')
file1.write("\n\n\t\t\t VICARIOUS JOBS\n\n")
file.write("\n\n\t\t\t VICARIOUS JOBS\n\n")
labels = ['Title','Description']
xlJobs = []
for job in jobs:
    title = job.find('div',{'class':'job-title'}).get_text()
    title = title.strip('\n').lstrip('\t').strip('\n')

    # print(title)
    description = job.find('div',{'class':'job-description'}).get_text()

    file.write('Title: '+title+"\nDescription: "+description)
    file1.write('Title: '+title+"\nDescription: "+description)
    file.write("\n---------------------------\n")
    file1.write("\n---------------------------\n")
    description= description.replace('\r', '').replace('\n', '')
    xlJobs.append([title,description])
file1.close()
writeToExcel('vicarious',xlJobs,labels)
count+=1
print("vicarious jobs scraped succesfully")





print('Total: ',count)
file.close()
workbook.close()
