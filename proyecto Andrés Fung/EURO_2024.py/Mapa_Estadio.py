import tkinter as tk
import random

def seats():
    stage_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def draw_stage_map(canvas):
        # Tamaño del asiento
        seat_size = 40

        # Colores para los asientos
        available_color = "green"
        occupied_color = "red"
        selected_color = "blue"

        # Dibujar el mapa del estadio
        for row in range(10):
            for col in range(10):
                x = col * seat_size
                y = row * seat_size

                # Dibujar el cuadrado del asiento
                if stage_map[row][col] == 0:
                    color = available_color
                elif stage_map[row][col] == 1:
                    color = occupied_color
                else:
                    color = selected_color
                canvas.create_rectangle(x, y, x + seat_size, y + seat_size, fill=color)

                # Agregar número y letra al asiento
                canvas.create_text(x + seat_size / 2, y + seat_size / 2, text=f"{row+1}-{chr(ord('A') + col)}", font=("Arial", 12))

    # Crear la ventana
    window = tk.Tk()
    window.title("Mapa del Estadio")

    # Crear el widget Canvas
    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    # Generar asientos disponibles y ocupados aleatoriamente
    for row in range(10):
        for col in range(10):
            if random.choice([0, 1]) == 1:
                stage_map[row][col] = 1

    # Dibujar el mapa del estadio
    draw_stage_map(canvas)

    def select_seat():
        print("Aqui tienes un mapa del estadio")
        print("")
        asiento_reservado = False
        while True:
            # Solicitar al usuario la fila
            selected_y = input("Ingrese el número de fila (1-10): ")

            # Solicitar al usuario la columna
            selected_x = input("Ingrese la letra de columna (A-J): ")

            # Convertir la entrada del usuario a valores de fila y columna
            selected_y = int(selected_y) - 1
            selected_x = ord(selected_x.upper()) - ord('A')

            # Verificar si el asiento está disponible
            if 0 <= selected_y < 10 and 0 <= selected_x < 10 and stage_map[selected_y][selected_x] == 0:
                # Marcar el asiento como seleccionado
                stage_map[selected_y][selected_x] = 2

                # Actualizar el gráfico del mapa del estadio
                canvas.delete("all")
                draw_stage_map(canvas)

                # Poner el asiento selecionado en azul
                x = selected_x 
                y = selected_y 
                canvas.create_rectangle(x - 40 / 2, y - 40 / 2, x + 40 / 2, y + 40 / 2, outline="blue", width=2)

                # Solicitar confirmación al usuario
                confirm = input("¿Desea reservar este asiento? (si o no): ").lower()
                if confirm == "si":
                    stage_map[selected_y][selected_x] = 1
                    print("¡Asiento reservado!")
                    # Guardar el asiento seleccionado en una variable de tipo lista
                    global selected_seat
                    selected_seat = [selected_y + 1, chr(ord('A') + selected_x)]
                    window.destroy()
                    break
                elif confirm == "no":
                    stage_map[selected_y][selected_x] = 0
                    canvas.delete("all")
                    draw_stage_map(canvas)   #row
                    print("Asiento no reservado.")
                else:
                    stage_map[selected_y][selected_x] = 0
                    canvas.delete("all")
                    draw_stage_map(canvas)
                    print("Asiento no reservado.")
                    print("Por favor diga si o no")
            else:
                print("El asiento seleccionado está ocupado o fuera de rango. Por favor, intente de nuevo.")
        


    window.after(1000, select_seat)
    window.mainloop()

    return (f"Asiento seleccionado: {selected_seat}")
    

