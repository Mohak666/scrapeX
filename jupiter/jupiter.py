############this script doesn't work###########
# scraping for jupiter jobs
print('\nscraping jobs at jupiter')
open('jupiter-jobs.txt','w').close()
file1=open('jupiter-jobs.txt','a+')
file1.write("\n\n\t\t\t\t\t jupiter JOBS\n\n")
file.write("\n\n\t\t\t\t\t jupiter JOBS\n\n")
url  = 'https://jobs.lever.co/jupiterintel'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")
jobs = bs.find_all('a',{"class":"posting-title"})
print(len(jobs))
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

        for entity in content:
            try:
                heading = entity.find('h3').get_text()
                text = entity.find('ul').get_text()
                file.write("\n"+heading+"\n"+text+"\n\n")
                file1.write("\n"+heading+"\n"+text+"\n\n")
            except:
                file1.write(entity.get_text()+"\n")
                file.write(entity.get_text()+"\n")
        file.write("\n-----------------\n")
        file1.write("\n-----------------\n")
    except:
        pass
file1.close()
print("jupiter jobs scraped successfully")
