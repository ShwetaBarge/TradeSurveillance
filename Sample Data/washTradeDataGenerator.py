import pandas as pd
import csv
import random as rd
from datetime import datetime
import time

brokerFileName = "broker.csv"
washTradeBookFileName = "WashTradeBook.csv"

#CHANGE PATH AS PER DIRECTORY & OS
brokerFilePath = "C:/Users/hp/Desktop/Untitled Folder/"
washTradeBookFilePath = "C:/Users/hp/Desktop/Untitled Folder/"

trade_id = 100
stock_symbol_list = ["FB","AAPL","WMT"]
security_type_list = ["EQUITY"]
action_list = ["BUY","SELL"]
base_price_list = {"FB" : [270, 278], "AAPL" : [113, 116], "WMT" : [137, 142]}
trade_id = 1000
firm_id = 50
l = 1
g = 1

"""
input : broker file path (str) & name (str)
function : extract broker IDs
output : return a list of broker IDs (list)
"""
def readBrokerFile(brokerFilePath, brokerFileName):

	try:

		broker_df = pd.read_csv(brokerFilePath + brokerFileName)

	except:
	
		print("Error in opening : " + brokerFileName)
		exit(1)


	listOfBrokerID = broker_df["Broker Id"].tolist()
	
	return listOfBrokerID


"""

"""
def generateWashTrade(washTradeBook, trade_id, brokerIDList,stock_symbol_list, security_type_list, action_list, base_price_list):

    for i in range(20):
        stock_name = rd.choice(stock_symbol_list)
        securityType = rd.choice(security_type_list)
        action = rd.choice(action_list)
        quantity = rd.choice(range(50,5000,50))
        price = round(rd.uniform(base_price_list[stock_name][0],base_price_list[stock_name][1]),2)
        brokerID = rd.choice(brokerIDList)
        print(stock_name)
        new_order = pd.DataFrame(
                {'trade_id':trade_id, 
                'trade_date':datetime.now().date(), 
                'trade_time' : datetime.now().time().strftime("%H:%M:%S"), 
                'Client_Type': "FIRM",
                'Client_ID' : firm_id,       
                'stockSymbol':stock_name,
                'securityType': securityType, 
                'trade_action':action, 
                'quantity':quantity,
                'price': price,
                'brokerID' : brokerID },index =[0])

        washTradeBook = pd.concat([new_order, washTradeBook]).reset_index(drop = True)
        trade_id += 1
        time.sleep(rd.uniform(l,g))

        # alterPrice(base_price_list, stock_name, quantity, action)
        for i in range(9):
            choice = rd.randint( 0, 1) 
            if (choice==0) :
                new_order_b = pd.DataFrame({'trade_id':trade_id, 
                                            'trade_date':datetime.now().date(), 
                                            'trade_time' : datetime.now().time().strftime("%H:%M:%S"), 
                                            'Client_Type': "FIRM",
                                            'Client_ID' : firm_id,       
                                            'stockSymbol':stock_name,
                                            'securityType':securityType, 
                                            'trade_action':"BUY", 
                                            'quantity':quantity,
                                            'price': price,
                                            'brokerID' : brokerID},index =[0])
                washTradeBook = pd.concat([new_order_b, washTradeBook]).reset_index(drop = True)
                trade_id += 1
                time.sleep(rd.uniform(l,g))

            else:
                new_order_s= pd.DataFrame({'trade_id':trade_id, 
                                            'trade_date':datetime.now().date(), 
                                            'trade_time' : datetime.now().time().strftime("%H:%M:%S"), 
                                            'Client_Type': "FIRM",
                                            'Client_ID' : firm_id,       
                                            'stockSymbol':stock_name,
                                            'securityType':securityType, 
                                            'trade_action':"SELL", 
                                            'quantity':quantity,
                                            'price': price,
                                            'brokerID' : brokerID},index =[0])
                washTradeBook = pd.concat([new_order_s, washTradeBook]).reset_index(drop = True)
                trade_id += 1
                time.sleep(rd.uniform(l,g))
    return washTradeBook

brokerIDList = readBrokerFile(brokerFilePath, brokerFileName)
washTradeBook= pd.DataFrame()
washTradeBook = generateWashTrade(washTradeBook,trade_id, brokerIDList,stock_symbol_list, security_type_list, action_list, base_price_list)
washTradeBook.to_csv( washTradeBookFilePath + washTradeBookFileName, index = False)


