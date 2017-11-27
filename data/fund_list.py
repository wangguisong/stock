import requests

source_url ='http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page=1,9999&feature=|&dt=&atfc=&onlySale=1'

def get_fund_list():
    r = requests.get(source_url)
    return r.text
