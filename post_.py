import requests
r = requests.post('http://127.0.0.1:5000/recommendation-system', data = {'id':'123456', "Name":"Phương", "...":"ok"})
print(r.json())