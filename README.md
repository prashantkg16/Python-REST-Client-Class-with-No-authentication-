"# Python-REST-Client-Class-with-No-authentication-" 

REST web service client class, it is useful for non-authentication REST web services.

http://aldbnagioscd.dev.att.com:8080/ALDB-NAG/NagiosService/fetchKMDetails/test99.att.com/format.json 

Response:  {"serverName":"test99.att.com","flag":"DN","fileList":[],"procList":[],"runList":[],"logList":[],"mysqlList":[],"mariaDBList":[],"db2List":[],"oracleList":[],"tcpportList":[]}

http://aldbnagioscd.dev.att.com:8080/ALDB-NAG/NagiosService/fetchRecoveryKMDetails/test99.att.com/format.json
Response: {"serverName":"test99.att.com","flag":"DN","fileList":[],"procList":[],"runList":[],"logList":[],"mysqlList":[],"mariaDBList":[],"db2List":[],"oracleList":[],"tcpportList":[]}

http://aldbnagioscd.dev.att.com:8080/ALDB-NAG/NagiosService/fetchUrlDetails/test99.att.com/format.json
Response: {"serverName":"test99.att.com","flag":"DN","urlList":[]}

http://aldbnagioscd.dev.att.com:8080/ALDB-NAG/NagiosService/fetchRecoveryUrlDetails/test99.att.com/format.json
Response: {"serverName":"test99.att.com","flag":"DN","urlList":[]}

It is not generic class because Rest URL was different. I don't want to facilitate user to pass URL.

Required module:
pip install requests
pip install json


Access web service
from webServices import doRequest

data={'serverName':'test99.att.com'}
obResponse = doRequest("fetchKMDetails", **data)
print(obResponse._call())