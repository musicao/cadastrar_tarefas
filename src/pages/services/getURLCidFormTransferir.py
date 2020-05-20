from bs4 import BeautifulSoup

def get_url_cid_form_transferir(html):
    try:
        soup = BeautifulSoup(html, 'xml')

        form = soup.find('update',{"id":"formTransferir"}).text

        soup = BeautifulSoup(form, 'html.parser')
        url_cid = soup.find("form", {"id": "formTransferir"}).get('action')

        if not url_cid:
            raise Exception("Erro ao obter url_cid")

        return url_cid
    except:
        raise Exception("Erro ao obter url_cid")
