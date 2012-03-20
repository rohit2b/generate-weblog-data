import genWebLogs
""" 
Test LogRecord
"""
def test_LogRecord():
	# Create LogRecord
	logRecord = genWebLogs.LogRecord('urlA', 'ipA', '20120128140223', 'FireFox')
	print 'Test log record in string output: ' 
	print logRecord

def test_writeOneLogRecord():
	logRecord = genWebLogs.LogRecord('urlA', 'ipA', '20120128140223', 'FireFox')
	writer = genWebLogs.RecordsFileWriter([logRecord], 'test_file')
	writer.writeToFile()

def test_generateDaysLogRecords():
	# Use the log generator class to create a set of log records for one day
	gen = genWebLogs.GenerateLogs()
	gen.setupDefaults()
	records = gen.generateRandomLogsForDateRange('20120124','20120125')

def test_writeRecordsToFile():
	gen = genWebLogs.GenerateLogs()
	gen.setupDefaults()
	records = gen.generateRandomLogsForDateRange('20120124','20140224')
	writer = genWebLogs.RecordsFileWriter(records, 'log.out')
	writer.writeToFile()

test_writeRecordsToFile()
