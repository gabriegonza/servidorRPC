import rpyc # biblioteca para Python RPC
from rpyc.utils.server import ThreadedServer 

class MyService(rpyc.Service):
    def exposed_IMC(self, peso, altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            mensagem = "Abaixo do peso"
        elif imc < 24.9:
            mensagem = "Peso normal"
        elif imc < 29.9:
            mensagem = "Sobrepeso"
        elif imc < 34.9:
            mensagem = "Obesidade Grau 1"
        elif imc < 39.9:
            mensagem = "Obesidade Grau 2"
        else:
            mensagem = "Obesidade Grau 3"
        
        print("Usaram a função de IMC")
        return imc, mensagem

    def exposed_Calcula_Equacao_Segundo_Grau(self, a, b, c):
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            return x1, x2
        elif delta == 0:
            x1 = x2 = -b / (2*a)
            return x1
        else:
            return "Nao existem raizes reais com esses valores"

    def exposed_Verifica_Palindromo(self, palavra):
        palavra = palavra.lower().replace(" ", "")
        if palavra == palavra[::-1]:
            return "A palavra " + palavra +" e um palindromo. " 
        else:
            return "A palavra " + palavra + " nao e um palindromo." 

if __name__ == "__main__":
    server = ThreadedServer(MyService, hostname='localhost', port = 8000)
    print('Servidor online')
    server.start()