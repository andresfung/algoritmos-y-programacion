import Venta_entradas 
from Venta_entradas import Cliente
from Venta_entradas import Entrada
from API import Partido
from API import Estadios
from API import Restaurantes


def register_sale(client_name, client_age, client_Ci, ticket_type, selected_seat, match_choice, ticket_price, id_ticket):
    
    
    # Save client information to a text file
    with open('datos_Entrada.txt', 'a') as file:
            file.write(f"Nombre: {client_name}\n")
            file.write(f"Edad: {client_age}\n")
            file.write(f"Cedula de Identidad: {client_Ci}\n")
            file.write(f"Tipo de Entrada: {ticket_type}\n")
            file.write(f"Asiento Seleccionado: {selected_seat}\n")
            file.write(f"Partido: {match_choice}\n")
            file.write(f"Precio de Entrada: {ticket_price}\n")
            file.write(f"ID de la Entrada: {id_ticket}\n")
            file.write(f"------------------------------\n")
            file.close()
    print("Sus datos se han guardado en el archivo 'datos_Entrada.txt'")
    print("")


Venta_entradas.Ticket_sale()

if Venta_entradas.Ticket_sale:
    register_sale(Cliente.name , Cliente.age , Cliente.ci, Entrada.ticket_type, Venta_entradas.Mapa_Estadio.selected_seat, Partido.number, Entrada.ticket_price, Entrada.id_ticket)


def authenticate_ticket():
    ticket_id = input("Por favor ingrese la ID de la entrada que desee para verificar su autenticidad: ")

    with open('datos_Entrada.txt', 'r') as file:
        for line in file:
            if f"ID de la Entrada: {ticket_id}" in line:
                return ticket_id

    print("La ID de la entrada no es válida o no se encuentra en el registro.")
    return None

def go_to_the_stadium():
    ticket_id = authenticate_ticket()

    if ticket_id:
        with open('datos_Entrada.txt', 'r') as file:
            lines = file.readlines()

        with open('datos_Entrada.txt', 'w') as file:
            for line in lines:
                if f"ID de la Entrada: {ticket_id}" in line:
                    file.write(line.replace(f"ID de la Entrada: {ticket_id}", "Ticket Usado"))
                else:
                    file.write(line)

        print("La entrada se ha usado correctamente.")
        print(f"Ha utilizado su entrada para el partido N°: {Partido.number}")
        print("Puede ingresar al juego.")
    else:
        print("La operación de uso de entrada ha sido cancelada.")



again = input("Desea comprar otra entrada? (si o no): ").lower()
if again == "si":
    Venta_entradas.Ticket_sale()
    if Venta_entradas.Ticket_sale:
        register_sale(Cliente.name , Cliente.age , Cliente.ci, Entrada.ticket_type, Venta_entradas.Mapa_Estadio.selected_seat, Partido.number, Entrada.ticket_price, Entrada.id_ticket)
elif again == "no":   
    go_to_the_stadium()



        
def restaurants_per_stadium():
        for stadium in Estadios.stadium_data:
            Estadios.name = stadium['name']
            print(f"Estadio: {stadium['name']}")
            print("Restaurantes:")
            for restaurant in stadium["restaurants"]:
                Restaurantes.name = stadium['restaurant']['name']
                print(f"- {restaurant['name']}")
            print("")
    


     
        



     