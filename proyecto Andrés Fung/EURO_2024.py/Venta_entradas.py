import Mapa_Estadio
import cdMatches
import Numero_vampiro
from API import Estadios
from API import Partido
from API import Restaurantes
import random
import string



class Cliente:
    def __init__(self, name, age, ci):
        self.name = name
        self.age = age
        self.ci = ci

class Entrada(Cliente):
    def __init__(self, name, age, ci, ticket_type, selected_seat, ticket_price, id_ticket):
        super().__init__(name)
        super().__init__(age)
        super().__init__(ci)
        self.ticket_type = ticket_type
        self.selected_seat = Mapa_Estadio.selected_seat
        self.ticket_price = ticket_price
        self.id_ticket = id_ticket   
     
#Venta de entradas para el ususario
def Ticket_sale():
    # Toma los datos del cliente
    def client():
        while True:
            global client_name
            client_name = input("Ingrese su nombre: ")
            if client_name.isdigit() or not isinstance(client_name , str):
                print("Por favor ingrese un nombre utilizando unicamente letras")
            else:
                Cliente.name = client_name
                break
                    
        while True: 
            global client_age     
            client_age = input("Ingrese su edad en numeros: ")
            if not client_age.isdigit or int(client_age) <= 0  or int(client_age) > 100:
                print("Por favor ingrese una edad valida utilizando unicamente letras")
            else:
                Cliente.age = client_age
                break
        
        while True:
            global client_ci
            client_ci = input("Ingrese su cedula de identidad: ")
            if not client_ci.isdigit or 6 > len(client_ci) < 8:
                print("Por favor ingrese una cedula valida usando unicamente numeros")
            else:
                Cliente.ci = client_ci
                break

        return (Cliente.name , Cliente.age , Cliente.ci)

    # Le muestra al usuario todos los partidos disponibles para comprar
    def show_matches():
        print("***PARTIDOS QUE SE JUGARAN EN LA EURO 2024***\n")
        cdMatches.matches()
        are_you_sure = False
        while are_you_sure == False:
            print("")
            global match_choice
            match_choice = input("Escriba el numero del partido al cual desea asistir: ")
            matches = cdMatches.get_matches(int(match_choice))
            if matches:
                for match in matches:
                    Partido.number = match_choice
                    print(match)
                    print("")
                decision = input("Esta seguro que desea comprar entradas para este partido?: ").lower()
                if decision == "si":
                    print("Excelente!")
                    print("")
                    are_you_sure = True
                    break
                elif decision == "no":
                    print("De acuerdo")
                    print("")
                else:
                    print("Escriba una opcion valida")
                    print("")
            else:
                print("Por favor ingrese un numero de partido valido")
                print("")
            
    # El usuario podra comprar una entrada normal o una vip
    def normal_or_vip():
        are_you_sure = False
        while are_you_sure == False:
            global ticket_type 
            ticket_type = input("Que tipo de entrada desea comprar (normal o VIP): ").lower()
            print("")
            if ticket_type == "normal":
                print("Si compra una entrada normal solo podrá ver el partido en su asiento")
                print("")
                decision = input("Si desea confirmar escriba si, y para volver atras escriba no: ").lower()
                if decision == "si":
                    Entrada.ticket_type = ticket_type
                    are_you_sure = True
                    print("De acuerdo!")
                    print("")
                    break 
                elif decision == "no":
                    print("De acuerdo")
                    print("")
                else:
                    print("Escriba una opcion valida")
                    print("")

            elif  ticket_type == "vip":
                print("Si compra una entrada VIP podrá disfrutar del restaurante del estadio, es decir podrá adquirir productos de dicho restaurante")
                print("")
                decision = input("Si desea confirmar escriba si, y para volver atras escriba no: ").lower()
                if decision == "si":
                    Entrada.ticket_type = ticket_type
                    are_you_sure = True
                    print("De acuerdo!")
                    print("")
                    are_you_sure = True
                elif decision == "no":
                    print("De acuerdo")
                    print("")
                else:
                    print("Escriba una opcion valida")
                    print("")

        
    # El precio de la entra mas IVA y menos el descuento de vampiro si la cedula del usuario es un numero vampiro
    def ticket_price_IVA_vampire():
        global ticket_type
        global client_ci
        global ticket_price
        if ticket_type == "normal":
            vampire = Numero_vampiro.is_vampire_number(int(client_ci))
            if vampire == True:
                print(f"Felicitaciones, su cedula: {client_ci} es un numero vampiro, usted tendrá un 50% de descuento en su entrada")
                discount = 35 * 0.5
                discount_price = 35 - discount
                iva = discount_price * 0.16 
                ticket_price = discount_price + iva
            else:
                print(f"Su cedula: {client_ci} no es un numero vampiro :(")
                print(Numero_vampiro.is_vampire_number(int(client_ci)))
                iva = 35 * 0.16
                ticket_price = 35 + iva
        
        else:
            vampire = Numero_vampiro.is_vampire_number(int(client_ci))
            if vampire == True:
                print(f"Felicitaciones, su cedula: {client_ci} es un numero vampiro, usted tendrá un 50% de descuento en su entrada")
                discount = 75 * 0.5
                discount_price = 75 - discount
                iva = discount_price * 0.16 
                ticket_price = discount_price + iva
            else: 
                print(f"Su cedula: {client_ci} no es un numero vampiro :(")
                print(Numero_vampiro.is_vampire_number(int(client_ci)))
                iva = 75 * 0.16
                ticket_price = 75 + iva

        Entrada.ticket_price = ticket_price 
        return (f"el precio de su entrada mas IVA son:  {ticket_price}$")
        
    # Generar una ID aleatoria de 10 dígitos para la entrada
    def ticket_id(length=10):
        characters = string.digits
        id = ''.join(random.choice(characters) for i in range(length))
        return id


        


   

    client_info = client()
    if client_info:
        print("Su usuario ha sido registrado exitosamente!")
        print("")

    show_matches()
    print("")

    normal_or_vip()

    Mapa_Estadio.seats()
    print("")

    ticket_price = ticket_price_IVA_vampire()
    print(ticket_price)
    print("")

    global final_response
    print(f"De acuerdo {client_name}, su asiento es el {Mapa_Estadio.selected_seat}, y {ticket_price}")
    final_response = input("Desea continuar con el pago? (si o no) ").lower()
    if final_response == "si":
        print("Gracias por su compra!")
        global id_ticket
        id_ticket = ticket_id()
        print("ID de su entrada:", id_ticket)
        Entrada.id_ticket = id_ticket
        print("")
    elif final_response == "no":
        print("Hasta pronto!")
    else:
        print("Escriba una opcion valida")

    return (Cliente.name , Cliente.age , Cliente.ci, Entrada.ticket_type, Mapa_Estadio.selected_seat, Partido.number, ticket_price, id_ticket)






    