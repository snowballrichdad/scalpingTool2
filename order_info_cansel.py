import urllib.request
import urllib.parse
import urllib.error
import json
import pprint
import settings
import sys
import variables


def orders_info_cansel(orderId):
    url = 'http://localhost:' + settings.port + '/kabusapi/orders'
    params = {'product': 0, 'id': orderId}
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', variables.token)

    try:
        print('###order_info')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            res_json = res.read()
            content = json.loads(res_json)
            pprint.pprint(content)

            first_order = content[len(content) - 1]

            # 注文状態を取得
            print(first_order['State'])
            state = first_order['State']
            # 全約定じゃない場合はNone
            if state != 5:
                return False

            return True

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()


# if __name__ == "__main__":
#     import sys
#
#     tradeP = TradeC.TradeC("test")
#     orders_info(tradeP)
