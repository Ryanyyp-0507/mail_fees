import time
from lib2to3.fixes.fix_dict import iter_exempt
from operator import itemgetter

import requests

url_joya = "https://joyabuy.com/wp-admin/admin-ajax.php?action=get_estimation_query_prices"

# params = {
#     "action": "get_estimation_query_prices"
# }

headers = {
    # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryPeB5LXBQArfKKy7u",
    # "Origin": "https://joyabuy.com",
    # "Referer": "https://joyabuy.com/zh/estimation/",
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # "Cookie": "PHPSESSID=kpasnfq8t2ftukrj8ngjtpltkv; wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=zh; _ga=GA1.1.1859330272.1739084233; __ukey=81nf7ejex237; _ss_s_uid=794d38360ed3b348b16b30f5ba05689f; _ga_LLNZ3BEEWR=GS1.1.1739084232.1.0.1739084244.0.0.0",

    "Host": "joyabuy.com",
    "Connection": "keep-alive",
    # "Content-Length": "804",
    "sec-ch-ua-platform": "\"Windows\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryeb1NOzKFJR0IPjbe",
    "sec-ch-ua-mobile": "?0",
    "Accept": "*/*",
    "Origin": "https://joyabuy.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://joyabuy.com/zh/estimation/",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    # "Cookie": "PHPSESSID=kpasnfq8t2ftukrj8ngjtpltkv; wmc_current_currency=USD; wmc_current_currency_old=USD; pll_language=zh; _ga=GA1.1.1859330272.1739084233; __ukey=81nf7ejex237; _ss_s_uid=794d38360ed3b348b16b30f5ba05689f; _ga_LLNZ3BEEWR=GS1.1.1739084232.1.0.1739084244.0.0.0"
}

data = {
    "destination": "GB",
    "weight": 6000,
    "features": None,
    "length": None,
    "width": None,
    "height": None,
    "username": None,
    "password": None,
}

response = requests.post(url=url_joya, data=data,headers=headers)

print(response.status_code)
print(response.json())


fee_datas = response.json()

# print(fee_datas)
my_feedata = {}
my_feedata["国家"] = "美国"
my_feedata["重量"] = "501g"
my_feedata["网站"] = {"siteName": "mulebuy", "venders": []}

for fee in fee_datas['data']:
    if fee['available']:
        # print(fee)
        my_feedata["网站"]['venders'].append([
            {"venderName": fee['name']},
            {'总价': fee['feeDetail']['total']},
            {'首重价格': fee['feeDetail']['feeFirst']},
            {"额外重量价格": fee['feeDetail']["feeContinue"]},
            {"操作费": fee['feeDetail']["operationFee"]},
            {"服务费": fee['feeDetail']["serviceFee"]},
            {"最低重量限制": fee['restrictions']["minWeight"]},
            {"最高重量限制": fee['restrictions']["maxWeight"]},
            {"尺寸限制": fee['restrictions']["dimensionRestriction"]},
            {"体积重量计费规则": fee['restrictions']["volumeWeightRule"]},
            {"运输时间": fee["transitTime"]},

        ])

print(my_feedata)
for item in my_feedata['网站']['venders']:
    print(item)
