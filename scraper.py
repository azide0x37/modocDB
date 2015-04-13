#modocDB/scraper.py
#Scrapes the offender web search library for offender data
import csv
import lxml #use this to speed up parsing for large datasets
import pymongo 
import requests
import BeautifulSoup as bs4

class docScraper:
	def __init__(self, url = "", _offenders = 1300000):
		self._url = 
		self._offenders = _offenders
		self._client = pymongo.MongoClient("localhost", 27017)
		self._db_offenders = self._client.db_offenders
	
	def _parse(self):
		##beautiful soup parsing
	def pull(self):
		result = [self._db_offenders.insert_one(self._parse(requests.post(self._url + "docId=", docId)) for docId in xrange(self._offenders)]

dataSet = docScraper()
dataSet.pull()
