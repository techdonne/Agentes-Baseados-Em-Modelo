import requests
import json

class ModelBasedAgent:
    def __init__(self, temperature, condition):
        self.temperature = temperature
        self.condition = condition

    def decide(self):
        #Condição de decisão do agente
        if self.temperature > 21 and self.condition == "Poucas nuvens":
            return "Go to Gym"
        else:
            return "Stay at home"


# Função para simular o ambiente, retornando a temperatura e o tempo
def simulate_enviroment(): 
    #Utilizando API de condições climáticas
    iToken = '83f346792f579c2ff63601e28c94687b'

    iCity = "São Luís"
    iState = "MA"

    iURL = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+ str(iCity) +"&state="+ str(iState) +"&token="+iToken
    iResponse = requests.request("GET", iURL)
    iReturnReq = json.loads(iResponse.text)

    for iKey in iReturnReq:
        iSearchedCity = iKey["name"]
        if iSearchedCity == iCity:
            iId = iKey["id"]
            break

    iURL = "http://apiadvisor.climatempo.com.br/api-manager/user-token/"+ str(iToken) +"/locales"
    payload = "localeId[]=" + str(iId)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    iResponse = requests.request("PUT", iURL, headers=headers, data=payload)

    iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" +str(iId) + "/current?token=" + iToken

    iResponse = requests.request("GET", iURL)
    iReturnReq = json.loads(iResponse.text)

    temperature = iReturnReq["data"]["temperature"]
    condition = iReturnReq["data"]["condition"]
    return temperature, condition


# Função principal
def main():
    temperature, condition = simulate_enviroment()
    agent = ModelBasedAgent(temperature, condition)
    decision = agent.decide()
    print("Agents decision:", decision)


if __name__ == "__main__":
    main()