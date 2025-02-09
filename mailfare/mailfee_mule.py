import requests

url_cnfans = "https://mulebuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

params_cnfans = {
    "action": "get_estimation_query_prices"
}

headers = {
    "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundarywQkmSLhKNWpKOJ9u",
    "Origin":"https://cnfans.com",
    "Referer":"https://cnfans.com/zh/estimation/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=ohp6s0j3vqfcnrbrr1vatq527u; wmc_current_currency=USD; wmc_current_currency_old=USD"
}
data = {
    "destination": "GB",
    "weight": 501,
    "features":None,
    "length":5,
    "width":3,
    "height":4,
    "username":None,
    "password":None,
    "terms":1

}

response = requests.post(url=url_cnfans, data=data)

print(response.status_code)
# print(response.json())

fee_datas = response.json()

# print(fee_datas)


for fee in fee_datas['data']:
    if fee['available']:
        print(fee)

