import urllib.request
import urllib.error
import json
import pprint
import settings
import password


def token():
    obj = {'APIPassword': password.apiPassword}
    json_data = json.dumps(obj).encode('utf8')

    url = 'http://localhost:' + settings.port + '/kabusapi/token'

    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')

    try:
        print('###token')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)
            token_a = content["Token"]
            f = open("token.txt", 'w')
            f.write(token_a)
            f.close()

            return

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()


if __name__ == "__main__":
    import sys

    token()
