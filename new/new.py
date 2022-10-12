from config import API_KEY, endpoint, country, ativo


API_URL = NewsApiClient(None)

class New:
    def __init__(self, API_KEY, endpoint, country, ativo):
        self.API_KEY = API_KEY
        self.endpoint = endpoint
        self.country = country
        self.ativo = ativo
        
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")

if __name__ == "__main__":
    new = New(True)
    new.desativar()
