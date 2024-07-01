from API import Estadios
from API import Restaurantes
from API import Productos
def restaurants_per_stadium():
    for stadium in Estadios.stadium_data:
        print(f"Estadio: {stadium['name']}")
        print("Restaurantes:")
        for restaurant in stadium["restaurants"]:
            print(f"- {restaurant['name']}")
        print("")

restaurants_per_stadium()

def get_restaurants(restaurant_name):
    for restaurant in Restaurantes.stadium_data:
            if restaurant["name"] == restaurant_name:
                return [Restaurantes(
                    restaurant["name"],
                )]
        
    print(f"No se encontró el restaurante '{restaurant_name}'")
    return []



#Función para que el usuario escoga un estadio y vea sus atributos
def get_stadium():
    stadiums_names = {stadium["name"]: stadium["id"] for stadium in Estadios.stadium_data}
    stadiums_id = {stadium["id"]: stadium["name"] for stadium in Estadios.stadium_data}

    stadiums = []
    for stadium in Estadios.stadium_data:
            stadium_info = {
                "name": stadium["name"],
                "city": stadium["city"],
                "capacity": stadium["capacity"],
                "id": stadium["id"],
                "restaurants": stadium["restaurants"]
            }
            stadiums.append(stadium_info)
    return stadiums


stadium_names_show = {stadium["name"]: stadium["id"] for stadium in Estadios.stadium_data}
print("****ESTADIOS QUE PARTICIPAN EN LA EURO 2024****")
print("")
print(stadium_names_show)
print("")
stadium_name = input("Ingrese el nombre o ID del estadio para ver su información:  ")

stadium_response = get_stadium(stadium_name)
if stadium_response:
    for stadium_info in stadium_response:
        stadium = Estadios(stadium_info['name'], stadium_info['city'], stadium_info['capacity'], stadium_info['id'])
        print(stadium)
        print("")

        restaurants = len(stadium_info["restaurants"])
        print("Número de restaurantes:", restaurants)
        print("")
        print("Restaurantes:")
        print("")
        for i in range(restaurants):
            print(stadium_info["restaurants"][i]["name"])
            print("Productos:", stadium_info["restaurants"][i]["products"])
            print("")