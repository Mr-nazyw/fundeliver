import json

from doctor_bear_api.bear_apis import BearAPIDeliver

if __name__ == '__main__':
    # data = bear_apis.get_funds_detail(["110011"])
    # print(data["data"])
    sort_info = BearAPIDeliver.FundSortInfo(fund_type=["zq"], sort_range="5n", page_size=40)
    date_top30_3years = BearAPIDeliver().get_sorted_funds(sort_info)
    sort_info = BearAPIDeliver.FundSortInfo(fund_type=["zq"], sort_range="1n", page_size=40)
    date_top30_1years = BearAPIDeliver().get_sorted_funds(sort_info)
    print(json.dumps(date_top30_3years, sort_keys=True, indent=2).encode('utf-8').decode('unicode_escape'))
    print(json.dumps(date_top30_1years, sort_keys=True, indent=2).encode('utf-8').decode('unicode_escape'))
    date_top30_3years = set(date_top30_3years[0])
    date_top30_1years = set(date_top30_1years[0])
    print(date_top30_3years & date_top30_1years)
    fund_details = BearAPIDeliver().get_funds_detail(list(date_top30_3years & date_top30_1years))
    print(json.dumps(fund_details, sort_keys=True, indent=2).encode('utf-8').decode('unicode_escape'))
