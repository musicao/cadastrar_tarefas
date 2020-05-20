from bs4 import BeautifulSoup
import re



def carregouFormResponsavel(pagina):
    soup = BeautifulSoup(pagina, 'xml')

    resposta =  soup.find('update', {"id": "formResponsavel:tableResponsavel"})

    return resposta.text if resposta else False


def temRegistro(pagina):
    try:

        motivo = None
        data_inicio = None
        data_fim = None
        data_rk = None



        soup = BeautifulSoup(pagina, 'xml')

        form = soup.find('update',{"id":"formResponsavel:tableResponsavel"}).text

        sem_registro = re.search('(?P<mensgem>Nenhum registro encontrado)', form)

        if sem_registro:
            return {"error" : True,
                    "motivo":'Nenhum registro encontrado ou usuário não atende esse serviço',
                    "vs": None,
                    "siape": None,
                    "data_rk": None,
                    "data_incio": None,
                    "data_fim": None

                    }

        else:


            trs = re.findall('\[CDATA\[(.*?)\]\]', pagina)

            dados_servidor = re.search('<td role=\"gridcell\">([0-9]+)</td><td role=\"gridcell\">('
                                       '.*?)</td>', trs[0])
            if not dados_servidor:
                raise Exception('Erro ao obter dados do servidor')
            else:
                siape = dados_servidor.groups()[0]
                nome = dados_servidor.groups()[1]

                data_rk = re.search('data-rk=\"(?P<rk>[0-9]*)',trs[0])
                if not data_rk:
                    raise Exception("Erro ao obter rk")
                else:
                    data_rk = data_rk.group('rk')

                tem_afastamento = re.search('[^-]*- (?P<texto>[^<]*)',nome)
                if tem_afastamento:
                    afastamento = re.search('([a-zA-Z\(\)]*) (?:DE ([0-9/]*) ATÉ ([0-9/]*))?',
                                            tem_afastamento.group('texto'))

                    motivo = afastamento.groups()[0]
                    data_inicio = afastamento.groups()[1]
                    data_fim = afastamento.groups()[2]


            return {"vs" : trs[2],
                    "siape":siape,
                    "data_rk": data_rk,
                    "motivo": motivo,
                    "data_incio":  data_inicio,
                    "data_fim": data_fim
                    }




    except:
        raise Exception("Erro ao obter formResponsavel")


def get_dtpinfra_token_responsavel(html):
    try:
        soup = BeautifulSoup(html, 'xml')
        form = soup.find('update', {"id": "formDetalharTarefa"}).text
        soup = BeautifulSoup(form, 'html.parser')

        DTPINFRA_TOKEN = soup.find("input",
                                   {"name": "DTPINFRA_TOKEN"}).get(
                'value')

        if not DTPINFRA_TOKEN:
            raise Exception("Erro ao obter DTPINFRA_TOKEN")

        return DTPINFRA_TOKEN
    except:
        raise Exception("Erro ao obter DTPINFRA_TOKEN")



def retorno_gravacao(pagina):

    soup = BeautifulSoup(pagina, 'xml')

    mensagem = soup.find('update', {"id": "mMensagens"}).text

    tem_erro = re.search(
                '<span class=\"ui-messages-error-summary\">(?P<mensagem>.*?)<\/span>',
                mensagem, re.IGNORECASE | re.MULTILINE
        )

    sucesso = re.search(
                '<span class=\"ui-messages-info-summary\">(?P<mensagem>.*?)<\/span>',
                mensagem, re.IGNORECASE | re.MULTILINE
        )

    detail = re.search(
                '<span class=\"ui-messages-info-detail\">(?P<mensagem>.*?)<\/span>',
                mensagem, re.IGNORECASE | re.MULTILINE
        )

    if tem_erro and detail:

        if tem_erro:
            mens = tem_erro.group('mensagem')

        if detail:
            mens = detail.group('mensagem')

        return { "error" : True, "motivo" : mens}

    else:
        mens = sucesso.group('mensagem')
        return {"error": False, "motivo": mens}
