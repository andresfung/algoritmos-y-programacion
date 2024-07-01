from API import Partido

#Funcion que devuelve todos los partidos
def matches():
    for match in Partido.matches_data:
            number = match["number"]
            home = match["home"]["name"]
            away = match["away"]["name"]
            date = match["date"]
            group = match["group"]
            id = match["id"]
            stadium_id = match["stadium_id"]
            
            print("")
            print(f"Partido N°: {number} -- (Casa) {home} vs {away} (Visitante) -- Fecha: {date} -- {group} -- ID partido {id} -- ID estadio {stadium_id} ")



#Funcion que devuelve los datos de un partido, el cual escoge el usuario
def get_matches(match_number_info):
    for match in Partido.matches_data:
        if match["number"] == match_number_info:
            return [Partido(
                match["number"],
                match["home"],
                match["away"],
                match["date"],
                match["group"],
                match["id"],
                match["stadium_id"]
            )]
    
    print(f"No se encontró el partido N° '{match_number_info}'")
    return []

print("Se jugaran 36 partidos en la fase de grupos de la EURO 2024")
matches()

match_choice = input("ELIGE")

matches = get_matches(int(match_choice))
if matches:
    for match in matches:
        print(match)
        print("")


