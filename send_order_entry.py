import urllib.request
import urllib.error
import pprint
import json
import sys

import password
import settings
import variables


def send_order_entry(side, qty, marginTradeType, price):

    obj = {'Password': password.password,
           'Symbol': settings.symbol,
           'Exchange': 1,
           'SecurityType': 1,
           'Side': side,
           'CashMargin': 2,
           'MarginTradeType': marginTradeType,
           'DelivType': 0,
           'AccountType': 4,
           'Qty': qty,
           'FrontOrderType': 20,
           'Price': price,
           'ExpireDay': 0}
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:' + settings.port + '/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', variables.token)

    try:
        print('###sendorder_entry')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)

            # エントリ注文の注文ID
            entry_order_id = content['OrderId']

            return entry_order_id

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()
