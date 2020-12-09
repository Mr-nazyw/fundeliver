import json

from doctor_bear_api import bear_apis

if __name__ == '__main__':
    # data = bear_apis.get_funds_detail(["110011"])
    # print(data["data"])
    date = bear_apis.get_sorted_funds()
    print(json.dumps(date, sort_keys=True, indent=2).encode('utf-8').decode('unicode_escape'))
