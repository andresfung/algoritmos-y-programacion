import requests
import json


class Equipos:
    url_teams = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    teams_info = requests.get(url_teams)
    if teams_info.status_code == 200:
        teams_data = json.loads(teams_info.content)
        
    def __init__(self, name, code, group, id):
        self.name = name
        self.code = code
        self.group = group
        self.id = id
    
    def __str__(self):
        return (f"Nombre: {self.name}, Código: {self.code}, Grupo: {self.group}, ID: {self.id}")
    

class Estadios:
    url_stadiums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    stadiums_info = requests.get(url_stadiums)
    if stadiums_info.status_code == 200:
        stadium_data = json.loads(stadiums_info.content)

    def __init__(self, name, city, capacity, id,):
        self.name = name
        self.city = city
        self.capacity = capacity
        self.id = id
        
    def __str__(self):
        return f"Nombre: {self.name}, Ciudad: {self.city}, Capacidad: {self.capacity}, ID: {self.id}"
    
class Restaurantes:
    url_stadiums = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
    stadiums_info = requests.get(url_stadiums)
    if stadiums_info.status_code == 200:
        stadium_data = json.loads(stadiums_info.content)

    def __init__(self, name, products):
        self.name = name
        self.products = products
    def __str__(self):
        return (f"Nombre: {self.name}, Productos: {self.products}")
        

class Productos(Restaurantes):
    def __init__(self, product_name, quantity, price, stock, aditional_info):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.aditional_info = aditional_info

    def __str__(self):
        return (f"Nombre: {self.product_name}, Cantidad: {self.quantity}, Precio: {self.price}, Stock: {self.stock}, Info adiconal: {self.aditional_info}")


class Partido:
    url_matches = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
    matches_info = requests.get(url_matches)
    if matches_info.status_code == 200:
        matches_data = json.loads(matches_info.content)

    def __init__(self, number, home, away, date, group, id, stadium_id):
        self.number = number
        self.home = home
        self.away = away
        self.date = date
        self.group = group
        self.id = id
        self.stadium_id = stadium_id

    def __str__(self):
        return (f"Partido N°: {self.number} -- {self.home['name']} vs {self.away['name']} -- Fecha: {self.date} -- {self.group} -- ID del Partido: {self.id}, ID del Estadio: {self.stadium_id}")
