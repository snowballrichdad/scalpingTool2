import urllib.request
import urllib.error
import json
import pprint
import settings
import password


def cancelorder(orderID):
    obj = {'OrderID': orderID, 'Password': password.password}
    json_data = json.dumps(obj).encode('utf8')

    url = 'http://localhost:' + settings.port + '/kabusapi/cancelorder'
    req = urllib.request.Request(url, json_data, method='PUT')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', settings.token)

    try:
        print('###cancelorder')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)

            # キャンセル注文の注文ID
            cansel_order_id = content['OrderId']

            return cansel_order_id

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)
