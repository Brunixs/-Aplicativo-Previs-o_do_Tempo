from kivy.app import App 
from kivy.lang import Builder
import requests

GUI = Builder.load_file("display.kv")

class Aplicativo(App):
    def build(self):
        return GUI
    
    def on_start(self):
        estado = self.pesq_estado()
        temp = self.pegar_temp(estado)
        self.root.ids[estado].text = f"Temperatura: {temp}ºC"

    def pegar_temp(self, estado):
        API_key = "c57cb8f4565c5cc240bf80c8aabc79f3"
        link = f"http://api.openweathermap.org/data/2.5/weather?q={estado},br&appid={API_key}&units=metric"
        requisicao =  requests.get(link)
        dic_requisicao = requisicao.json()
        temp = dic_requisicao['main']['temp']
        return temp

    def pesq_estado(self):
        pesquisar = input("Digite um estado(BR):")
        return pesquisar

Aplicativo().run()
