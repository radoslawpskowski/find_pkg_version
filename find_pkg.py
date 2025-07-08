import json
import os
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

agents_number = 1
user = "wazuh-api-user"
user_pass = "Your_password_to_wazuh_api_user"

url_auth ="https://localhost:55000/security/user/authenticate"
url = "https://localhost:55000/syscollector/"

auth=(user, user_pass)

params = {
    'raw': 'true',
}

x = requests.post(url = url_auth,params=params, auth = auth, verify=False)
token = x.content.decode("utf-8")

agents_dict = {
}

headers = {
    'Authorization': f"Bearer {token}",
}

params = {
    'pretty': 'true',
    'limit' : '50000',
 }

response_agent = requests.get(url = "https://localhost:55000/agents", params=params, headers=headers, verify=False)
data = json.loads(response_agent.content.decode("utf-8"))

for agents in data.get("data", {}).get("affected_items", []):
  name = agents.get("name", "<brak>")
  agent_id = agents.get("id", "<brak>")

  agents_dict[agent_id] = name

nazwa = input("wprowadz nazwe poszukiwanego pakietu: ")

for i in range (0, agents_number):
 params = {
    'pretty': 'true',
    'limit' : '50000',
 }

 url = f"https://localhost:55000/syscollector/{i:03}/packages"
# print(url)
 response = requests.get(url = url, params=params, headers=headers, verify=False)

 data = json.loads(response.content.decode("utf-8"))

 for pkg in data.get("data", {}).get("affected_items", []):
  name = pkg.get("name", "<brak>")
  version = pkg.get("version", "<brak>")
  if nazwa == name:
    idd = f"{i:03}"

    print(agents_dict[idd])
    print(f"nazwa pakietu {name}", "wersja", version)


