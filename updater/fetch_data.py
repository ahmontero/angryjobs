# -*- encoding: utf-8 -*-


import simplejson as json
import urllib2

from utils import IJParser
import settings


URL = settings.WEB_URL
API = settings.API
CONF = settings.CONF

NUMBER_PAGES = 1


def main():
    parser = 'lxml'
    ijparser = IJParser(parser, pages_limit=NUMBER_PAGES)
    companies = ijparser.companies
    premium_offers = ijparser.premium_offers
    standard_offers = ijparser.standard_offers
    banners = ijparser.banners

    print '>>> Nº Banners: %s' % len(banners)
    objects_added = 0
    for banner in banners:
        banner_api_url = URL + API + 'banner' + CONF
        json_post = json.dumps({"url": banner})
        http_req = urllib2.Request(banner_api_url, json_post, {
            'Content-Type': 'application/json',
            'ACCEPT': 'application/json, text/html'
        })

        if send_data(http_req):
            objects_added += 1
    print '    >>> Added %s banners' % objects_added

    print '>>> Nº Companies: %s' % len(companies)
    objects_added = 0
    for key, company in companies.items():
        company_api_url = URL + API + 'company' + CONF

        json_post = json.dumps({
            "source": company['source'],
            "cid": company['cid'],
            "name": company['name'],
            "link": company['link'],
            "shitty": company['shitty']
            })
        http_req = urllib2.Request(company_api_url, json_post,
            {'Content-Type': 'application/json',
             'ACCEPT': 'application/json, text/html'})

        if send_data(http_req):
            objects_added += 1
    print '    >>> Added %s companies' % objects_added

    print '>>> Nº Premium offers: %s' % len(premium_offers)
    objects_added = 0
    for offer in premium_offers:
        company_api_url = URL + API + 'offer' + CONF

        company = get_company(offer.company_cid)
        if company:
            json_post = json.dumps({
                "source": offer.source,
                "company": "/api/v1/company/%s/" % company['id'],
                "profile": "/api/v1/profile/%s/" % offer.profile,
                "vacant": offer.vacant,
                "link": offer.url,
                "css_class": offer.css_class,
                "poblation": offer.poblation,
                "date": offer.date,
                "level": offer.level,
                "description": offer.description,
                "min_form": offer.min_form,
                "min_exp": offer.min_exp,
                "min_req": offer.min_req,
                "des_req": offer.des_req,
                "salary": offer.salary,
                "number_of_vacants": offer.number_of_vacants,
                "premium": True
                })
            http_req = urllib2.Request(company_api_url, json_post,
                {'Content-Type': 'application/json',
                 'ACCEPT': 'application/json, text/html'})

            if send_data(http_req):
                objects_added += 1
        else:
            print 'Ouch!'
    print '    >>> Added %s premium offers' % objects_added

    print '>>> Nº Standard offers: %s' % len(standard_offers)
    objects_added = 0
    for offer in standard_offers:
        company_api_url = URL + API + 'offer' + CONF

        company = get_company(offer.company_cid)
        if company:
            json_post = json.dumps({
                "source": offer.source,
                "company": "/api/v1/company/%s/" % company['id'],
                "profile": "/api/v1/profile/%s/" % offer.profile,
                "vacant": offer.vacant,
                "link": offer.url,
                "css_class": offer.css_class,
                "poblation": offer.poblation,
                "date": offer.date,
                "level": offer.level,
                "description": offer.description,
                "min_form": offer.min_form,
                "min_exp": offer.min_exp,
                "min_req": offer.min_req,
                "des_req": offer.des_req,
                "salary": offer.salary,
                "number_of_vacants": offer.number_of_vacants,
                "premium": False
                })
            http_req = urllib2.Request(company_api_url, json_post,
                {'Content-Type': 'application/json',
                 'ACCEPT': 'application/json, text/html'})

            if send_data(http_req):
                objects_added += 1
        else:
            print 'Ouch!'
    print '    >>> Added %s standard offers' % objects_added


def get_company(company_cid):
    api_url = URL + API + 'company' + CONF + '&limit=0'
    http_req = urllib2.Request(api_url,
        headers={'ACCEPT': 'application/json, text/html'})
    try:
        resp = urllib2.urlopen(http_req)
        contents = resp.read()
        data = json.loads(contents)
        companies = data['objects']

        for company in companies:
            if company['cid'] == company_cid:
                return company
        return None
    except urllib2.HTTPError, error:
        print error.getcode()
        print error


def send_data(http_req):
    try:
        response = urllib2.urlopen(http_req)

        if 201 == response.getcode():
            return True
        else:
            return False

        #print response.read()
        #print response.getcode()
        #print response.info()
        #print response.msg
    except Exception:
        return False
    """
    except urllib2.HTTPError as he:
        print he.getcode()
        print he.info()
        print he.msg
    except urllib2.URLError as ue:
        print ue
    """


if __name__ == "__main__":
    main()
