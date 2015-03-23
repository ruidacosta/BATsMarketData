import time
import sys
import os
from DataMarket import DataMarket

dataMarket = DataMarket()
clearCommand = 'cls' if sys.platform == 'win32' else 'clear'

def genOutputString(data):
	str_out = '''
Ticker:     %s
Company:    %s
Volume:     %s
Orders:     %s
High:       %s
Low:        %s
Open:       %s
Last Trade: %s
TimeStamp:  %s
Change:     %s
Bid: \n%s
Ask: \n%s
Trades: \n%s
	''' % (data['data']['symbol'],data['data']['company'],data['data']['volume'],data['data']['orders'],data['data']['high'],
		data['data']['low'],data['data']['open'],data['data']['last'],data['data']['timestamp'],data['data']['change'],table(('Quant.','Price'),data['data']['bids']),
		table(('Quant.','Price'),data['data']['asks']),table(('DateTime','Quant.','Price'),data['data']['trades']))

	return str_out

def table(header,data_list):
	longg = dict(zip(range(len(header)),(len(str(x)) for x in header)))

	for tu in data_list:
	    longg.update(( i, max(longg[i],len(str(el))) ) for i,el in enumerate(tu))
    
	fofo = ' | '.join('%%-%ss' % longg[i] for i in xrange(len(header)))

	if len(header) == 2:
		return '\n'.join((fofo % header,
        	         '-|-'.join( longg[i]*'-' for i in xrange(len(header))),
            	     '\n'.join(fofo % (a,b) for (a,b) in data_list)))
	elif len(header) == 3:
		return '\n'.join((fofo % header,
        	         '-|-'.join( longg[i]*'-' for i in xrange(len(header))),
            	     '\n'.join(fofo % (a,b,c) for (a,b,c) in data_list)))

def process(data):
	global lastBackSpace
	if data['reload'] != 0:
		os.system(clearCommand)
		sys.stdout.write('%s\r' % genOutputString(data))
		sys.stdout.flush()
	else:
		print 'Ticker unknown.'
		sys.exit(0)
	#print data

def init():
	print 'BATs - Stock Exchanges'
	print 'Please select region'
	print '1. United States'
	print '2. Europe'
	option = 0
	while option not in ['1','2']:
		option = raw_input('Selection: ')
	return option

def USexchange():
	print 'BAT US selected.'
	return raw_input('Enter stock ticker: ')

def EURexchange():
	print 'BAT EUR selected.'
	return raw_input('Enter stock ticker: ')

def makeDataRequest(stock):
	return dataMarket.getUSData(stock)

def main():
	try:
		option = init()
		if option == '1':
			stock = USexchange()
		elif option == '2':
			stock = EURexchange()
		sys.stdout.write('Please wait...')
		while 1:
			data = makeDataRequest(stock)
			process(data)
			#time.sleep(5)
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()