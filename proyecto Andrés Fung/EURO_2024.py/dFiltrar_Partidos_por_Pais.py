from API import Equipos
from API import Partido

   


def get_matches_by_country(country_name_info):
     # Crear un diccionario para mapear los códigos de los equipos a sus nombres
    team_codes = {team["code"]: team["name"] for team in Equipos.teams_data}
    team_names = {team["name"]: team["code"] for team in Equipos.teams_data}
    global team_names_show
    team_names_show = {team["name"] for team in Equipos.teams_data}
        
        
        
    country_code = team_names.get(country_name_info, None)
    if country_code is None:
        return []
    else:
        matches = []
        for match in Partido.matches_data:
            if match["home"]["code"] == country_code or match["away"]["code"] == country_code:
                match_info = {
                    "number": match["number"],
                    "home_team": team_codes[match["home"]["code"]],
                    "away_team": team_codes[match["away"]["code"]],
                    "date": match["date"],
                    "group": match["group"],
                    "stadium_id": match["stadium_id"]
                }
                matches.append(match_info)
        return matches

    # Pedir al usuario que ingrese el nombre del país
print("****EQUIPOS QUE PARTICIPAN EN LA EURO 2024****")
print("")
print(team_names_show)
print("")
country_name = input("Ingrese el nombre del país para ver sus partidos:  ")
    
    # Obtener los partidos del país y mostrarlos
country_matches = get_matches_by_country(country_name)
if country_matches:
    print("Partidos de", country_name+":")
    print("")
    for match in country_matches:
        print(f"Partido N°{match['number']}: {match['home_team']} contra {match['away_team']} ---  Fecha: {match['date']} --- Grupo: {match['group']} --- Estadio: {match['stadium_id']}")
else:
        print(f"No se encontraron partidos para el país '{country_name}'.")


get_matches_by_country()