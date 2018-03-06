import requests
import lxml
from bs4 import BeautifulSoup

class MarineTraffic():
    def __init__(self):
        self.url = 'https://www.marinetraffic.com'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

    def Search(self, keyword):        
        myurl = '/en/ais/index/search/all/keyword:%s'%keyword.replace(' ', '%20')      
        res = self.Link2Results(myurl)       
        output = list(map(lambda x: (x[0], self.Link2Details(x[1], kind = x[0][1])), res))
        sum_output = '%s results found for keyword: %s'%(len(output), keyword)
        return sum_output, output

    def Link2Results(self, myurl):
        myurl = self.url + myurl
        response = requests.get(myurl, headers = self.headers)
        data = BeautifulSoup(response.content, 'lxml')

        search_result = data.find_all('table', {'class': 'table table-hover text-left'})[0]
        search_links = list(map(lambda x: x.get('href'), search_result.find_all('a', {'class': "search_index_link"})))
        temp = search_result.get_text().splitlines()
        temp = [x for x in temp if x!='']
        search_titles = []
        for i in range(3, len(temp)-2, 3):
            search_titles.append([temp[i].strip(), temp[i+1].strip(), temp[i+1].strip()])

        res = list(zip(search_titles, search_links))        
        next_page = data.find_all('span', {'class': 'next'})
        if next_page and next_page[0].find_all('a') and next_page[0].find_all('a')[0].get('href'):
            return res + self.Link2Results(next_page[0].find_all('a')[0].get('href'))
        else:
            return res
      
    def Link2Details(self, myurl, kind):        
        myurl = self.url + myurl
        response = requests.get(myurl, headers = self.headers)
        data = BeautifulSoup(response.content, 'lxml')
        
        if kind in ['Photographer']:
            return ['Photos Not Shown']
        elif kind in ['Station']:
            temp = data.find_all('div', {'class': "bg-info bg-light padding-10 radius-8 text-left"})
        elif kind in ['Vessel', 'Callsign', 'Light', 'Exname', 'IMO number', 'MMSI number', 'Port']:
            temp = data.find_all('div', {'class': 'bg-info bg-light padding-10 radius-4 text-left'})
        else:
            return ['Result Type Not Available']

        try:
            temp = temp[0].get_text(separator = '').splitlines()
            temp = [x for x in temp if x!='']
        except:
            return ['Information Not Available Now, Please Try Again']

        if kind == 'Port' and 'Show on Map' in temp:
            temp.remove('Show on Map')

        details = []
        for i in range(0, len(temp)-1, 2):
            details.append(temp[i] + temp[i+1])
        return details