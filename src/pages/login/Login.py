import requests
import re
from bs4 import BeautifulSoup

from modules.utils import limpar
from src.pages.services import RequestService
from src.pages.services.getDTPINFRA_TOKEN import \
    get_dtpinfra_token as dtpinfra_token
from src.pages.services.getViewState import \
    get_javax_faces_view_state as javax_faces_view_state


class Login():

    def __init__(self):

        self.sessao = requests.Session()


        self.url_login_homologacao = "https://hgeridinss.dataprev.gov.br/cas/login?service=http://hsagapr01.prevnet/tarefas"
        self.url_login_externo = "https://geridinss.dataprev.gov.br/cas/login?service=www.tarefas.inss.gov.br"
        self.url_login_interno = "https://geridinss.dataprev.gov.br/cas/login?service=www-tarefas"
        self.url_raiz = ''



#00457766107
#dataprev



    def carregarPaginaDeLogin(self,origem_remoto):

        if origem_remoto == 'homologacao':
            self.url_login = self.url_login_homologacao
            self.sessao.url_index = "http://hsagapr01/tarefas/pages/index.xhtml"


        elif origem_remoto == 'externo':
                self.url_login = self.url_login_externo
                self.sessao.url_index = "http://www.gestaotarefas.inss.gov.br/gestaotarefas/pages/index.xhtml"

        else:
            self.url_login = self.url_login_interno
            self.sessao.url_index = "http://www-tarefas/tarefas/pages/index.xhtml"

        return RequestService.get(self.sessao,  self.url_login )

    def entrar(self, username, password, origem_remoto):

        try:

            retorno = self.carregarPaginaDeLogin(origem_remoto)
            s = self.sessao

            soup = BeautifulSoup(retorno.text, 'html.parser')

            lt = soup.find("input", {"name": "lt"}).get('value')
            execution = soup.find("input", {"name": "execution"}).get('value')

            payload = {"username": username, "password": password, "lt": lt,
                       "execution": execution,
                       "_eventId": "submit", "submit": "Entrar"}

            retorno = RequestService.post(s, self.url_login, payload,
                                               False)

            if retorno.status_code != 302 or retorno.headers._store[
                'location'] in s.headers._store:
                raise ("Falha ao logar no sistema")

            RequestService.get(s, retorno.headers._store['location'][1],True)

            self.sessao.url_raiz = self.sessao.url_index.replace('/pages/index.xhtml','')

            r = RequestService.get(s, self.sessao.url_raiz, True)

            temQueEscolherDominio = re.search(
                    '<legend class="panel-title">Escolha o domínio</legend>',
                    r.text,
                    re.IGNORECASE |
                    re.MULTILINE
            )

            if temQueEscolherDominio:
                domains = "UO:15.001.GEXREC"
                payload = {"domains": domains}

                url = self.sessao.url_raiz + '/pages/comum/domainController.srv'

                r = RequestService.post(self.sessao,url, payload, True)
                r = RequestService.get(self.sessao, self.sessao.url_raiz, True)
                r = RequestService.get(self.sessao,self.sessao.url_index, True)


                tela = limpar(r.text)

                isPaginaEsperada = re.search(
                        'span> Nova Tarefa</a>',
                        tela,
                        re.IGNORECASE |
                        re.MULTILINE
                )

                if isPaginaEsperada:

                    self.sessao.dtp_infra_token = dtpinfra_token(r.text)
                    self.sessao.view_state = javax_faces_view_state(r.text)
                    return self.sessao

                else:
                    raise Exception("Falha ao logar no sistema - Página Inesperada")

            else:
                raise ("Falha ao logar no sistema")


        except:
            self.logado = False
            raise ("Falha ao logar no sistema")

