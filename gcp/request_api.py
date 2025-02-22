import requests

res = requests.get(
    "http://10.2.12.123:5001/get_param?x=5&y=8"
)

print(res.json())