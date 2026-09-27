import re
import tldextract
from urllib.parse import urlparse

SHORTENERS = ['bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly']

def having_ip_address(url):
    host = urlparse(url).hostname or ''
    return 1 if re.match(r'^\d{1,3}(\.\d{1,3}){3}$', host) else -1

def url_length(url):
    n = len(url)
    if n < 54:
        return -1
    if n <= 75:
        return 0
    return 1

def shortining_service(url):
    host = urlparse(url).hostname or ''
    return 1 if host in SHORTENERS else -1

def having_at_symbol(url):
    return 1 if '@' in url else -1

def double_slash_redirecting(url):
    return 1 if url.rfind('//') > 7 else -1

def prefix_suffix(url):
    domain = tldextract.extract(url).domain
    return 1 if '-' in domain else -1

def having_sub_domain(url):
    sub = tldextract.extract(url).subdomain
    if sub in ('', 'www'):
        return -1
    labels = sub.split('.')
    if len(labels) == 1:
        return -1
    if len(labels) == 2:
        return 0
    return 1

def sslfinal_state(url):
    return -1 if urlparse(url).scheme == 'https' else 1

def extract_domain_features(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return {
        'having_IP_Address': having_ip_address(url),
        'URL_Length': url_length(url),
        'Shortining_Service': shortining_service(url),
        'having_At_Symbol': having_at_symbol(url),
        'double_slash_redirecting': double_slash_redirecting(url),
        'Prefix_Suffix': prefix_suffix(url),
        'having_Sub_Domain': having_sub_domain(url),
        'SSLfinal_State': sslfinal_state(url)
    }
