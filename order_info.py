import urllib.request
import urllib.parse
import urllib.error
import json
import pprint
import settings
import sys
import variables


def orders_info(orderId):
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
                return None

            # 注文情報を取得
            print(first_order['Details'])
            order_details = first_order['Details']

            order_price = None

            for orderDetail in order_details:
                hold_id = orderDetail['ExecutionID']
                if hold_id is None:
                    continue

                # エントリ値で最も不利な値をエントリ値にする
                if first_order['Side'] == '1':
                    # 売りの場合は最も低い値
                    if order_price is None or orderDetail['Price'] < order_price:
                        order_price = orderDetail['Price']
                else:
                    # 買いの場合は最も高い値
                    if order_price is None or orderDetail['Price'] > order_price:
                        order_price = orderDetail['Price']

            return order_price

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
