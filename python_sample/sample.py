def mostrar_proceso():
    print('Seleccione el proceso que desea aplicar:')
    print('1: Introducir puntos de evaluación y comentarios')
    print('2: Comprobar los resultados hasta ahora')
    print('3: Terminar')

def introducir_puntuacion_comentarios():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5:')
        punto = input()
        if punto.isdecimal():
            punto = int(punto)
            if 1 <= punto <= 5:
                print('Introduzca sus comentarios:')
                comentario = input()
                registro = f'Puntuación: {punto} Comentario: {comentario}'
                guardar_datos(registro)
                break
            else:
                print('Por favor, introduzca un valor entre 1 y 5.')
        else:
            print('Introduzca los puntos de valoración como números.')

def guardar_datos(registro):
    with open("data.txt", 'a') as archivo:
        archivo.write(f'{registro}\n')

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    with open("data.txt", "r") as archivo:
        print(archivo.read())
        archivo.close()

def main():
    while True:
        mostrar_proceso()
        opcion = input()
        if opcion.isdigit() and 1 <= int(opcion) <= 3:
            opcion = int(opcion)
            if opcion == 1:
                introducir_puntuacion_comentarios()
            elif opcion == 2:
                comprobar_resultados()
            else:
                print('Terminación.')
                break
        else:
            print('Por favor, introduzca del 1 al 3 para la selección del proceso a realizar.')

if __name__ == "__main__":
    main()
