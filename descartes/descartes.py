import requests
import bs4

url  = 'https://jobs.lever.co/descarteslabs.com/'
html = requests.get(url)



bs = bs4.BeautifulSoup(html.text,"html.parser")


jobs = bs.find_all('a',{"class":"posting-title"})
file = open("descartes-jobs.txt","w")
file.write('')
file.close()
file = open("descates-jobs.txt","a+")
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
    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    entities = bs1.find_all('div',{'class':'section page-centered'})
    try:
        headPara = entities[0].find('span').get_text()
        file.write("\t"+headPara+"\n")
        del entities[0]
        for entity in entities:
            heading = entity.find('h3').get_text()
            listItems = entity.find_all('li')
            file.write("\n\t"+heading+"\n")
            for item in listItems:
                file.write("\t\t->"+item.get_text()+"\n")
    except:
        # headPara = entities[0].find('b')
        # file.write("\t"+headPara+"\n")
        # del entities[0]
        # for entity in entities:
        #     heading = entity.find('h3').get_text()
        #     listItems = entity.find_all('li')
        #     file.write("\n\t"+heading+"\n")
        #     for item in listItems:
        #         file.write("\t\t->"+item.get_text()+"\n")
        file.write("\t\tnone")

    file.write("\n\n\n\n")
file.close()
