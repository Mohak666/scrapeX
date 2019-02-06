import requests
import bs4

url  = 'https://embarktrucks.com/jobs.html'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")
open('embark-jobs.txt','w').close()
file =  open('embark-jobs.txt','a+')
jobs = bs.find_all('div',{'class':'posting'})
print(len(jobs))

for job in jobs:
    item = job.find('a')
    link = item['href']
    title = job.find('h5').get_text()
    commitment = job.find('span',{'class':'sort-by-commitment posting-category small-category-label'}).get_text()
    department = job.find('span',{'class':'sort-by-team posting-category small-category-label'}).get_text()
    location = job.find('span',{'class':'sort-by-location posting-category small-category-label'}).get_text()
    descriptionHTML = requests.get(link)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    content = bs1.find('div',{'class':'section-wrapper page-full-width'})

    file.write("Title: "+title+"\nLocation: "+location+"\nDepartment: "+department+"\nCommitment: "+commitment+"\nDescription: \n")
    items = content.find_all('div',{'class':'section page-centered'})

    for item in items:
        try:
            heading = item.find('h3').get_text()
            text = item.find('ul').get_text()
            file.write(heading+"\n"+text+"\n\n")
        except:
            file.write(item.get_text())
    file.write("\n-------------------\n")
file.close()
