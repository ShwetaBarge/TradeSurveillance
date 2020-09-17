"""
Date : 11th September 2020
Author : Shriniwas Nayak
"""

#min number of trades to ensure transactions can be classified as wash trade
sizeThreshold = 8
priceThreshold = 1000

firmTradeList = [{'trade_id': '1069', 'trade_date': '11-09-2020', 'trade_time': '20:20:23', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1068', 'trade_date': '11-09-2020', 'trade_time': '20:20:22', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1067', 'trade_date': '11-09-2020', 'trade_time': '20:20:21', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1066', 'trade_date': '11-09-2020', 'trade_time': '20:20:20', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1065', 'trade_date': '11-09-2020', 'trade_time': '20:20:19', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1064', 'trade_date': '11-09-2020', 'trade_time': '20:20:18', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1063', 'trade_date': '11-09-2020', 'trade_time': '20:20:17', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1062', 'trade_date': '11-09-2020', 'trade_time': '20:20:16', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1061', 'trade_date': '11-09-2020', 'trade_time': '20:20:15', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1060', 'trade_date': '11-09-2020', 'trade_time': '20:20:14', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4800', 'price': '271.3000955', 'brokerID': '4'}, {'trade_id': '1059', 'trade_date': '11-09-2020', 'trade_time': '20:20:13', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1058', 'trade_date': '11-09-2020', 'trade_time': '20:20:12', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1057', 'trade_date': '11-09-2020', 'trade_time': '20:20:11', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1056', 'trade_date': '11-09-2020', 'trade_time': '20:20:09', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1055', 'trade_date': '11-09-2020', 'trade_time': '20:20:08', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1054', 'trade_date': '11-09-2020', 'trade_time': '20:20:07', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1053', 'trade_date': '11-09-2020', 'trade_time': '20:20:06', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1052', 'trade_date': '11-09-2020', 'trade_time': '20:20:05', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1051', 'trade_date': '11-09-2020', 'trade_time': '20:20:04', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1050', 'trade_date': '11-09-2020', 'trade_time': '20:20:03', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '4300', 'price': '113.838956', 'brokerID': '1'}, {'trade_id': '1049', 'trade_date': '11-09-2020', 'trade_time': '20:20:02', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1048', 'trade_date': '11-09-2020', 'trade_time': '20:20:01', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1047', 'trade_date': '11-09-2020', 'trade_time': '20:20:00', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1046', 'trade_date': '11-09-2020', 'trade_time': '20:19:59', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1045', 'trade_date': '11-09-2020', 'trade_time': '20:19:58', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1044', 'trade_date': '11-09-2020', 'trade_time': '20:19:57', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1043', 'trade_date': '11-09-2020', 'trade_time': '20:19:56', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1042', 'trade_date': '11-09-2020', 'trade_time': '20:19:55', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1041', 'trade_date': '11-09-2020', 'trade_time': '20:19:54', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1040', 'trade_date': '11-09-2020', 'trade_time': '20:19:53', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'FB', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3750', 'price': '277.5852115', 'brokerID': '4'}, {'trade_id': '1039', 'trade_date': '11-09-2020', 'trade_time': '20:19:52', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1038', 'trade_date': '11-09-2020', 'trade_time': '20:19:51', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1037', 'trade_date': '11-09-2020', 'trade_time': '20:19:50', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1036', 'trade_date': '11-09-2020', 'trade_time': '20:19:49', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1035', 'trade_date': '11-09-2020', 'trade_time': '20:19:48', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1034', 'trade_date': '11-09-2020', 'trade_time': '20:19:47', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1033', 'trade_date': '11-09-2020', 'trade_time': '20:19:46', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1032', 'trade_date': '11-09-2020', 'trade_time': '20:19:45', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1031', 'trade_date': '11-09-2020', 'trade_time': '20:19:44', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1030', 'trade_date': '11-09-2020', 'trade_time': '20:19:43', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '3850', 'price': '114.9474984', 'brokerID': '1'}, {'trade_id': '1029', 'trade_date': '11-09-2020', 'trade_time': '20:19:42', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1028', 'trade_date': '11-09-2020', 'trade_time': '20:19:41', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1027', 'trade_date': '11-09-2020', 'trade_time': '20:19:40', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1026', 'trade_date': '11-09-2020', 'trade_time': '20:19:39', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1025', 'trade_date': '11-09-2020', 'trade_time': '20:19:38', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1024', 'trade_date': '11-09-2020', 'trade_time': '20:19:37', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1023', 'trade_date': '11-09-2020', 'trade_time': '20:19:36', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1022', 'trade_date': '11-09-2020', 'trade_time': '20:19:35', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1021', 'trade_date': '11-09-2020', 'trade_time': '20:19:34', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1020', 'trade_date': '11-09-2020', 'trade_time': '20:19:33', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'AAPL', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '2150', 'price': '113.1828717', 'brokerID': '1'}, {'trade_id': '1019', 'trade_date': '11-09-2020', 'trade_time': '20:19:32', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1018', 'trade_date': '11-09-2020', 'trade_time': '20:19:31', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1017', 'trade_date': '11-09-2020', 'trade_time': '20:19:30', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1016', 'trade_date': '11-09-2020', 'trade_time': '20:19:29', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1015', 'trade_date': '11-09-2020', 'trade_time': '20:19:28', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1014', 'trade_date': '11-09-2020', 'trade_time': '20:19:27', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1013', 'trade_date': '11-09-2020', 'trade_time': '20:19:26', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1012', 'trade_date': '11-09-2020', 'trade_time': '20:19:25', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1011', 'trade_date': '11-09-2020', 'trade_time': '20:19:24', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1010', 'trade_date': '11-09-2020', 'trade_time': '20:19:23', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '100', 'price': '139.930339', 'brokerID': '1'}, {'trade_id': '1009', 'trade_date': '11-09-2020', 'trade_time': '20:19:22', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1008', 'trade_date': '11-09-2020', 'trade_time': '20:19:21', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1007', 'trade_date': '11-09-2020', 'trade_time': '20:19:20', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1006', 'trade_date': '11-09-2020', 'trade_time': '20:19:19', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1005', 'trade_date': '11-09-2020', 'trade_time': '20:19:18', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1004', 'trade_date': '11-09-2020', 'trade_time': '20:19:17', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1003', 'trade_date': '11-09-2020', 'trade_time': '20:19:16', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1002', 'trade_date': '11-09-2020', 'trade_time': '20:19:15', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1001', 'trade_date': '11-09-2020', 'trade_time': '20:19:14', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'SELL', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}, {'trade_id': '1000', 'trade_date': '11-09-2020', 'trade_time': '20:19:13', 'Client_Type': 'FIRM', 'Client_ID': '50', 'stockSymbol': 'WMT', 'securityType': 'EQUITY', 'trade_action': 'BUY', 'quantity': '200', 'price': '137.2699641', 'brokerID': '4'}]


"""
input : action (string)
function : returns -1 if sell, 1 otherwise
output : constant (int)
"""
def findType(action):

	if(action == "SELL"):
	
		return -1
		
	else:
	
		return 1
		
		

"""
input : list of firm trades (list of dictionaries)
function : group orders with same broker and same stock Symbol
output : brokerDict (nested dictionary)
"""
def generateBrokerDict(listOfDates, firmTradeList):

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
			
			
			
	return mainMap
	
"""
input : list of orders worth (list of float)
function : find size of largest subset with total zero
output : size (int)
"""
def findSubsetSize(tempList):

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
	
	
"""
input : grouped firm orders (nested dictionary)
function : print wash trades
return : None
"""
def detectWash(mainMap):

	found = False

	for checkDate in mainMap:
	
		brokerDict = mainMap[checkDate]

		for brokerId in brokerDict:
		
			for stockSymbol in brokerDict[brokerId]:
			
				tempList = brokerDict[brokerId][stockSymbol]
				
				maxSize = findSubsetSize(tempList)
				
				if(maxSize > sizeThreshold):
				
					"""print(tempList)
					print(len(tempList))"""
				
					print("\n\nDate : {2}\n::: WASH TRADE DETECTED :::\nBroker Id : {0}\nStock Symbol : {1}\n\n".format(brokerId, stockSymbol,checkDate))
					
					found = True
				
				"""netting = sum(tempList)
				
				#print(netting,len(tempList))
				
				if(len(tempList) > sizeThreshold and abs(netting) < priceThreshold):
				
					print("\n\n::: WASH TRADE DETECTED :::\nBroker Id : {0}\nStock Symbol : {1}\n\n".format(brokerId, stockSymbol))
					
					found = True"""
				

	if(not found):
	
		print("No wash trades detected")



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


#MAIN		

listOfDates = findUniqueDates(firmTradeList)
brokerDict = generateBrokerDict(listOfDates, firmTradeList)
detectWash(brokerDict)




