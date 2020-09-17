"""

Date : 10th Sept 2020
Author : Shriniwas Nayak, Akshat Mehta, Shweta Barge

"""

from datetime import datetime


potentialList =[{'trade_id': '1115', 'trade_date': '11-09-2020', 'trade_time': '17:18:26', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4400', 'price': '138.4013253', 'brokerID': '2'}, {'trade_id': '1111', 'trade_date': '11-09-2020', 'trade_time': '17:18:18', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3800', 'price': '134.4668657', 'brokerID': '2'}, {'trade_id': '1096', 'trade_date': '11-09-2020', 'trade_time': '17:17:55', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3950', 'price': '276.5310344', 'brokerID': '4'}, {'trade_id': '1093', 'trade_date': '11-09-2020', 'trade_time': '17:17:50', 'Client_Type': 'CUSTOMER', 'Client_ID': '105', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4650', 'price': '273.8962764', 'brokerID': '2'}, {'trade_id': '1087', 'trade_date': '11-09-2020', 'trade_time': '17:17:40', 'Client_Type': 'CUSTOMER', 'Client_ID': '103', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4900', 'price': '278.9953294', 'brokerID': '3'}, {'trade_id': '1069', 'trade_date': '11-09-2020', 'trade_time': '17:17:13', 'Client_Type': 'CUSTOMER', 'Client_ID': '104', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3950', 'price': '135.197848', 'brokerID': '3'}, {'trade_id': '1060', 'trade_date': '11-09-2020', 'trade_time': '17:17:01', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3850', 'price': '144.5491228', 'brokerID': '3'}, {'trade_id': '1048', 'trade_date': '11-09-2020', 'trade_time': '17:16:43', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4850', 'price': '120.1370385', 'brokerID': '4'}, {'trade_id': '1042', 'trade_date': '11-09-2020', 'trade_time': '17:16:34', 'Client_Type': 'CUSTOMER', 'Client_ID': '102', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4250', 'price': '116.3540292', 'brokerID': '4'}, {'trade_id': '1027', 'trade_date': '11-09-2020', 'trade_time': '17:16:11', 'Client_Type': 'CUSTOMER', 'Client_ID': '104', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4150', 'price': '276.5668563', 'brokerID': '1'}, {'trade_id': '1024', 'trade_date': '11-09-2020', 'trade_time': '17:16:06', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '150.7229455', 'brokerID': '3'}, {'trade_id': '1018', 'trade_date': '11-09-2020', 'trade_time': '17:15:57', 'Client_Type': 'CUSTOMER', 'Client_ID': '101', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4500', 'price': '275.0264973', 'brokerID': '1'}, {'trade_id': '1013', 'trade_date': '11-09-2020', 'trade_time': '17:15:49', 'Client_Type': 'CUSTOMER', 'Client_ID': '105', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4900', 'price': '119.0980699', 'brokerID': '3'}, {'trade_id': '1003', 'trade_date': '11-09-2020', 'trade_time': '17:15:34', 'Client_Type': 'CUSTOMER', 'Client_ID': '102', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3700', 'price': '269.8628606', 'brokerID': '4'}]






firmTradeList = [{'trade_id': '1127', 'trade_date': '11-09-2020', 'trade_time': '17:18:45', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '500', 'price': '253.6000993', 'brokerID': '2'}, {'trade_id': '1122', 'trade_date': '11-09-2020', 'trade_time': '17:18:36', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '400', 'price': '248.2250572', 'brokerID': '2'}, {'trade_id': '1119', 'trade_date': '11-09-2020', 'trade_time': '17:18:31', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '1100', 'price': '157.6692398', 'brokerID': '1'}, {'trade_id': '1118', 'trade_date': '11-09-2020', 'trade_time': '17:18:30', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '350', 'price': '129.5058792', 'brokerID': '4'}, {'trade_id': '1116', 'trade_date': '11-09-2020', 'trade_time': '17:18:27', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3900', 'price': '138.4013253', 'brokerID': '1'}, {'trade_id': '1114', 'trade_date': '11-09-2020', 'trade_time': '17:18:24', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3900', 'price': '138.4013253', 'brokerID': '4'}, {'trade_id': '1112', 'trade_date': '11-09-2020', 'trade_time': '17:18:20', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3800', 'price': '136.1228657', 'brokerID': '3'}, {'trade_id': '1110', 'trade_date': '11-09-2020', 'trade_time': '17:18:16', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3800', 'price': '134.4668657', 'brokerID': '3'}, {'trade_id': '1105', 'trade_date': '11-09-2020', 'trade_time': '17:18:09', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '1550', 'price': '251.625552', 'brokerID': '3'}, {'trade_id': '1103', 'trade_date': '11-09-2020', 'trade_time': '17:18:06', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2650', 'price': '127.3599778', 'brokerID': '1'}, {'trade_id': '1102', 'trade_date': '11-09-2020', 'trade_time': '17:18:04', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '1300', 'price': '251.5360037', 'brokerID': '4'}, {'trade_id': '1101', 'trade_date': '11-09-2020', 'trade_time': '17:18:02', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4450', 'price': '258.4425808', 'brokerID': '3'}, {'trade_id': '1100', 'trade_date': '11-09-2020', 'trade_time': '17:18:00', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '150', 'price': '256.665676', 'brokerID': '2'}, {'trade_id': '1097', 'trade_date': '11-09-2020', 'trade_time': '17:17:56', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3950', 'price': '279.1700344', 'brokerID': '3'}, {'trade_id': '1095', 'trade_date': '11-09-2020', 'trade_time': '17:17:53', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3950', 'price': '276.5310344', 'brokerID': '1'}, {'trade_id': '1094', 'trade_date': '11-09-2020', 'trade_time': '17:17:51', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4650', 'price': '276.5422764', 'brokerID': '2'}, {'trade_id': '1092', 'trade_date': '11-09-2020', 'trade_time': '17:17:48', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4650', 'price': '273.8962764', 'brokerID': '4'}, {'trade_id': '1088', 'trade_date': '11-09-2020', 'trade_time': '17:17:42', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4400', 'price': '278.9953294', 'brokerID': '3'}, {'trade_id': '1086', 'trade_date': '11-09-2020', 'trade_time': '17:17:39', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4400', 'price': '278.9953294', 'brokerID': '1'}, {'trade_id': '1070', 'trade_date': '11-09-2020', 'trade_time': '17:17:15', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3950', 'price': '136.855348', 'brokerID': '4'}, {'trade_id': '1068', 'trade_date': '11-09-2020', 'trade_time': '17:17:12', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3950', 'price': '135.197848', 'brokerID': '1'}, {'trade_id': '1061', 'trade_date': '11-09-2020', 'trade_time': '17:17:02', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '146.2056228', 'brokerID': '1'}, {'trade_id': '1059', 'trade_date': '11-09-2020', 'trade_time': '17:16:59', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3850', 'price': '144.5491228', 'brokerID': '1'}, {'trade_id': '1058', 'trade_date': '11-09-2020', 'trade_time': '17:16:57', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2650', 'price': '130.1562443', 'brokerID': '2'}, {'trade_id': '1057', 'trade_date': '11-09-2020', 'trade_time': '17:16:56', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4600', 'price': '258.0462313', 'brokerID': '2'}, {'trade_id': '1051', 'trade_date': '11-09-2020', 'trade_time': '17:16:47', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4950', 'price': '154.0545482', 'brokerID': '1'}, {'trade_id': '1049', 'trade_date': '11-09-2020', 'trade_time': '17:16:45', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2800', 'price': '120.1370385', 'brokerID': '4'}, {'trade_id': '1047', 'trade_date': '11-09-2020', 'trade_time': '17:16:42', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2800', 'price': '120.1370385', 'brokerID': '4'}, {'trade_id': '1043', 'trade_date': '11-09-2020', 'trade_time': '17:16:35', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4250', 'price': '117.7340292', 'brokerID': '4'}, {'trade_id': '1041', 'trade_date': '11-09-2020', 'trade_time': '17:16:32', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4250', 'price': '116.3540292', 'brokerID': '2'}, {'trade_id': '1035', 'trade_date': '11-09-2020', 'trade_time': '17:16:24', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3350', 'price': '128.8643899', 'brokerID': '2'}, {'trade_id': '1031', 'trade_date': '11-09-2020', 'trade_time': '17:16:18', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2050', 'price': '264.0930627', 'brokerID': '3'}, {'trade_id': '1029', 'trade_date': '11-09-2020', 'trade_time': '17:16:14', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2150', 'price': '127.8078144', 'brokerID': '3'}, {'trade_id': '1028', 'trade_date': '11-09-2020', 'trade_time': '17:16:13', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2500', 'price': '276.5668563', 'brokerID': '3'}, {'trade_id': '1026', 'trade_date': '11-09-2020', 'trade_time': '17:16:09', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2500', 'price': '276.5668563', 'brokerID': '1'}, {'trade_id': '1025', 'trade_date': '11-09-2020', 'trade_time': '17:16:07', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3400', 'price': '150.7229455', 'brokerID': '3'}, {'trade_id': '1023', 'trade_date': '11-09-2020', 'trade_time': '17:16:04', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3400', 'price': '150.7229455', 'brokerID': '2'}, {'trade_id': '1019', 'trade_date': '11-09-2020', 'trade_time': '17:15:58', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4500', 'price': '277.7589973', 'brokerID': '1'}, {'trade_id': '1017', 'trade_date': '11-09-2020', 'trade_time': '17:15:55', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4500', 'price': '275.0264973', 'brokerID': '2'}, {'trade_id': '1016', 'trade_date': '11-09-2020', 'trade_time': '17:15:54', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '1600', 'price': '152.6682422', 'brokerID': '3'}, {'trade_id': '1014', 'trade_date': '11-09-2020', 'trade_time': '17:15:50', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4900', 'price': '120.4295699', 'brokerID': '2'}, {'trade_id': '1012', 'trade_date': '11-09-2020', 'trade_time': '17:15:48', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4900', 'price': '119.0980699', 'brokerID': '1'}, {'trade_id': '1004', 'trade_date': '11-09-2020', 'trade_time': '17:15:36', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3150', 'price': '269.8628606', 'brokerID': '2'}, {'trade_id': '1002', 'trade_date': '11-09-2020', 'trade_time': '17:15:32', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3150', 'price': '269.8628606', 'brokerID': '2'}]



firmDict = dict()

"""
input : checkDate (str), firmList : (list of dictionaries)
function : create a segregated dictionary from 
output : mainMap : dictionary (recursive)
"""
def generateMap(checkDate, firmTradeList):

	mainMap = {"SELL" : dict(), "BUY" : dict()}
	
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
	

	
	return mainMap
	


"""
"""
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
			
			
			


"""
input : mainMap dictionary (recursive), potentialList list of dictionaries
function : 
output : None
"""
def detectFraud(mainMap, potentialList):

	potentialList = sorted(potentialList, key = lambda x : datetime(year = int(x["trade_date"].split("-")[2]), month = int(x["trade_date"].split("-")[1]), day = int(x["trade_date"].split("-")[0]), hour = int(x["trade_time"].split(":")[0]), minute = int(x["trade_time"].split(":")[1]), second = int(x["trade_time"].split(":")[2])))
	
	
	for custTrade in potentialList:
	
		if(custTrade["trade_action"] == "SELL"):
		
			sellTradeId = findSell(mainMap, custTrade, "SSB")
		
			if(sellTradeId):
			
				buyTradeId = findBuy(mainMap, custTrade, "SSB")
				
				if(buyTradeId):
				
					if(firmDict[buyTradeId] == firmDict[sellTradeId]):
				
						print("\n::FRONT RUNNING DETECTED (SSB) ::\nFirm Sell : {0}\tCust Sell : {1}\tFirm Buy : {2}\n\n".format(sellTradeId,custTrade["trade_id"],buyTradeId))
				
				
		else:
		
			buyTradeId = findBuy(mainMap, custTrade, "BBS")
			
			if(buyTradeId):
			
				sellTradeId = findSell(mainMap, custTrade, "BBS")
				
				if(sellTradeId):
				
					if(firmDict[buyTradeId] == firmDict[sellTradeId]):
				
						print("\n::FRONT RUNNING DETECTED (BBS) ::\nFirm Buy : {0}\tCust Buy : {1}\tFirm Sell : {2}\n\n".format(buyTradeId,custTrade["trade_id"],sellTradeId))


"""
input : firmList : (list of dictionaries)
function : 
output : 
"""
def findUniqueDates(firmTradeList):

	dateSet = set()

	for tempDict in firmTradeList:
	
		dateSet.add(tempDict["trade_date"])
		
	return list(dateSet)


"""
input : listOfDates (list of unique dates), firmList : (list of dictionaries)

"""
def generateDateMainMap(listOfDates, firmTradeList):

	mainMap = dict()
	
	for date in listOfDates:

		mainMap[date] = generateMap(date, firmTradeList)
		
	return mainMap

		
#MAIN


listOfDates = findUniqueDates(firmTradeList)

mainMap = generateDateMainMap(listOfDates, firmTradeList)

#print(firmDict)
#print(mainMap)

detectFraud(mainMap, potentialList)


