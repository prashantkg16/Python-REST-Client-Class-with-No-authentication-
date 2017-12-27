from webServices import doRequest

data={'serverName':'test99.att.com'}
obResponse = doRequest("fetchKMDetails", **data)
print(obResponse._call())


#data={'serverName':'test99.att.com','returnCode':'0'}
#data={'hostName':'test99.att.com','agentName':'0','platform':'0','starVersion':'0','primaryXiServerName':'0','secondaryXiServerName':'0'}
#data={'hostName':'test99.att.com'}
#data={'profileName':'proTest1','serverGroupName':'groupTest1','serverName':'test99.att.com',}
#data={'profileName':'proTest1'}
#obResponse = doRequest("submitProfile", **data)


#data={'serverName':'test99.att.com'}
#obResponse = doRequest("fetchKMDetails", **data)
#print(obResponse._call())

#obResponse = Request("fetchKMDetails", argPass)

































#url = 'http://aldbnagioscd.dev.att.com:8080/ALDB-NAG/NagiosService/fetchKMDetails/test9.att.com/format.json'
#data = '''{
  # "query": {
    # "bool": {
      # "must": [
        # {
          # "text": {
            # "record.document": "SOME_JOURNAL"
          # }
        # },
        # {
          # "text": {
            # "record.articleTitle": "farmers"
          # }
        # }
      # ],
      # "must_not": [],
      # "should": []
    # }
  # },
  # "from": 0,
  # "size": 50,
  # "sort": [],
  # "facets": {}
# }'''

# response = requests.get(url)
# print("prashant")
# print(response.json())
