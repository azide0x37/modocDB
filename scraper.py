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
		
	def pull():
		dataSet = (requests.post(self._url + "docId=", docId for docId in xrange(self._offenders))
		
		try:
			#TODO: check if already in dataset and discard
			for n in xrange(self._offenders):
				self._db_offenders.write = mongoDBwriter.row_add(BeautifulSoup.parse(dataSet.next()))

dataSet = docScraper()
dataSet.pull()
