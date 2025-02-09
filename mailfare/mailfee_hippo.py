import requests, json

url_hippo = "https://api-jiyun-v3.haiouoms.com/api/client/express/price-query"


headers = {
    "Host": "api-jiyun-v3.haiouoms.com",
    "Connection": "keep-alive",
    "Content-Length": "150",
    "language": "zh_CN",
    "sec-ch-ua-platform": "\"Windows\"",
    "Authorization": "null",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "currency": "USD",
    "sec-ch-ua-mobile": "?0",
    "App-key": "arIM1n8tmcrHgD1jHz0Zt8H1XPxUjVen",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "X-Uuid": "dd70dbad-9df5-4813-b17d-910a60dd54ef",
    "Origin": "https://hippoobuy.com",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://hippoobuy.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

data = {"warehouse_id":1250,"country_id":11987,"area_id":"","sub_area_id":"","weight":5700000,"length":"","width":"","height":"","prop_ids":[],"postcode":""}

response = requests.post(url=url_hippo,  headers=headers, json=data, verify=False)

# print(response)
print(response.json())
# print(response.json())

# fee_datas = response.json()

# print(fee_datas)


# for fee in fee_datas['data']:
#     if fee['available']:
#         print(fee)

