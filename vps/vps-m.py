import requests
import bs4

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
    file.write("Description: \n")
    file1.write("Description: \n")
    file.write("\t"+description+"\n")
    file1.write("\t"+description+"\n")
    file.write("\n---------------------\n")
    file1.write("\n---------------------\n")
file.write("\n\n")
file1.write("\n\n")

file1.close()
