# -*- encoding: utf-8 -*-


import urllib2

import settings


URL = settings.WEB_URL
API = settings.API
CONF = settings.CONF


def main():
    api_url = URL + API + 'comment' + CONF + '&limit=0'
    http_req = urllib2.Request(api_url,
        headers={'ACCEPT': 'application/json, text/html'})
    try:
        response = urllib2.urlopen(http_req)
        print response.read()
        #print response.getcode()
        #print response.info()
        #print response.msg

    except urllib2.HTTPError, error:
        print error.getcode()
        print error


if __name__ == "__main__":
    main()
