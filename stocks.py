import sys
import glob
import fnmatch
import os
import urllib2

def listStocks():
	print 'List the stocks available for analysis:' 
	for file in os.listdir('./stocks/'):
		if fnmatch.fnmatch(file, '*.csv'):
			print file.split('.',1)[0]

def downloadFile(url, filename):
	print 'downloading each file'
	#"http://ichart.finance.yahoo.com/table.csv?s=AAPL&amp;d=1&amp;e=1&amp;f=2014&amp;g=d&amp;a=8&amp;b=7&amp;c=1984&amp;ignore=.csv")
	# Retrieve the webpage as a string
	response = urllib2.urlopen(url)
	csv = response.read()
	# Save the string to a file
	csvstr = str(csv).strip("b'")
	lines = csvstr.split("\\n")
	f = open('./stocks/'+filename, "w")
	for line in lines:
		f.write(line + "\n")
	f.close()
			
''' http://real-chart.finance.yahoo.com/table.csv?s=AMZN&d=10&e=12&f=2014&g=d&a=4&b=16&c=1997&ignore=.csv ''' 
def downloadStocks(args):
	if not os.path.exists('./stocks/'):
		os.makedirs('./stocks/')
	print 'downloading all the files'
	argNumber = len(args)
	print argNumber
	count=1
	while (count < argNumber):
		downloadFile('http://real-chart.finance.yahoo.com/table.csv?s='+args[1+count]+'&d=10&e=12&f=2014&g=d&a=4&b=16&c=1997&ignore=.csv', args[1+count]+'.csv')
		count = count + 1
		
def refreshStocks():
	print 'refreshing all the downloads'
	
def maxDayIncrease():
	print 'max_day_increase'
	
def maxDayDecrease():
	print 'max_day_decrease'

def maxDayPercentIncrease():
	print 'max_day_percent_increase' 

def maxDayPercentDecrease():
	print 'max_day_percent_decrease'
	
def whatIf():
	print 'what_if'

def top3():
	print 'top3'

def main(args):
	command = args[1]
	if command == 'list':
		listStocks()
	elif command == 'download':
		downloadStocks(args)
	elif command == 'refresh':
	    refreshStocks()
	elif command == 'max_day_increase':
		maxDayIncrease()
	elif command == 'max_day_decrease':
		maxDayDecrease()
	elif command == 'max_day_percent_increase':
		maxDayPercentIncrease()
	elif command == 'max_day_percent_decrease':
		maxDayPercentDecrease()
	elif command == 'what_if':
		whatIf()
	elif command == 'top3':
		top3()

if __name__=='__main__':
    sys.exit(main(sys.argv))
