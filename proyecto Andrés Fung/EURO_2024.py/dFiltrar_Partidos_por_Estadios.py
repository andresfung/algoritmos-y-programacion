from API import Equipos
from API import Partido
from API import Estadios




def get_matches_by_stadium(stadium_name_or_id):
    team_codes = {team["code"]: team["name"] for team in Equipos.teams_data}
    global team_names
    team_names = {team["name"]: team["code"] for team in Equipos.teams_data}
    global stadium_names
    stadium_names = {stadium["name"]: stadium["id"] for stadium in Estadios.stadium_data}
    global stadium_ids
    stadium_ids = {stadium["id"]: stadium["name"] for stadium in Estadios.stadium_data}

    stadium_id = None
    if stadium_name_or_id in stadium_names: 
        #Si se utiliza el nombre del estadio
        stadium_id = stadium_names[stadium_name_or_id]
    else: 
        #Si se utiliza el ID del estadio
        for stadium in Estadios.stadium_data:
            if stadium["id"] == stadium_name_or_id:
                stadium_id = stadium["id"]
                break

    if stadium_id is None:
        return []

    matches = []
    for match in Partido.matches_data:
        if match["stadium_id"] == stadium_id:
            match_info = {
                "number": match["number"],
                "home_team": team_codes[match["home"]["code"]],
                "away_team": team_codes[match["away"]["code"]],
                "date": match["date"],
                "group": match["group"]
            }
            matches.append(match_info)
    return matches

# Pedir al usuario que ingrese el nombre o ID del estadio
print("***ESTADIOS EN LOS QUE SE JUGARA LA EURO 2024***")
print(stadium_names)
print("")
stadium_identifier = input("Ingrese el nombre o ID del estadio: ")

# Obtener los partidos del estadio y mostrarlos
stadium_matches = get_matches_by_stadium(stadium_identifier)
if stadium_matches:
    stadium_name = stadium_ids.get(stadium_identifier, stadium_identifier)
    print(f"Partidos en el estadio '{stadium_name}':")
    for match in stadium_matches:
        print(f"Partido N°{match['number']} ----- (Casa) {match['home_team']} vs {match['away_team']} (Visitante) ----- Fecha: {match['date']} --- {match['group']}")
else:
    print(f"No se encontraron partidos para el estadio '{stadium_identifier}'.")