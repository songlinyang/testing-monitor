import requests
import unittest
import json
rsp = requests.get("http://183.62.139.101:18084/pj-p2p-bank/swagger-ui.html")
print(rsp.status_code)
