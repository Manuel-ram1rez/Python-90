import ejercicio_json
#-----
menu = {
    '1': ejercicio_json.agregar_producto,
    '2': ejercicio_json.ver_archivo,
    '3': ejercicio_json.actualizar_producto,
    '4': ejercicio_json.borrar_producto,
    '5': ejercicio_json.salir
}

def ejecutar_menu():
    while True:
        print('-'*24)
        print('-----Menu principal-----')
        print('--1 Agregar un nuevo producto')
        print('--2 Ver Inventario')
        print('--3 Actualizar producto')
        print('--4 Borrar producto')
        print('--5 Salir')
        opcion = input('Ingrese opcion: ')

        accion = menu.get(opcion)

        if accion:
            accion()
        else:
            print('Opcion invalida')

if __name__ == '__main__':
    ejecutar_menu()