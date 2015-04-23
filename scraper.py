#modocDB/scraper.py
"""
Scrapes the Missouri Department of Corrections 
Offender web search site for offender data.

Stores in MongoDB collection
"""
#import lxml #TODO: implement this to speed up parsing
import os
import psycopg2
import urlparse
import requests
from bs4 import BeautifulSoup

class docScraper:
    def __init__(self, offenders = 1250000):
        self._url = "https://web.mo.gov/doc/offSearchWeb/searchOffender.do"
        self._offenders = offenders
        urlparse.uses_netloc.append("postgres")
        conn_url = urlparse.urlparse(os.environ["HEROKU_POSTGRESQL_GRAY_URL"])
        #TODO: Set DATABASE_URL on nitrowagon and neodymium

        self._conn = psycopg2.connect(
                database = conn_url.path[1:],
                user = conn_url.username,
                password = conn_url.password,
                host = conn_url.hostname,
                port = conn_url.port
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
	
    def get(self):
        return self._update((self._parse(requests.get(self._url + "?docId=" + str(docId)).text) for docId in xrange(1250050, self._offenders)))
        #return link to database
    
    def _update(self, dataset):
		return dataset

		"""
		#TODO: Change this over to psycopg2 insertions
        #dataset is expected as a generator object
        for _ in dataset:
            val = dataset.next()
            #TODO: Check if in database; if not, insert, if so, check if different, if so update
            if val:
                self._db_offenders.insert_one(val)
                print "inserted record"
                print [_ for _ in self._db_offenders.find()]
		"""
dataSet = docScraper()
dataSet.get()
