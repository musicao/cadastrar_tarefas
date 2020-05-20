import requests


def post(sessao,url,payload,allow_redirect=True,
         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:56.0) Gecko/20100101 Firefox/56.0'}):

    return sessao.post(
            url,
            data=payload,
            headers = headers,
            allow_redirects=allow_redirect)


def get(sessao,url,allow_redirect=True):

    return sessao.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:56.0) Gecko/20100101 Firefox/56.0'},
            allow_redirects=allow_redirect)