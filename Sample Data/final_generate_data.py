"""
Author : Shriniwas Nayak, Saloni Agiwal
Date : 9th Sept 2020
"""

import pandas as pd
import csv
import random as rd
from datetime import datetime
import time


customer_file_name = "customer.csv"
customerOrderFileName = "customerOrder.csv"
brokerFileName = "broker.csv"
tradeBookFileName = "tradebook.csv"

#CHANGE PATH AS PER DIRECTORY & OS
customer_file_path = "C:/Users/hp/Desktop/Untitled Folder/"
customerOrderFilePath = "C:/Users/hp/Desktop/Untitled Folder/"
brokerFilePath = "C:/Users/hp/Desktop/Untitled Folder/"
tradeBookFilePath = "C:/Users/hp/Desktop/Untitled Folder/"

cutomerOrderThreshold = 3500

firmOrderThreshold = 2500

order_id = 100

stock_symbol_list = ["FB","AAPL","WMT"]

security_type_list_customer = ["EQUITY","FUTURES"]
security_type_list = ["EQUITY","FUTURES","CALL OPTION"]

action_list = ["BUY","SELL"]

base_price_list = {"FB" : [270, 278], "AAPL" : [113, 119], "WMT" : [137, 142]}
final_price_list = {"FB" : [270, 278], "AAPL" : [113, 119], "WMT" : [137, 142]}

trade_id = 1000

firm_id = 50

min_price = 30

l = 1
g = 2


"""
input : customer file path (str) & name (str)
function : extract customer IDs
output : return a list of customer IDs (list)
"""

def readCustomerFile(customer_file_path, customer_file_name):

	try:

		cust_df = pd.read_csv(customer_file_path + customer_file_name)

	except:
	
		print("Error in opening : " + customer_file_name)
		exit(1)


	list_of_cust_id = cust_df["customerId"].tolist()
	
	return list_of_cust_id



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
input : dictionary with ticker:[min,max] (dict), stock_name(str), quantiy of stock(int), buy/sell(str)
function : alters the dictionary inplace according to change parameter
output : None
"""
def alterPrice(base_price_list, stock_name, quantity, trade_action):

	change_parameter = 0.001

	stock_price_list = base_price_list[stock_name]
	
	change = change_parameter * quantity
	
	if(trade_action == "SELL"):
	
		change*=-1
		
	stock_price_list[0] += change
	stock_price_list[1] += change



"""
input : dictionary with ticker:[min,max] (dict), stock_name(str), quantiy of stock(int), buy/sell(str)
function : alters the dictionary inplace according to change parameter
output : None
"""
def finalAlterPrice(final_price_list, stock_name, quantity, trade_action, price):
	global min_price 
	change_parameter = 0.005

	stock_price_list = final_price_list[stock_name]
	
	change = change_parameter * quantity
	
	if(trade_action == "SELL"):
	
		stock_price_list[0] -= change
		if(stock_price_list[0]<=0):
			stock_price_list[0] = min_price

		stock_price_list[1] = price
		
	else:
	
		stock_price_list[0] = price
		stock_price_list[1] += change
		
	

"""
"""
def thresholdCheck(quantity):

	global cutomerOrderThreshold

	return quantity > cutomerOrderThreshold



"""
"""
def generateFirmOrderFR(custOrder, base_price_list):

	listOfFirmOrders = []
	
	if(custOrder["trade_action"] == "SELL"):
	
		trade_action = "SELL"
		quantity = rd.choice(range(firmOrderThreshold,custOrder["quantity"],50))
		securityType = rd.choice(security_type_list)
		new_order_s = pd.DataFrame(
           {'stockSymbol':custOrder["stockSymbol"],
            'securityType':securityType, 
            'trade_action':trade_action, 
            'quantity':quantity,
            'price': custOrder["price"]}, index =[0])
        
		alterPrice(base_price_list, custOrder["stockSymbol"], custOrder["quantity"], trade_action)
        
		listOfFirmOrders.append(new_order_s)

		trade_action = "BUY"
		new_order_b = pd.DataFrame(
			{'stockSymbol':custOrder["stockSymbol"],
			'securityType':securityType, 
			'trade_action':trade_action, 
			'quantity':quantity,
			'price': custOrder["price"]}, index =[0])

		alterPrice(base_price_list, custOrder["stockSymbol"], quantity, trade_action)

		listOfFirmOrders.append(new_order_b)

	else:
		choice = rd.randint( 0, 1) 
		if (choice==0) :
			trade_action = "BUY"
			quantity = rd.choice(range(firmOrderThreshold,custOrder["quantity"],50))
			securityType = rd.choice(security_type_list)
			new_order_b = pd.DataFrame(
				{'stockSymbol':custOrder["stockSymbol"],
				'securityType':securityType, 
				'trade_action':trade_action, 
				'quantity':quantity,
				'price': custOrder["price"]}, index =[0])

			alterPrice(base_price_list, custOrder["stockSymbol"], quantity, trade_action)

			listOfFirmOrders.append(new_order_b)

			trade_action = "SELL"
			new_order_s = pd.DataFrame(
				{'stockSymbol':custOrder["stockSymbol"],
				'securityType':securityType, 
				'trade_action':trade_action, 
				'quantity':quantity,
				'price': custOrder["price"] + (0.01*base_price_list[custOrder["stockSymbol"]][1])}, index =[0])


			alterPrice(base_price_list, custOrder["stockSymbol"], quantity, trade_action)

			listOfFirmOrders.append(new_order_s)
		else :
			trade_action = "BUY"
			securityType = rd.choice(security_type_list)
			new_order_b = pd.DataFrame(
               {'stockSymbol':custOrder["stockSymbol"],
                'securityType':securityType, 
                'trade_action':trade_action, 
                'quantity':custOrder["quantity"],
                'price': custOrder["price"]}, index =[0])
			alterPrice(base_price_list, custOrder["stockSymbol"], custOrder["quantity"], trade_action)
			listOfFirmOrders.append(new_order_b)
			trade_action = "SELL"
			new_order_s = pd.DataFrame(
				{'stockSymbol':custOrder["stockSymbol"],
                'securityType':securityType, 
                'trade_action':trade_action, 
                'quantity':custOrder["quantity"],
                'price': custOrder["price"] + (0.01*base_price_list[custOrder["stockSymbol"]][1])}, index =[0])
			alterPrice(base_price_list, custOrder["stockSymbol"], custOrder["quantity"], trade_action)
			listOfFirmOrders.append(new_order_s)
			
	return listOfFirmOrders



"""
"""
def generateFirmOrder(stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate):

	stock_name = rd.choice(stock_symbol_list)
		
	trade_action = rd.choice(action_list)
		
	quantity = rd.choice(range(50,5000,50))

	price = rd.uniform(base_price_list[stock_name][0],base_price_list[stock_name][1])

	securityType = rd.choice(security_type_list)

	new_order = pd.DataFrame(
           {'stockSymbol':stock_name,
            'securityType':securityType, 
            'trade_action':trade_action, 
            'quantity':quantity,
            'price': price}, index =[0])
            
	alterPrice(base_price_list, stock_name, quantity, trade_action)

	return new_order
	

"""
input : empty Data Frame (pandas.DataFrame()) start of order id (int), customer id list (list), ... (list) , size of cust order table (int)
function : generate random orders and alter price accordingly 
output : list of orders (list)
"""
def generateOrders(order_id, customerID_list, stock_symbol_list, security_type_list_customer, action_list, base_price_list, size_to_generate):

	customerOrders = pd.DataFrame()
	
	for i in range(size_to_generate):
	
		stock_name = rd.choice(stock_symbol_list)
		
		trade_action = rd.choice(action_list)
		
		quantity = rd.choice(range(50,5000,50))
		
		new_order = pd.DataFrame(
           {'order_id':order_id, 
            'trade_date':datetime.now().date(), 
			'trade_time' : datetime.now().time(),
            'custID': rd.choice(customerID_list),         
            'stockSymbol':stock_name,
            'securityType':rd.choice(security_type_list_customer), 
            'trade_action':trade_action, 
            'quantity':quantity,
            'price': rd.uniform(base_price_list[stock_name][0],base_price_list[stock_name][1]),
            'status':'Yes'}, index =[0])
        
		alterPrice(base_price_list, stock_name, quantity, trade_action)
        
		order_id += 1
        
		customerOrders = pd.concat([new_order, customerOrders]).reset_index(drop = True) 
	
		
		#time.sleep(rd.uniform(l,g))
	
	return customerOrders




"""
"""
def addOrders(listOfFirmOrders, custOrder, brokerIDList):

	global trade_id

	fraud_df = pd.DataFrame()


	#if(len(listOfFirmOrders) > 1):
	
	
	firmOrder = listOfFirmOrders[0]
	new_df = pd.DataFrame({'trade_id':trade_id, 
					'trade_date':datetime.now().date(), 
					'trade_time' : datetime.now().time().strftime("%H:%M:%S"), 
					'Client_Type': "FIRM",
					'Client_ID' : firm_id,       
					'stockSymbol': firmOrder["stockSymbol"],
					'securityType': firmOrder["securityType"], 
					'trade_action': firmOrder["trade_action"], 
					'quantity':firmOrder["quantity"],
					'price': firmOrder["price"],
					'brokerID' : rd.choice(brokerIDList)},index =[0])

	print("ID : {0}".format(trade_id) )
		
	trade_id += 1
	
	time.sleep(rd.uniform(l,g))
	
	fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
	
	new_df = pd.DataFrame(
					{'trade_id':trade_id, 
					'trade_date':datetime.now().date(), 
					'trade_time' : datetime.now().time().strftime("%H:%M:%S"), 
					'Client_Type': "CUSTOMER",
					'Client_ID' : custOrder["custID"],       
					'stockSymbol': custOrder["stockSymbol"],
					'securityType': custOrder["securityType"], 
					'trade_action':custOrder["trade_action"], 
					'quantity':custOrder["quantity"],
					'price': custOrder["price"],
					'brokerID' : rd.choice(brokerIDList)},index =[0])
					
	trade_id += 1
	
	time.sleep(rd.uniform(l,g))
	
	fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
	
	firmOrder = listOfFirmOrders[1]
	new_df = pd.DataFrame({'trade_id':trade_id, 
					'trade_date':datetime.now().date(), 
					'trade_time' : datetime.now().time().strftime("%H:%M:%S"),
					'Client_Type': "FIRM",
					'Client_ID' : firm_id,       
					'stockSymbol': firmOrder["stockSymbol"],
					'securityType': firmOrder["securityType"], 
					'trade_action': firmOrder["trade_action"], 
					'quantity':firmOrder["quantity"],
					'price': firmOrder["price"],
					'brokerID' : rd.choice(brokerIDList)},index =[0])
		
	trade_id += 1
	
	fraud_df = pd.concat([new_df, fraud_df]).reset_index(drop = True)
	
		
	return fraud_df
	
		

"""
"""
def generateTradeBook(customerOrders, brokerIDList):

	global trade_id

	tradeBook = pd.DataFrame()

	for i in range(len(customerOrders)):
		
		custOrder = customerOrders.loc[i]
		
		
		if(thresholdCheck(custOrder["quantity"])):
		
			if( bool( rd.choices([0,1], weights = [0.85, 0.15], k = 1)[0] ) ):
			
				listOfFirmOrders = generateFirmOrderFR(custOrder, base_price_list)
				new_df = addOrders(listOfFirmOrders, custOrder, brokerIDList)
				tradeBook = pd.concat([new_df, tradeBook]).reset_index(drop = True)
				
			else:
			
				firmOrder = generateFirmOrder(stock_symbol_list, security_type_list, action_list, base_price_list, size_to_generate)
				new_df = pd.DataFrame(
					   {'trade_id':trade_id, 
						'trade_date':datetime.now().date(), 
						'trade_time' : datetime.now().time().strftime("%H:%M:%S"),
						'Client_Type': "FIRM",
						'Client_ID' : firm_id,       
						'stockSymbol': firmOrder["stockSymbol"],
						'securityType': firmOrder["securityType"], 
						'trade_action': firmOrder["trade_action"], 
						'quantity':firmOrder["quantity"],
						'price': firmOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
						
				trade_id += 1	
				
				tradeBook = pd.concat([new_df, tradeBook]).reset_index(drop = True)
				
		else:
		
			new_df = pd.DataFrame(
					   {'trade_id':trade_id, 
						'trade_date':datetime.now().date(), 
						'trade_time' : datetime.now().time().strftime("%H:%M:%S"),
						'Client_Type': "CUSTOMER",
						'Client_ID' : custOrder["custID"],       
						'stockSymbol': custOrder["stockSymbol"],
						'securityType': custOrder["securityType"], 
						'trade_action':custOrder["trade_action"], 
						'quantity':custOrder["quantity"],
						'price': custOrder["price"],
						'brokerID' : rd.choice(brokerIDList)},index =[0])
						
			trade_id += 1
			
			tradeBook = pd.concat([new_df, tradeBook]).reset_index(drop = True)
			
		time.sleep(rd.uniform(l,g))
							
				
	return tradeBook
				
				
"""
input : 
function : 
output : 
"""
def changePrice(tradeBook):

	for iterator in range(len(tradeBook)-1,-1,-1):
	
		tradeBook["price"].iloc[iterator] = float("{0:.2f}".format(rd.uniform(final_price_list[tradeBook["stockSymbol"].iloc[iterator]][0],final_price_list[tradeBook["stockSymbol"].iloc[iterator]][1])))
		
		finalAlterPrice(final_price_list, tradeBook["stockSymbol"].iloc[iterator],tradeBook["quantity"].iloc[iterator], tradeBook["trade_action"].iloc[iterator], tradeBook["price"].iloc[iterator])
		

#MAIN

customerID_list = readCustomerFile(customer_file_path, customer_file_name)

brokerIDList = readBrokerFile(brokerFilePath, brokerFileName)

size_to_generate = 200


customerOrders = generateOrders(order_id, customerID_list, stock_symbol_list, security_type_list_customer, action_list, base_price_list, size_to_generate)
customerOrders.to_csv(customerOrderFilePath + customerOrderFileName, index = False)
tradeBook = generateTradeBook(customerOrders, brokerIDList)

changePrice(tradeBook)

tradeBook.to_csv(tradeBookFilePath + tradeBookFileName, index = False)





