import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/tags/python-requests'
#url2 = 'https://stackoverflow.com/questions/tagged/python-requests?tab=newest&page=2&pagesize=15'

#response = requests.get(url)

#parser = BeautifulSoup(response.text, 'html.parser')
#questinon = parser.find_all("div", {"class":"s-post-summary"})

for i in range(1,11):
    url2 = 'https://stackoverflow.com/questions/tagged/python-requests?tab=newest&page='+str(i)+'&pagesize=15'

    response = requests.get(url2)
    parser = BeautifulSoup(response.text, 'html.parser')
    questinon = parser.find_all("div", {"class": "s-post-summary"})

    print("Content Count " + str(i))

    for q in questinon:
        print("****************************************")
        #print(q)
        title = q.find("h3", {"class":"s-post-summary--content-title"})
        print(title.text.strip())
        content = q.find("div", {"class":"s-post-summary--content-excerpt"})
        print(content.text.strip())
        time = q.find('span', {"class": "relativetime"})
        print(time['title'])
        print("****************************************")


