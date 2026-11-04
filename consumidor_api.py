import requests 
from pprint import pprint

def consultar_clima():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=apparent_temperature,temperature_2m,relative_humidity_2m"

    
    resposta = requests.get(url)#busca os dados da URL (requisição HTTP)

    if resposta.status_code == 200:
        resposta.raise_for_status()
        dados = resposta.json()
        '''condicoes_atuais = dados["current"]
        return {
            "temperatura": condicoes_atuais["temperature_2m"],
            "umidade": condicoes_atuais["relative_humidity_2m"],
            "sensacao_termica": condicoes_atuais["apparent_temperature"],
            "precipitacao": condicoes_atuais["precipitation"],
            "veto": condicoes_atuais["wind_speed_10m"],
            "horario": condicoes_atuais["time"],
            }'''
        pprint(dados) #mostra os dados no terminal
        

    else:
        print("Erro ao consultar API...") #informa se houve falha na consulta
consultar_clima()



