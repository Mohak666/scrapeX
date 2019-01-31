import requests
import bs4

url  = 'https://jobs.lever.co/descarteslabs.com/'
html = requests.get(url)

# handle = open("descartes.txt",'w')
# handle.write(html.text)
# handle.close()
# file = open("descartes.txt","r")
# html = file.read()
# file.close()

bs = bs4.BeautifulSoup(html.text,"html.parser")


jobs = bs.find_all('a',{"class":"posting-title"})

file = open("descates-jobs.txt","a+")
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
file.close()
