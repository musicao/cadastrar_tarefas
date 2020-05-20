from bs4 import BeautifulSoup

def get_javax_faces_view_state(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        viewState = soup.find("input", {"id": "javax.faces.ViewState"}).get('value')

        if not viewState:
            raise Exception("Erro ao obter ViewState")

        return viewState
    except:
        raise Exception("Erro ao obter JavaxFacesViewState")


