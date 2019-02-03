import requests
import bs4

# scraping jobs at enlitic
print("\nscraping jobs at enlitic")

url  = 'https://jobs.lever.co/enlitic/'
html = requests.get(url)
bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'posting'})
open('enlitic-jobs.txt','w').close()
file1 = open('enlitic-jobs.txt','a+')
for job in jobs:
    try:
        title = job.find('h5').get_text()
        commitment = job.find('span',{'class':'sort-by-commitment posting-category small-category-label'}).get_text()
        department = job.find('span',{'class':'sort-by-team posting-category small-category-label'}).get_text()
        location = job.find('span',{'class':'sort-by-location posting-category small-category-label'}).get_text()
    except:
        pass
    file1.write("Title: "+title+"\nLocation: "+location+"\nDepartment: "+department+"\nCommitment: "+commitment+"\n\n")
    title=location=commitment=department=''
print('enlitic jobs scraped succesfully')
file1.close()
