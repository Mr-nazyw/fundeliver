import json
from urllib import request as m_req
from http.client import HTTPResponse


def get_funds_detail(funds_code: [str]) -> dict:
    """
    api: 返回一个标准json_body，处理方便
    {code: XXX, data: XXX, message: XXX, meta: XXX}
    :return:
    """
    api = "https://api.doctorxiong.club/v1/fund"
    url = f"{api}?code={','.join(funds_code)}"
    req = m_req.Request(url)
    date: HTTPResponse = m_req.urlopen(req)
    res = json.loads(date.read().decode('utf-8'))
    if res['code'] == 400:
        return {}
    elif res['code'] == 405:
        return {}
    elif res['code'] == 500:
        return {}
    else:
        return res


def get_sorted_funds():
    api = "https://api.doctorxiong.club/v1/fund/rank"
    url = api
    params = {
        "fundType": ["hh"],
        "sort": "1n",
        "pageIndex": 1,
        "pageSize": 10
    }
    params = json.dumps(params)
    params = bytes(params, 'utf8')
    headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
    req = m_req.Request(url, data=params, method='POST', headers=headers)
    date: HTTPResponse = m_req.urlopen(req)
    res = json.loads(date.read().decode('utf-8'))
    if res['code'] == 202:
        return "没有符合条件的基金"
    elif res['code'] == 400:
        return "解析请求失败,一般是参数错误"
    elif res['code'] == 500:
        return "内部网络异常"
    else:
        return res
