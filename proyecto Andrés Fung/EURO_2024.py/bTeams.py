import requests
import json
from API import Equipos

def get_team(team_name_info):
    teams_names = {team["name"]: team["code"] for team in Equipos.teams_data}
        
    team_code = teams_names.get(team_name_info, None)
    if team_code is None:
        print(f"No se encontró el equipo '{team_name_info}'")
        return []

    teams = []
    for team in Equipos.teams_data:
        if team["code"] == team_code:
            teams_info = {
                "name": team["name"],
                "code": team["code"],
                "group": team["group"],
                "id": team["id"]
            }
            teams.append(teams_info)
    return teams
        
team_names_show = {team["name"] for team in Equipos.teams_data}
print("****EQUIPOS QUE PARTICIPAN EN LA EURO 2024****")
print("")
print(team_names_show)
print("")
team_name = input("Ingrese el nombre del país para ver su información:  ")

team_response = get_team(team_name)
if team_response:
    
    for team_info in team_response:
            team = Equipos(team_info['name'], team_info['code'] , team_info['group'], team_info['id'])
            print(team)
        
            
                
