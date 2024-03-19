import requests


def get_weather_from_api(api_key, city): #conecta com a API
    base_url = "http://api.openweathermap.org/data/2.5/weather?" #url para conexão com a API
    complete_url = f"{base_url}appid={api_key}&q={city}" #recebe a chave da API para acesso do clima da cidade
    response = requests.get(complete_url)
    
    response = requests.get(complete_url) #criar request para o servidor passar a url
    
    return response.json() # retorna a resposta da API em formato estruturado de chave valor

def get_weather(city_name): #chama o programa principal
    """
        Filtrar os dados climáticos de uma cidade
     :param city_name:
     :return:
    """
    api_key = #Insira aqui a chave da API do site OpenWeatherMap
    weather_data = get_weather_from_api(api_key, city_name)
    
    if weather_data["cod"] == 401: #caso haja algum problema de request, executa o bloco de código abaixo
        print('Problema com a requisição!\n'
          f'Mensagem: {weather_data['message']}')
    elif weather_data["cod"] != 404:
        main_weather = weather_data["weather"][0]["main"]
        temperature = weather_data["main"]["temp"]
    
        print(f"Clima em {city_name}: {main_weather}")
        print(f"Temperatura: {temperature- 273.15:.2f}°C") #ponto decimal para converter farenheit para celsius
    else:
        print("Cidade não encontrada!")
    