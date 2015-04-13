#modocDB/scraper.py
"""
Scrapes the Missouri Department of Corrections 
Offender web search site for offender data.

Stores in MongoDB collection
"""
#import lxml #TODO: implement this to speed up parsing
#import pymongo #get this working
import requests
from bs4 import BeautifulSoup

class docScraper:
    def __init__(self, url = "https://web.mo.gov/doc/offSearchWeb/searchOffender.do", _offenders = 1230000):
        self._url = url
        self._offenders = _offenders
        #self._client = pymongo.MongoClient("localhost", 27017)
        #self._db_offenders = self._client.db_offenders

    def _parse(self, _rawHTML):
        ##beautiful soup parsing
        _souped = BeautifulSoup(_rawHTML)
        _table = _souped.find('table', { "class" : "displayTable" })
        try:
            _cols = _table.findAll('tr')
            _data = {}        
            for tr in _cols:
                td = tr.findAll('td')
                try:                
                    results = ["".join(_.find(text=True)).strip() for _ in td if _ != '']
                except(TypeError):
                    pass

                if (len(results) == 3):
                    results.pop(0)
                
                try:
                    _key, _value = results[0:2]
                    _data[_key] = _value
                except(ValueError):
                    pass
                
            print _data
                #_key = "".join(td.find(text=True))
                #_value = "".join(td.findNext(text=True))
                #_data[_key] = _value
        
        except(AttributeError):
            pass
    
    def pull(self):
        dataset = [self._parse(requests.get(self._url + "?docId=" + str(docId)).text) for docId in xrange(1229000, self._offenders)]
                  
         
dataSet = docScraper()
dataSet.pull()
