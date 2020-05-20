import logging


from pages.acoes.CriarTarefa.CriarTarefa import CriarTarefa
from pages.login.Login import Login
from pages.services import RequestService


class GetTarefas():

    def __init__(self,username,password,acesso_remoto):

        try:
            logging.info("Logando")
            self.logar(username, password,acesso_remoto)

        except Exception as e:
            logging.error("erro ao acessar: " + e.__str__())
            raise ('Impossível acessar')

    def criarTarefa(self):
        return CriarTarefa(self.sessao)



    def logar(self,username,password,acesso_remoto):
        login = Login()
        self.sessao = login.entrar(username,password,acesso_remoto)


    def logout(self):
        RequestService.get(self.sessao, 'https://geridinss.dataprev.gov.br/cas/logout', True)


