import re


def get_total_records(html):
    try:
        match = re.search(r'totalRecords":(?P<total_records>[0-9]+)',html,re.I|re.M)

        if not match:
            raise Exception("Erro ao obter totalRecords")

        return match.group('total_records')
    except:
        raise Exception("Erro ao obter totalRecords")
