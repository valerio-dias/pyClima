import requests
import json
from turtle import Turtle, Screen

t = Turtle()
t.hideturtle()
screen = Screen()



def tela(r, g, b, temperatura, condicao, sensacao, min, max):
    screen.setup(width=400, height=200)
    screen.bgcolor(r/255, g/255,b/255)
    screen.title('Clima')
    screen.tracer(0)
    t.clear()
    t.goto(100, 0)
    t.color('Green')
    t.clear()
    t.write(temperatura, align='center', font=('Roboto', 30, 'normal'))
    t.goto(-100, 0)
    t.color('Green')
    t.write(condicao, align='center', font=('Roboto', 15, 'normal'))
    t.goto(-100, 30)
    t.color('Green')
    t.write(cidade, align='center', font=('Roboto', 15, 'normal'))
    t.goto(-100, -30)
    t.color('Green')
    t.write(sensacao, align='center', font=('Roboto', 7, 'normal'))
    t.goto(60, -30)
    t.color('Green')
    t.write(min, align='center', font=('Roboto', 7, 'normal'))
    t.goto(120, -30)
    t.color('Green')
    t.write(max, align='center', font=('Roboto', 7, 'normal'))
    t.goto(0, -70)
    t.color('Green')
    t.write('Clique na tela para sair.', align='center', font=('Comic Sans MS', 7, 'normal'))



def update_tela():
    t.clear()
    t.penup()
    t.goto(0, 0)

cidade= ''
temperatura = ' '
condicao = ' '
sensacao = ' '
min = ' '
max = ' '
tela(0, 0, 0, temperatura, condicao, sensacao, min, max)

cidade = screen.textinput(title="Cidade", prompt="Qual sua cidade? ")

update_tela()
key_w = # Criar chave em http://https://openweathermap.org/ e inserir entre aspas.
clima = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' +cidade+ '&appid='+key_w+  '')
tempo = json.loads(clima.text)
grau = round(float(tempo['main']['temp']- 273.15))
grau_s = round(float(tempo['main']['feels_like']- 273.15))
grau_min = round(float(tempo['main']['temp_min']- 273.15))
grau_max = round(float(tempo['main']['temp_max']- 273.15))
temperatura = f'{grau}º'
sensacao = f'Sensação térmica: {grau_s}º'
min = f'Min: {grau_min}º'
max = f'Max: {grau_max}º'
condicao = tempo['weather'][0]['main']
cidade = tempo['name']
tela(0, 0, 0, temperatura, condicao, sensacao, min, max)


screen.exitonclick()
