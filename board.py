import urllib.request
import urllib.error
import urllib.request
import urllib.error
import json
import datetime

import settings
import variables


def get_current_price():
    url = 'http://localhost:' + settings.port + '/kabusapi/board/' + settings.symbol + '@1'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', variables.token)

    with urllib.request.urlopen(req) as res:
        content = json.loads(res.read())
        cur_price = content["CurrentPrice"]
        now_time = datetime.datetime.now()
        print("##", end=" ")
        print(now_time.strftime("%H:%M:%S"), end=" ")
        print("curPrice", end=":")
        print(cur_price)

        return cur_price
