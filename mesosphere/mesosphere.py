import requests
import bs4

url  = 'https://mesosphere.com/careers/'
html = requests.get(url)

bs = bs4.BeautifulSoup(html.text,"html.parser")

jobs = bs.find_all('div',{'class':'careers-view__jobs-item'})

file = open("mesosphere-jobs.txt",'a+')
# print(jobs[0])
for job in jobs:
    link = job.find('a')['href']
    title = job.find('span',{'class':'careers-view__job-item-title'}).get_text()
    location = job.find('span',{'class':'careers-view__job-item-location text-color-gray-light small flush-bottom'}).get_text()
    title = title.split('-')
    # print(link)
    if(len(title)>1):
        file.write("Title: "+title[0]+"\n")
        file.write("Speciality/Area: "+title[1]+"\n")
    else:
        file.write("Title: "+title[0]+"\n")
    file.write("Location: "+location+"\n")
    file.write("Description: \n")

    descriptionURL = link;
    descriptionHTML = requests.get(descriptionURL)
    bs1 = bs4.BeautifulSoup(descriptionHTML.text,"html.parser")
    container = bs1.find('div',{'id':'content'})
    entities = container.find_all('span',{'style':"font-weight: 400;"})
    for entity in entities:
        file.write("\t\t"+entity.get_text()+"\n")
        # print('done')
    file.write("\n\n")
file.close()

# <span style="font-weight: 400;"> and other open source projects. Our engineers take pride in their craft and ship code that is well engineered and tested.</span>
# <div class="careers-view__jobs-item" data-id="1494701" data-department="[913]" data-location="[870]"> <a href="https://boards.greenhouse.io/mesosphere/jobs/1494701?gh_jid=1494701" class="careers-view__job-anchor-row" target="_blank"> <div class="careers-view__job-item-info"> <span class="careers-view__job-item-title">Engineering Manager - Cluster Ops (Hamburg)</span> <span class="careers-view__job-item-location text-color-gray-light small flush-bottom"> Hamburg </span> </div> <div class="hidden-mini-down careers-view__job-item-action"> <span class="text-link text-link--arrow text-link--arrow-right"> View Details <svg class="icon icon-mini icon-purple" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 492.004 492.004"> <path d="M484.14 226.886L306.46 49.202c-5.072-5.072-11.832-7.856-19.04-7.856-7.216 0-13.972 2.788-19.044 7.856l-16.132 16.136c-5.068 5.064-7.86 11.828-7.86 19.04 0 7.208 2.792 14.2 7.86 19.264L355.9 207.526H26.58C11.732 207.526 0 219.15 0 234.002v22.812c0 14.852 11.732 27.648 26.58 27.648h330.496L252.248 388.926c-5.068 5.072-7.86 11.652-7.86 18.864 0 7.204 2.792 13.88 7.86 18.948l16.132 16.084c5.072 5.072 11.828 7.836 19.044 7.836 7.208 0 13.968-2.8 19.04-7.872l177.68-177.68c5.084-5.088 7.88-11.88 7.86-19.1.016-7.244-2.776-14.04-7.864-19.12z"></path> </svg> </span> </div> </a> </div>
