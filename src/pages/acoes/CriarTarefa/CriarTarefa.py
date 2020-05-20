import re

from modules.utils import limpar
from pages.services import RequestService

from src.pages.services.getDTPINFRA_TOKEN import \
    get_dtpinfra_token as dtpinfra_token
from src.pages.services.getViewState import \
    get_javax_faces_view_state as javax_faces_view_state


class CriarTarefa():

    def __init__(self,sessao):
        self.sessao = sessao
        self.url = self.sessao.url_raiz + '/pages/detalhar/criarTarefa.xhtml'

        r = RequestService.get(self.sessao, self.url)
        print(r.text)

        isPaginaEsperada = re.search('span> Dados básicos',limpar(r.text))

        if isPaginaEsperada:

            self.sessao.dtp_infra_token = dtpinfra_token(r.text)
            self.sessao.view_state = javax_faces_view_state(r.text)
          
        else:
            raise Exception("Erro ao carregar tela de criação da tarefa")

