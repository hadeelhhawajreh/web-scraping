import requests
import pprint
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/History_of_Jordan'
def get_citations_needed_count(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    return len(get_citations_needed_report(url))

final_res=[]
def get_citations_needed_report(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    word='citation needed'
    res=[]

    for i in soup.select('p'):
        ele=i.get_text()
        
        if word in ele:
            print(' \n ********* \n ')
            print(ele[0:ele.find('needed')+len('needed ')])
            res.append(ele)
        dic={
        'citation':ele
    }
    final_res.append(dic)
    return res


print(f'\n ********* \n \n The length is : {get_citations_needed_count(URL)}\n')

# print(get_citations_needed_report(URL))
import json
jsonObj=json.dumps(final_res,indent=4)
with open('data.json','w') as file:
    file.write(jsonObj)
