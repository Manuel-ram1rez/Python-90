import json
#-----
def leer_archivo_(presupuesto: int)-> list:
    try:
        with open ('tiend.json', 'r', encoding= 'utf-8') as archivo:
            dato = json.load(archivo)
            return sorted([i['nombre'] for i in dato if i['precio'] <= presupuesto and i.get('con_stock', False)])
    except FileNotFoundError:
        print('No se pudo abrir el archivo, ERROR')
        return []

def agregar_producto():
    ruta = 'tienda.json'
    try:
        with open (ruta, 'r', encoding='utf-8') as archivo:
            inventario = json.load(archivo)
        
        nombre = input('Ingrese el nombre del producto: ')

        while True:
            try:
                precio = int(input('Ingrese el precio del producto: '))
                break
            except ValueError:
                print('ERROR: tines que ingresar numeros')

        opcion = input('Hay producto si/no').lower()
        con_stock = True if opcion == 'si' else False

        nuevo_item = {
            'nombre': nombre,
            'precio': precio,
            'con_stock': con_stock
        }

        inventario.append(nuevo_item)

        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii= False)

        print(f'{nombre} agregado correctamente')

    except FileNotFoundError:
        print('El archivo no existe en la BD')




def ver_archivo():
    with open ('tienda.json', 'r', encoding='utf-8') as archivo:
        dato_tienda = json.load(archivo)
        
        for i in dato_tienda:
            print(f'producto: {i['nombre']}: {i['precio']}  {i['con_stock']}')


def actualizar_producto():
    ruta = 'tienda.json'

    try:
        with open (ruta, 'r', encoding='utf-8') as archivo:
            inventario = json.load(archivo)
        
        encontrado = False
        actualizar_p = input('Ingrese el nombre del producto: ')

        for producto in inventario:
            #vemos is tiene stock
            if actualizar_p.lower() == producto['nombre'].lower():
                print('Producto encontrado :)\n')

                if producto['con_stock'] == False:
                    print('No hay en stock')
                else:
                    print('Producto con stock')
                print(f'Nombre: {producto['nombre']}  Precio: {producto['precio']}')
                encontrado = True

                #nuevos datos

                print('------Nuevos Datos-----')
                producto['nombre'] = input('Ingrese nuevo nombre: ')

                while True:
                    try:
                        producto['precio'] = int(input('Ingrese nuevo precio: '))
                        break
                    except ValueError:
                        print('ERROR: Ingrese solo numeros')

                nuevo_stock = input('Tiene stock? si/no: ').lower()
                producto['con_stock'] = True if nuevo_stock == 'si' else False

                #guaradar y salir del bucle for
                with open (ruta, 'w', encoding='utf-8') as archivo:
                    json.dump(inventario, archivo, indent=4, ensure_ascii= False)

                print('Producto agregado correcatamente!!!')
                break

        if not encontrado:
            print('Producto no existente')

    except FileNotFoundError:
        print('No se encotro el archivo')


def borrar_producto():
    ruta = 'tienda.json'
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            inventario = json.load(archivo)
        
        nombre_eliminar = input("Nombre del producto a borrar: ").lower()
        
        # Guardamos el tamaño original para saber si realmente borramos algo
        total_antes = len(inventario)
        

        # "Crea una lista con los productos cuyo nombre NO sea el que quiero borrar"
        inventario = [p for p in inventario if p['nombre'].lower() != nombre_eliminar]
        
        if len(inventario) < total_antes:
            with open(ruta, 'w', encoding='utf-8') as archivo:
                json.dump(inventario, archivo, indent=4, ensure_ascii=False)
            print(f"Producto '{nombre_eliminar}' eliminado con éxito.")
        else:
            print("No se encontró ningún producto con ese nombre.")
            
    except FileNotFoundError:
        print("Error: No existe la base de datos.")

def salir():
    exit()