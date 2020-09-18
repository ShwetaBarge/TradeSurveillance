# -*- coding: utf-8 -*-
# try something like
from datetime import datetime

def index(): return dict(message="hello from tradebook.py")

#Takes order from user
def post():
    '''
    Take form information and post it into database
    params:
        forms - SQLFORM
    '''
    form = SQLFORM(db.tradebook).process()
    # db.blog - tells to connect this form to blog table that has been created
    # process() = does the enitre insert in the blog table
    if form.process().accepted:
       session.flash = 'form accepted'
       redirect(URL('view'))
    elif form.errors:
       response.flash = 'form has errors'
    else:
       response.flash = 'please fill out the form'
    return locals()


def view():
    #Displays Table Tradebook, if empty goes to insert_table
    rows = db(db.tradebook).select() or db.tradebook.import_from_csv_file(open('C:/Users/HP/OneDrive/Desktop/UBS Training/web2py/web2py/applications/watchDogs/Sample Data/tradebook.csv', 'r', encoding='utf-8', newline=''))
    rows = db(db.tradebook).select()
    return locals()



def view_washtrade():
    # Displays table, if empty -> fills table
    db(db.tradebook_wash).select() or db.tradebook_wash.import_from_csv_file(open('C:/Users/HP/OneDrive/Desktop/UBS Training/web2py/web2py/applications/watchDogs/Sample Data/WashTradeBook.csv', 'r', encoding='utf-8', newline=''))
    rows = db(db.tradebook_wash).select()
    
    ### INSERT into broker table if emtpy
    db(db.broker).select() or  db.broker.import_from_csv_file(open('C:/Users/HP/OneDrive/Desktop/UBS Training/web2py/web2py/applications/watchDogs/Sample Data/broker.csv', 'r', encoding='utf-8', newline=''))
    return locals()

###--------------------FRONTRUNNING-----------------------------------
def findBuy(mainMap, custTrade, typeToFind):
	stockSymbol = custTrade["stockSymbol"]
	date = custTrade["trade_date"]
	if(date not in mainMap):
		return None
	tempDict = mainMap[date]["BUY"]
	if(stockSymbol not in tempDict):
		return None

	tempList = tempDict[stockSymbol]
	date = list(map(int,custTrade["trade_date"].split("-")))
	time = list(map(int,custTrade["trade_time"].split(":")))
	custTimeStamp = datetime(year = date[2], month = date[1], day = date[0], hour = time[0], minute = time[1], second = time[2])

	if(typeToFind == "BBS"): 
		if(tempList[-1][1] < custTimeStamp):
			tradeId = tempList[-1][0]
			tempList.pop()
			return tradeId
		return None
	else:
		ans = tuple([None])
		if(custTimeStamp > tempList[0][1]):
			return None
		iterator = 0
		for iterator in range(len(tempList)):
			if(tempList[iterator][1] > custTimeStamp):
				ans = tempList[iterator]
			else:
				break
		tempList.pop(iterator)
		return ans[0]
	
		


"""
"""
def findSell(mainMap, custTrade, typeToFind):
	stockSymbol = custTrade["stockSymbol"]
	date = custTrade["trade_date"]
	
	if(date not in mainMap):
		return None
	
	tempDict = mainMap[date]["SELL"]
		
	if(stockSymbol not in tempDict):
		return None			
		
	tempList = tempDict[stockSymbol]
	date = list(map(int,custTrade["trade_date"].split("-")))
	time = list(map(int,custTrade["trade_time"].split(":")))
	custTimeStamp = datetime(year = date[2], month = date[1], day = date[0], hour = time[0], minute = time[1], second = time[2])
	if(typeToFind == "SSB"):
		if(tempList[-1][1] < custTimeStamp):
			tradeId = tempList[-1][0]
			tempList.pop()
			return tradeId
		return None
	else:
		ans = tuple([None])
		if(custTimeStamp > tempList[0][1]):
			return None
		iterator = 0
		for iterator in range(len(tempList)):
			if(tempList[iterator][1] > custTimeStamp):
				ans = tempList[iterator]
			else:
				break
		tempList.pop(iterator)
		return ans[0]		

def generateMap(checkDate, firmTradeList):
	mainMap = {"SELL" : dict(), "BUY" : dict()}
	firmDict = dict()
	for firmTrade in firmTradeList:	
		firmDict[firmTrade["trade_id"]] = firmTrade["securityType"]	
		if(firmTrade["trade_date"] == checkDate):	
			if(firmTrade["trade_action"] == "SELL"):			
				tempDict = mainMap["SELL"] 				
			else:			
				tempDict = mainMap["BUY"]			
			date = list(map(int,firmTrade["trade_date"].split("-")))			
			time = list(map(int,firmTrade["trade_time"].split(":")))	
			
			timeStamp = datetime(year = date[2], month = date[1], day = date[0], hour = time[0], minute = time[1], second = time[2])	
			
			tempTuple = tuple([firmTrade["trade_id"], timeStamp])			
			if(firmTrade["stockSymbol"] in tempDict):			
				tempDict[firmTrade["stockSymbol"]].append(tempTuple)
				
			else:			
				tempDict[firmTrade["stockSymbol"]] = [tempTuple]
	return mainMap, firmDict

def findUniqueDates(firmTradeList):
	dateSet = set()
	for tempDict in firmTradeList:	
		dateSet.add(tempDict["trade_date"])		
	return list(dateSet)



def get_data_for_frontrunning():
    threshold = 3500
    query_cust = "SELECT trade_id,trade_date,trade_time,Client_Type,Client_ID,stockSymbol,securityType,trade_action,quantity,price,brokerID FROM tradebook where cast(quantity as integer) > {0} and Client_Type = 'CUSTOMER' ORDER BY trade_time DESC ;".format(threshold)
    query_firm = "SELECT trade_id,trade_date,trade_time,Client_Type,Client_ID,stockSymbol,securityType,trade_action,quantity,price,brokerID FROM tradebook where Client_Type = 'FIRM' ORDER BY trade_time DESC;"

    potentialList = db.executesql(query_cust, as_dict=True)
    firmTradeList = db.executesql(query_firm, as_dict=True)
    table = db.executesql(query_cust)
    table1 = db.executesql(query_firm)
    
    
    listOfDates = findUniqueDates(firmTradeList)
    mainMap = dict()	
    firmDict = dict()
    for date in listOfDates:
        mainMap[date], firmDict = generateMap(date, firmTradeList)


    potentialList = sorted(potentialList, key = lambda x : datetime(year = int(x["trade_date"].split("-")[2]), month = int(x["trade_date"].split("-")[1]), day = int(x["trade_date"].split("-")[0]), hour = int(x["trade_time"].split(":")[0]), minute = int(x["trade_time"].split(":")[1]), second = int(x["trade_time"].split(":")[2])))
	

    fraud_SSB = []
    fraud_BBS = []
    for custTrade in potentialList:	
        if(custTrade["trade_action"] == "SELL"):		
            sellTradeId = findSell(mainMap, custTrade, "SSB")		
            if(sellTradeId):			
                buyTradeId = findBuy(mainMap, custTrade, "SSB")			
                if(buyTradeId):				
                    if(firmDict[buyTradeId] == firmDict[sellTradeId]):				
                        print("\n::FRONT RUNNING DETECTED (SSB) ::\nFirm Sell : {0}\tCust Sell : {1}\tFirm Buy : {2}\n\n".format(sellTradeId,custTrade["trade_id"],buyTradeId))
                        key = [sellTradeId,custTrade["trade_id"],buyTradeId]
                        if key not in fraud_SSB:
                            fraud_SSB.append(key)
        else:		
            buyTradeId = findBuy(mainMap, custTrade, "BBS")			
            if(buyTradeId):			
                sellTradeId = findSell(mainMap, custTrade, "BBS")				
                if(sellTradeId):				
                    if(firmDict[buyTradeId] == firmDict[sellTradeId]):				
                        print("\n::FRONT RUNNING DETECTED (BBS) ::\nFirm Buy : {0}\tCust Buy : {1}\tFirm Sell : {2}\n\n".format(buyTradeId,custTrade["trade_id"],sellTradeId))
                        key = [buyTradeId,custTrade["trade_id"],sellTradeId]
                        if key not in fraud_BBS:
                            fraud_BBS.append(key)
    index = 0
    i = index
    for key in fraud_SSB:
        for key_id in key:
            query_SSB = "INSERT INTO front_running_SSB SELECT {0},trade_id,trade_date,trade_time,Client_Type,Client_ID,stockSymbol,securityType,trade_action,quantity,price,brokerID FROM tradebook WHERE trade_id  =  {1} ;".format(i,key_id)
            # Check if already present in table then insert
            db(db.front_running_SSB.trade_id == key_id).select() or db.executesql(query_SSB)
            i = i + 1
    front_running_SSB = db(db.front_running_SSB).select()

#Populating front_running_BBS
    i = index
    for key in fraud_BBS:
        for key_id in key:
            query_BBS = "INSERT INTO front_running_BBS SELECT {0},trade_id,trade_date,trade_time,Client_Type,Client_ID,stockSymbol,securityType,trade_action,quantity,price,brokerID FROM tradebook WHERE trade_id  =  {1} ;".format(i,key_id)
            i = i + 1
            # Check if already present in table
            db(db.front_running_BBS.trade_id == key_id).select() or db.executesql(query_BBS)
    front_running_BBS = db(db.front_running_BBS).select()

    return locals()

#-------------------------------------------------------------------------------
# WASH TRADES FUNCTIONS

def findType(action):
    sizeThreshold = 8
    priceThreshold = 1000
    if(action == "SELL"):
        return -1
    else:
        return 1

def findSubsetSize(tempList):
    sizeThreshold = 8
    priceThreshold = 1000
    numDict = {0:0}
    altDict = dict()
    for num in tempList:
        keyList = numDict.keys()		
        for key in keyList:		
            temp = 0		
            if( (num + key) in keyList):			
                temp = numDict[key]							
            altDict[num + key] = max(temp, numDict[key] + 1)			
        numDict = {**altDict}		
    if(0 in numDict):	
        return numDict[0]		
    else:	
        return 0
	

def findUniqueDatesW(firmTradeList):
    sizeThreshold = 8
    priceThreshold = 1000
    dateSet = set()
    for tempDict in firmTradeList:	
        dateSet.add(tempDict["trade_date"])		
    return list(dateSet)


def get_data_washtrade():
    sizeThreshold = 8
    priceThreshold = 1000

    
    query_firm = "SELECT trade_id,trade_date,trade_time,Client_Type,Client_ID,stockSymbol,securityType,trade_action,quantity,price,brokerID FROM tradebook_wash;"
    firmTradeList = db.executesql(query_firm, as_dict=True)
    
    listOfDates = findUniqueDatesW(firmTradeList)

    mainMap = dict()
    for checkDate in listOfDates:	
        mainMap[checkDate] = dict()	
    for firmTrade in firmTradeList:	
        brokerId = firmTrade["brokerID"]
        stockSymbol = firmTrade["stockSymbol"]	
        tradeDate = firmTrade["trade_date"]	
        brokerDict = mainMap[tradeDate]	
        if(brokerId in brokerDict):		
            tempDict = brokerDict[brokerId]		
            if(stockSymbol in tempDict):			
                tempList = tempDict[stockSymbol]				
                tempList.append(findType(firmTrade["trade_action"]) * int(firmTrade["quantity"]) * float(firmTrade["price"]))	
				
            else:			
                tempDict[stockSymbol] = [findType(firmTrade["trade_action"]) * int(firmTrade["quantity"]) * float(firmTrade["price"])]		
			
        else:		
            tempList = [findType(firmTrade["trade_action"]) * int(firmTrade["quantity"]) * float(firmTrade["price"])]		
            brokerDict[brokerId] = {stockSymbol : tempList}


    found = False
    for checkDate in mainMap:
        brokerDict = mainMap[checkDate]
        for brokerId in brokerDict:		
            for stockSymbol in brokerDict[brokerId]:
                brokerId_attr = brokerId
                stockSymbol_attr = stockSymbol
                tempList = brokerDict[brokerId][stockSymbol]				
                maxSize = findSubsetSize(tempList)				
                if(maxSize > sizeThreshold):		
                    print("\n\nDate : {2}\n::: WASH TRADE DETECTED :::\nBroker Id : {0}\nStock Symbol : {1}\n\n".format(brokerId, stockSymbol,checkDate))					
                    found = True
                    query_1 = "INSERT INTO wash_trade_broker SELECT id,Broker_Id,Broker_Name,Email, email, email FROM broker WHERE Broker_ID  =  {0};".format(brokerId)
                    db(db.wash_trade_broker.Broker_Id == brokerId).select() or db.executesql(query_1)
                    db.wash_trade_broker.update_or_insert(db.wash_trade_broker.Broker_Id == brokerId,
                           stockSymbol= stockSymbol_attr,
                                                     date_trade = checkDate)
                rows = db(db.wash_trade_broker).select()
    if(not found):	
        print("No wash trades detected")
    return locals()


#-----------------------------------------Download as CSVs----------------------------------------
def export_to_csv_wash_trade():
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')

    response.headers['Content-disposition'] = 'attachment; filename=Wash_Trade.csv'
    query = (db.wash_trade_broker.id>0)
    return str(db(query).select())


def export_to_csv_front_running_SSB():
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')

    response.headers['Content-disposition'] = 'attachment; filename=Frontrunning_SSB.csv'
    query = (db.front_running_SSB.id>0)
    return str(db(query).select())

def export_to_csv_front_running_BBS():
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')

    response.headers['Content-disposition'] = 'attachment; filename=Frontrunning_BBS.csv'
    query = (db.front_running_BBS.id>0)
    return str(db(query).select())
