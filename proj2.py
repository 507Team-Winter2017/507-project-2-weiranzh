#proj2.py
import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

count=0
for story_heading in soup.find_all(class_="story-heading"):
    try:
        if story_heading.a:
            print(story_heading.a.content.replace("\n", " ").strip())
            count+=1
        else:
            print(story_heading.contents[0].strip())
            count+=1
        if count==10:
            break
    except:
        pass

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here

base_url = 'http://www.michigandaily.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

for item in soup.find_all('div',attrs={'class':'view-most-read'}):
    print (item.text)

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here

base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,"html.parser")

for image in soup.find_all('img'):
    if image.get('alt'):
        print (image.get('alt',''))
    else:
        print ('No alternative text provided!')

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here

base_url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'

pagenum = 0
count = 1
while pagenum<7:
    r = requests.get(base_url,headers={'User-Agent':'SI_CLASS'})
    soup = BeautifulSoup(r.text,"html.parser")
    for item in soup.find_all('div',attrs={'class':'field-name-contact-details'}):
        # print (item.a.get('href'))

        result = requests.get('https://www.si.umich.edu'+str(item.a.get('href')),headers={'User-Agent':'SI_CLASS'})
        subsoup = BeautifulSoup(result.text,"html.parser")
        for divs in subsoup.find_all('div',attrs={'class':'field-name-field-person-email'}):
            for div in divs.find_all(class_="field-item"):
                print (str(count)+" "+(div.a.text))
        count +=1
    pagenum+=1
    base_url+='&page='+str(pagenum)
