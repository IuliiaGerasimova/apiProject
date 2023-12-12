import requests
import hmac
import hashlib
import json
import copy
from typing import List, Set, Dict, Tuple




#-----Requests Part ------
url_root = 'https://p2psys-publicoffice.konomik.com'

#Headers is a map with headers for request
headers = {'accept': 'application/json',
           'ClientId': 'ID-6892fc719fbc467bae2564f37fdb64f728070be92e744a18b7ede4842ad4181f',
           'Content-Type': 'application/json',
           }

#Query is used as a map with params for the request
query = {
         "id":858,
         "status":"0"
         }


#Payload is used as a body for request
payload = {
 #           "name": "myDev1",
  #          "model": "Pixel4a",
  #          "type": "TYPE_UNKNOWN",
  #          "status": "Active"
          }

#https://p2psys-publicoffice.konomik.com







"""if len(query.keys()) == 0:
    payload_to_json_conv = str(json.dumps(payload))
elif len(payload.keys()) == 0:
    payload_to_json_conv = str(json.dumps(query))
else:
    payload_to_json_conv = (str(json.dumps(query) + str(json.dumps(payload))))"""

def process_sha256(payload:Dict[str,str], query:Dict[str,str], clientSecret:str) -> str:
    query_list: List[str]   = []
    proxy_query:str         = ""
    json_data_bytes:str     = ""
    common_byte_str:str     = ""
    if query.keys != 0:
        for key, value in query.items():
            query_list.append(f"{key}={value}")
        print("&".join(query_list))
    if len(query_list):
        proxy_query=f"{'&'.join(query_list)}"

    if len(payload.keys())!= 0:
        json_data_bytes = json.dumps(payload)

    if (json_data_bytes != "" and proxy_query != ""):
        common_byte_str  = bytes(f"{proxy_query}", 'utf-8')+bytes(f"{json_data_bytes}", 'utf-8')
        print(common_byte_str)
    elif (json_data_bytes == "" and proxy_query != ""):
        common_byte_str = bytes(f"{proxy_query}", 'utf-8')
    elif (json_data_bytes != "" and proxy_query == ""):
        common_byte_str = bytes(f"{json_data_bytes}", 'utf-8')
    else:
        print("ERROR_FUCKER!")
    print(common_byte_str)
    signature = hmac.new(bytes(f"{clientSecret}", 'utf-8'), common_byte_str, hashlib.sha256).hexdigest()
    return signature.lower()


#print("signature_new = {0}".format(process_sha256(json_data=payload_to_json_conv,
 #       clientSecret="18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48")))

#-----Requests Part ------
url_root = 'https://p2psys-publicoffice.konomik.com'


params = {'signature': process_sha256(payload=payload, query=query,
                        clientSecret="18c7652ba591431881391cba29f08fd6bcb2cdc6cbe646ff9d6b03d2f1520d48"),}


"""r = requests.post(url=url_root+"/v1/transactions/withdraw?", data=json.dumps(payload), headers=headers, params=params)
print(r.content)

r = requests.get(url=url_root+"/v1/transactions/withdraw?", data=json.dumps(payload), headers=headers, params=params)
print(r.content)

r = requests.get(url=url_root+"/v1/account/info", data=json.dumps(payload), headers=headers, params=params)
print(r.content)"""

params_prx = copy.deepcopy(params)
params_prx.update(query)

if (len(payload.keys()) == 0):
    r = requests.get(url=url_root+"/v1/devices/858", headers=headers, params=params_prx, json=None)
    print(r.content)
else:
    r = requests.get(url=url_root + "/v1/devices", headers=headers, params=params_prx, json=payload)
    print(r.content)
print(r.request.url)
#print(r.request.body)
#print(r.request.headers)
print(r.content)










