import json
from urllib import request as m_req
from http.client import HTTPResponse


class BearAPIDeliver:
    """
    API调用来自：https://www.doctorxiong.club/#/guide
    本类提供使用该APIs的基本方法集合
    """

    class FundSortInfo:
        def __init__(self, fund_type=None, sort_range="3n", asc=0, page_size=10):
            """
            使用类BearAPIDeliver的get_sorted_funds方法的参数列表集合类，默认提供四个可传人参数
            其他参数若需要制定，需要手动修改对象的元素值，如声明对象后，制定修改元素
            :param fund_type: 基金类型，默认为空表示所有类型
            :param sort_range: 净值时间，默认按3年净值排序
            :param asc: 排序升序或者降序
            :param page_size: 排序的每个页面数量，即返回的一个结果的基金个数
            """
            if fund_type is None:
                fund_type = []
            self.fund_type = fund_type
            self.sort_range = sort_range
            self.fund_company = ""
            self.creat_time_limit = ""
            self.asc = asc
            self.fund_scale = ""
            self.page_index = 1
            self.page_size = page_size

    def __init__(self):
        pass

    def get_funds_detail(self, funds_code: [str]) -> dict:
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

    def get_sorted_funds(self, msg: FundSortInfo) -> (list, str):
        """
        接受一个FundSortInfo类，提供了所有筛选基金的信息，而后进行基金的筛选接口调用
        :return:
        """
        api = "https://api.doctorxiong.club/v1/fund/rank"
        url = api
        params = {
            "fundType": msg.fund_type,
            "sort": msg.sort_range,
            "pageIndex": msg.page_index,
            "pageSize": msg.page_size
        }
        print(params)
        params = json.dumps(params)
        params = bytes(params, 'utf8')
        headers = {'Accept-Charset': 'utf-8', 'Content-Type': 'application/json'}
        req = m_req.Request(url, data=params, method='POST', headers=headers)
        date: HTTPResponse = m_req.urlopen(req)
        res = json.loads(date.read().decode('utf-8'))
        if res['code'] == 200:
            return [x["code"] for x in res["data"]["rank"]], ""
        else:
            if res['code'] == 202:
                return None, "没有符合条件的基金"
            elif res['code'] == 400:
                return None, "解析请求失败,一般是参数错误"
            elif res['code'] == 500:
                return None, "内部网络异常"
            elif res['code'] == 412:
                return None, "参数解析失败，检查调用参数是否符合规范"
