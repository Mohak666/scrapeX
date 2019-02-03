import bs4
from urllib.request import Request, urlopen

site= "https://kurbo.com/careers/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
bs = bs4.BeautifulSoup(page,"html.parser")
open('kurbo-jobs.txt','w').close()
file = open('kurbo-jobs.txt','a+')
file.write("\n\n\t\t\t KURBO JOBS\n\n")
# print(bd)
descriptions = bs.find_all('div',{'class':'career-content'})
titles = bs.find_all('button',{'class','button-primary'})
for i in range(len(titles)):
    file.write("Title: "+titles[i].get_text()+"\nDescription: \t"+descriptions[i].get_text())
    file.write("\n----------------------------\n")
file.close()
