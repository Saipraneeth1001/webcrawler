from urllib.parse import urlparse


# to get the original domain name we want to crawl ..
def get_domain_name(url):
    try:
        results = get_subdomain_name(url).split('.')
        return results[-3] + '.' + results[-2] + '.' + results[-1]
    except:
        return ''


def get_subdomain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


