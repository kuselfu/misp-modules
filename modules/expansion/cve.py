import json
import requests

misperrors = {'error': 'Error'}
mispattributes = {'input': ['vulnerability'], 'output': ['']}
moduleinfo = {'version': '0.1', 'author': 'Alexandre Dulaunoy', 'description': 'An expansion hover module to expand information about CVE id.', 'module-type': 'hover'}
moduleconfig = []
cveapi_url = 'https://cve.circl.lu/api/cve/'


def handler(q=False):
    if q is False:
        return False
    print (q)
    request = json.loads(q)
    if not request.get('vulnerability'):
        misperrors['error'] = 'Vulnerability id missing'
        return misperrors

    r = requests.get(cveapi_url+request.get('vulnerability'))
    if r.status_code == 200:
        vulnerability = json.loads(r.text)
    else:
        misperrors['error'] = 'cve.circl.lu API not accessible'
        return misperrors['error']

    return vulnerability


def introspection():
    return mispattributes


def version():
    moduleinfo['config'] = moduleconfig
    return moduleinfo
