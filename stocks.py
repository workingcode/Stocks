import sys
import glob
import fnmatch
import os
import urllib2
import csv

		
def refreshStocks():
	print 'refreshing all the downloads'
	downloadStocks(listStocks())

def listStocks():
	listOfStocks = []
	for file in os.listdir('./stocks/'):
		if fnmatch.fnmatch(file, '*.csv'):
			fileName = file.split('.',1)[0]
			print fileName
			listOfStocks.append(fileName)
	return listOfStocks

def downloadFile(url, filename):
	print 'downloading ' + filename
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
			
def downloadStocks(args):
	if not os.path.exists('./stocks/'):
		os.makedirs('./stocks/')
	argNumber = len(args)
	count=0
	while (count < argNumber):
		downloadFile('http://real-chart.finance.yahoo.com/table.csv?s='+args[count]+'&d=10&e=12&f=2014&g=d&a=4&b=16&c=1997&ignore=.csv', args[count]+'.csv')
		count = count + 1
	
def mod(val):
	try:
	 if val<0:
		return val*(-1)
	 else:
		return val
	except:
		return val
	
def maxDayIncrease(args):
    #print 'max_day_increase'
    fileName = './stocks/' +args[0] + '.csv'
    maxDifference=0.0
    openPrice=''
    closePrice=''
    bestDate=''
    with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			try:
				if((float(row[4]) - float(row[1])) > maxDifference):
					maxDifference = float(row[4]) - float(row[1])
					openPrice = row[1]
					closePrice = row[4]
					bestDate =row[0]
				#print 'open :' + openPrice + ', close:' + closePrice + ', maximum:' + str(maxDifference)
			except ValueError:
				pass
				#print 'ValueError'
			except:
				pass
				#print 'Exception ' + str(row)
	#FOO: 2013-10-23 open = 22.00 close = 100.00 diff = 78.00
    print args[0] + ':' + bestDate + ' open = ' + openPrice + ' close = ' + closePrice + ' diff = ' + str(mod(maxDifference))

def maxDayDecrease(args):
	#print 'max_day_decrease'
	fileName = './stocks/' +args[0] + '.csv'
	maxDifference=0.0
	openPrice=''
	closePrice=''
	bestDate=''
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			try:
				if(float(row[4]) - float(row[1]) < maxDifference):
					maxDifference = float(row[4]) - float(row[1])
					openPrice = row[1]
					closePrice = row[4]
					bestDate =row[0]
				#print 'open :' + openPrice + ', close:' + closePrice + ', maximum:' + str(maxDifference)
			except ValueError:
				pass
				#print 'ValueError'
			except:
				pass
				#print 'Exception ' + str(row)
	#FOO: 2013-10-23 open = 22.00 close = 100.00 diff = 78.00
	print args[0] +':'+bestDate+ ' open = ' + openPrice + ' close = ' + closePrice + ' diff =' + str(mod(maxDifference))

def maxDayPercentIncrease(args):
	#print 'max_day_percent_increase' 
	#print 'max_day_decrease'
	fileName = './stocks/' +args[0] + '.csv'
	maxDifference=0.0
	openPrice=''
	closePrice=''
	bestDate=''
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			try:
				if((((float(row[4]) - float(row[1]))/float(row[1]))*100) > maxDifference):
					maxDifference = (((float(row[4]) - float(row[1]))/float(row[1]))*100)
					openPrice = row[1]
					closePrice = row[4]
					bestDate =row[0]
				#print 'open :' + openPrice + ', close:' + closePrice + ', maximum:' + str(maxDifference)
			except ValueError:
				pass
				#print 'ValueError'
			except:
				pass
				#print 'Exception ' + str(row)
	#FOO: 2013-10-23 open = 22.00 close = 100.00 diff = 78.00
	print args[0] +':'+bestDate +' open = ' + openPrice + ' close = ' + closePrice + ' diff =' + str(mod(maxDifference)) + '%'

def maxDayPercentDecrease(args):
	#print 'max_day_percent_decrease'
	fileName = './stocks/' +args[0] + '.csv'
	maxDifference=0.0
	openPrice=''
	closePrice=''
	bestDate=''
	with open(fileName, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			try:
				if(((float(row[4]) - float(row[1]))/float(row[1]))*100 < maxDifference):
					maxDifference = ((float(row[4]) - float(row[1]))/float(row[1]))*100
					openPrice = row[1]
					closePrice = row[4]
					bestDate =row[0]
				#print 'open :' + openPrice + ', close:' + closePrice + ', maximum:' + str(maxDifference)
			except ValueError:
				pass
				#print 'ValueError'
			except:
				pass
				#print 'Exception ' + str(row)
	#FOO: 2013-10-23 open = 22.00 close = 100.00 diff = 78.00
	print args[0] +':'+bestDate +' open = ' + openPrice + ' close = ' + closePrice + ' diff =' + str(mod(maxDifference)) + '%'
	
def whatIf(args):
	print 'what_if'

def top3():
	print 'top3'
	allStocksAvailable = listStocks()
	for eachStock in allStocksAvailable:
		print eachStock

def main(args):
	command = args[1]
	# removing unnecessary params
	args.pop(0)
	args.pop(0)
	if command == 'list':
		print 'List the stocks available for analysis:' 
		listStocks()
	elif command == 'download':
		downloadStocks(args)
	elif command == 'refresh':
	    refreshStocks()
	elif command == 'max_day_increase':
		while len(args) > 0:
			maxDayIncrease(args)
			args.pop(0)
	elif command == 'max_day_decrease':
		while len(args) > 0:
			maxDayDecrease(args)
			args.pop(0)
	elif command == 'max_day_percent_increase':
		while len(args) > 0:
			maxDayPercentIncrease(args)
			args.pop(0)		
	elif command == 'max_day_percent_decrease':
		while len(args) > 0:
			maxDayPercentDecrease(args)
			args.pop(0)	
	elif command == 'what_if':
		whatIf(args)
	elif command == 'top3':
		top3()
	else:
		print 'enter valid args '

if __name__=='__main__':
    sys.exit(main(sys.argv))
