
import logging
from datetime import datetime

from GetTarefas import GetTarefas
from repositories import mongoRepository

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler('{:%Y-%m-%d}.log'.format(datetime.now())),
            logging.StreamHandler()
        ])


def logar(identificador,senha,acesso):

    return GetTarefas(identificador,senha,acesso)



def cadastrar():

    try:
        identificador = '00457766107'
        senha = 'dataprev'
        acesso = 'homologacao'
        descending = True

        filter = {"resumo": {"$exists": False}}

        if descending:
            order = {'field': 'XXXX', 'direction': 1}
        else:
            order = {'field': 'XXXX', 'direction': -1}

        collection = 'migracao'

        itens = mongoRepository.count_documents(collection, filter)

        if itens:

            get_gestao = logar(identificador, senha,acesso)


            for item in mongoRepository.find(collection, filter, **order):

                try:

                    protocolo = item['PROTOCOLO']
                    logging.info('abrindo tarefa: ' + str(protocolo))

                    criarTarefa = get_gestao.criarTarefa()

                    tarefa = {'Resultado': 'Da tentativa de castro'}

                    filter = {"PROTOCOLO": protocolo}
                    retorno = mongoRepository.findOneAndReplace(collection, filter, tarefa)
                    print(retorno)

                    print('tarefa atualizada' + str(protocolo))

                except Exception as e:
                    'Persistir falha no banco em caso de insucesso'
                    print("pega proxima - aqui deu falha" + e.__str__())



            get_gestao.logout()
            print('fim')
        else:
            logging.info('não tem tarefas pra cadastrar')


    except Exception as e:
        print(e)
        get_gestao.logout()

if __name__ == '__main__':
    cadastrar()