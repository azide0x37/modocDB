#modocDB/scraper.py
"""
Scrapes the Missouri Department of Corrections 
Offender web search site for offender data.

Stores in MongoDB collection
"""
#import lxml #TODO: implement this to speed up parsing
from pymongo import MongoClient

import os
import psycopg2
import urlparse
import requests
from bs4 import BeautifulSoup

class docScraper:
    def __init__(self, url = "https://web.mo.gov/doc/offSearchWeb/searchOffender.do", _offenders = 1050000):
        self._url = url
        self._offenders = _offenders
        urlparse.uses_netloc.append("postgres")
        url = urlparse.urlparse(os.environ["DATABASE_URL"])

        self._conn = psycopg2.connect(
                database = url.path[1:],
                user = url.username,
                password = url.password,
                host = url.hostname,
                port = url.port
        )

    def _parse(self, _rawHTML):
        #beautiful soup parsing
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
                
            return _data

        except(AttributeError):
            return False
    
    def pull(self):
        dataset = (self._parse(requests.get(self._url + "?docId=" + str(docId)).text) for docId in xrange(1000000, self._offenders))
        
        for x in dataset:
            val = dataset.next()
            if val:
                self._db_offenders.insert_one(val)
                print "inserted record"
                print [x for x in self._db_offenders.find()]      

dataSet = docScraper()
dataSet.pull()
