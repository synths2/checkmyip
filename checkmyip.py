import json, requests


def checkIP():
    response = requests.get(url='http://telnetmyip.com')
    result = json.loads(response.text)
    print result['ip']
    return result['ip']

if __name__ == "__main__":
    checkIP()