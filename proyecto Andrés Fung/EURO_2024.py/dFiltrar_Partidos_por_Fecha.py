from API import Equipos
from API import Partido

   

#Funcion que devuelve todos los partidos que se jugaran en una fecha especifica
def get_matches_by_date(match_date_info):
     # Crear un diccionario de los códigos a sus nombres
    team_codes = {team["code"]: team["name"] for team in Equipos.teams_data}
    global team_names
    team_names = {team["name"]: team["code"] for team in Equipos.teams_data}
    matches = {match["date"]: match["number"]  for match in Partido.matches_data}
        
        
    match_date = matches.get(match_date_info, None)
    if match_date is None:
        return []
    else:
        matches_info = []
        for match in Partido.matches_data:
            if match["date"] == match_date_info:
                match_info = {
                    "number": match["number"],
                    "home_team": team_codes[match["home"]["code"]],
                    "away_team": team_codes[match["away"]["code"]],
                    "date": match["date"],
                    "group": match["group"],
                    "stadium_id": match["stadium_id"]
                    }
                matches_info.append(match_info)
        return matches_info

    # Pedir al usuario que ingrese el nombre del país

date = input("Ingrese una fecha para poder ver los partidos que se jugaran ese día   (EJEMPLO: 2024-06-15):  ")
    
    # Obtener los partidos del país y mostrarlos
dates_with_matches = get_matches_by_date(date)
if dates_with_matches:
    print("Partidos del", date+":")
    print("")
    for match in dates_with_matches:
        print(f"Partido N°{match['number']} ----- {match['home_team']} vs {match['away_team']} -----  Fecha: {match['date']} --- {match['group']} --- Estadio: {match['stadium_id']}")
else:
        print(f"No se encontraron partidos para el país '{date}'.")