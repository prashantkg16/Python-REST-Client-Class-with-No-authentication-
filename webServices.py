import requests
import json

class webServices:
	_url = "http://aldbnagioscd.dev.att.com:8080/ALDB-NAG/NagiosService"
	
	def __init__(self, serviceMethod):        
		self.serviceMethod = serviceMethod
	
	@property
	def serviceMethod(self):
		return self._serviceMethod
		
	@serviceMethod.setter
	def serviceMethod(self, serviceMethod):
		self._serviceMethod = serviceMethod

	def __str__(self):
		return self._url +"/"+ self.serviceMethod
		
class doRequest(webServices):
	def __init__(self, serviceMethod, **params):
		super().__init__(serviceMethod)
		self.param = params
		
	@property
	def param(self):
		return self._param
	
	@param.setter
	def param(self, params):
		self._param = params	
		
	def _getMethodParam(self):
		if(self.serviceMethod == "fetchKMDetails"):
			return '{}/format.json'.format(self.param['serverName'])
		elif(self.serviceMethod == "fetchRecoveryKMDetails"):
			return '{}/format.json'.format(self.param['serverName'])
		elif(self.serviceMethod == "fetchUrlDetails"):
			return '{}/format.json'.format(self.param['serverName'])
		elif(self.serviceMethod == "fetchRecoveryUrlDetails"):
			return '{}/format.json'.format(self.param['serverName'])
		elif(self.serviceMethod == "updateDetails"):
			''' This method would only update server flag.return code (0 -> Flag update successfully; 1 -> Not updated), check applied only for return code 0, not 1'''
			return '{}/format.json?{}'.format(self.param['serverName'], self.param['returnCode'])
		elif(self.serviceMethod == "addServer"):
			return '{}/{}/{}/{}/format.json? primaryXiServer={}&secondaryXiServer={}'.format(self.param['hostName'], self.param['agentName'], self.param['platform'], self.param['starVersion'], self.param['primaryXiServerName'], self.param['secondaryXiServerName'])
		elif(self.serviceMethod == "deleteServer"):
			return '{}/format.json'.format(self.param['hostName'])
		elif(self.serviceMethod == "addServerToServerGroup"):
			''' Profile and server group should be exist beore server add 
				Server should already exist in ALDB server list. Use addServer method to add server to ALDB server list.
			'''
			return '{}/{}/{}/format.json'.format(self.param['profileName'],self.param['serverGroupName'],self.param['serverName'])
		elif(self.serviceMethod == "submitProfile"):
			'''This will submit the profile for monitoring'''
			return '{}/format.json'.format(self.param['profileName'])
	
	def _call(self):
		response=""
		try:
			response = requests.get(super().__str__() + "/" + self._getMethodParam())
			return response.json()
		except KeyError:
			print("Please validate parameters")
		except TypeError:
			print("Method does not exist")
		
		return response
