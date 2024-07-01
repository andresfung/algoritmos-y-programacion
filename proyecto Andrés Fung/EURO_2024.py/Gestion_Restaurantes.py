
from Venta_entradas import Cliente
from Venta_entradas import Entrada
from API import Restaurantes



if Entrada.client_choice == "vip":
    def register_restaurant(restaurant_name, products,):
        with open('datos_Entrada.txt', 'a') as file:
            file.write(f"Nombre del Producto: {restaurant_name}\n")
            file.write(f"Tipo de Producto: {products}\n")
            file.write(f"------------------------------\n")
        print("Sus datos del restaurante se han guardado en el archivo 'datos_Entrada.txt'")
        print("")

    register_restaurant(Restaurantes.name , Restaurantes.products)





