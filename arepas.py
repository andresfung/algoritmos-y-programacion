#Arepas dinámicas Andrés Fung

print("Hoy vamos a hacer unas arepas")
agua = input("indique la cantidad de agua en mililitros: ") 
harina = input("indique la cantidad de harina en gramos: ")
sal = int(agua)/16
bol = (int(harina) + int(agua))
aceite = int(bol)/16/3
masa = bol + sal + aceite

print("La cantidad de masa de arepas en gramos es: ", masa)
print("¡Disfrute de sus arepas!")



200