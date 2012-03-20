"""
	Parameters:
		* URLs
		* IP Addresses
		* # of clicks per session
		* Date range
		* Browsers list
"""
import random
import math

class LogRecord:
	def __init__(self, url, ip, timestamp, browser):
		self.url = url
		self.ip = ip
		self.timestamp = timestamp
		self.browser = browser
	
	def __str__(self):
		rec = self.ip + '\t' + self.url + '\t' +  self.timestamp + '\t' + self.browser
		return rec

	def __repr__(self):
		return __str__(self)

class GenerateLogs:
	def __init__(self):
		self.startDate = ''
		self.endDate = ''

	def setupCustomParams(self, urls, ips, clicks_per_session, startDate, endDate, browsers):
		self.urls = urls
		self.ips = ips
		self.clicks_per_session = clicks_per_session
		self.startDate = startDate
		self.endDate = endDate
		self.browsers = browsers
	
	def setupDefaultURLs(self):
		urls = ['urlA', 'urlB', 'urlC']
		self.urls = urls

	def setupDefaultIPs(self):
		ips = ['ipA', 'ipB', 'ipC'] 
		self.ips = ips

	def setupDefaultBrowsers(self):
		browsers = ['Chrome', 'Safari', 'Internet_Explorer', '']
		self.browsers = browsers;

	def setupDefaults(self):
		clicks_per_session = 5
		self.clicks_per_session = clicks_per_session 
		self.setupDefaultURLs()
		self.setupDefaultBrowsers()
		self.setupDefaultIPs()

	def generateRandomIP(self):
		import random as r
		index = r.random()*len(self.ips)
		return self.ips[int(math.floor(index))]

	def generateRandomURL(self):
		import random as r
		index = r.random()*len(self.urls)
		return self.urls[int(math.floor(index))]

	def generateRandomBrowser(self):
		import random as r
		index = r.random()*len(self.browsers)
		return self.browsers[int(math.floor(index))]
	'''
		Ignores clicks per session
		Takes into account URLs, Browser list, IP addresses
		Creates a set of records whose timestamps fall within the date range
		Example date string param: 20120124 ( YYYYMMDD )
		Returns: List of LogRecord items
	'''
	def generateRandomLogsForDateRange(self, startDate, endDate):
		# Logic - Start with the 'start' time, and create records at 'rand()*5 seconds' intervals.
		# 				Increment the time by 5 seconds while looping through and creating records
		import datetime as dt
		records = []
		baseTime = dt.datetime.strptime(startDate, '%Y%m%d')
		endTime = dt.datetime.strptime(endDate, '%Y%m%d')
		counterTime = baseTime
		while True:
			recordTime = counterTime + dt.timedelta(seconds=random.random()*5)
			# Create a record with random url and ip
			record = LogRecord(self.generateRandomURL(), self.generateRandomIP(), recordTime.strftime('%Y:%m:%d:%M:%S'), self.generateRandomBrowser())
			records.append(record)
			counterTime = counterTime + dt.timedelta(seconds=5)
			if(counterTime > endTime):
				break
		return records

	def generateRandomLogs(num_records):
		import random
		for i in range(1, num_records):
			rand = random.random()
			
class RecordsFileWriter:
	def __init__(self, records, file_name):
		self.records = records
		self.file_name = file_name

	def writeToFile(self):
		file_path = 'generatedLogs/' + self.file_name
		file = open(file_path, 'w')
		for rec in self.records:
			recStr = str(rec) + '\n'
			file.write(recStr)
		file.close()
		print 'Finished writing to {0}'.format(file_path)
	
def makeFile(file_name):
	file_path = 'generatedLogs/' + file_name
	file = open(file_path, 'w')
	file.write(' ')
	file.close()
	print 'Finished writing'

