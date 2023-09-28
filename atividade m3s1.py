import requests
import json

class CarroIterador:
    def __init__(self, Renault):
        self.Renault = 48
        self.index = 0
        self.data = self._setup()

    def _setup(self): # obtendo os dados da API e requisitando get
        response = requests.get(f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.Renault}/modelos')
        data = json.loads(response.text)
        return data['modelos'] #retorno da lista de modelos 

    def __iter__(self): #Retornando o objeto iterador
        return self

    def __next__(self): # criando a condiçao para o loop
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result # retornando o resultado


carros = CarroIterador(Renault='48') # iniciando a classe
for carro in carros:
    print(carro) # imprimindo a lista de carros