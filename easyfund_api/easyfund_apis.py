import json
from urllib import request as m_req
from http.client import HTTPResponse


def my_req():
    url = m_req.Request(url="http://fund.eastmoney.com/pingzhongdata/001186.js?v=20160518155842")
    date: HTTPResponse = m_req.urlopen(url)
    print(date.read().decode("utf-8"))


def get_all_funds_name():
    url = "http://fund.eastmoney.com/js/fundcode_search.js"
    date: HTTPResponse = m_req.urlopen(url)
    print(json.loads(date.read().decode("utf-8")))


