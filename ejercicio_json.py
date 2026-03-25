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

        try:
            precio = int(input('Ingrese el precio del producto: '))

        except ValueError:
            print('tines que ingresar numeros')

        con_stock = input('Hay producto si/no').lower()

        if con_stock == 'si':
            con_stock = True
        elif con_stock == 'no':
            con_stock = False

        nuevo_item = {
            'nombre': nombre,
            'precio': precio,
            'con_stock': con_stock
        }

        inventario.append(nuevo_item)
        with open(ruta, 'w', encoding='utf-8') as archivo:
            json.dump(inventario, archivo, indent=4)

        print(f'{nombre} agregado correctamente')
    except FileNotFoundError:
        print('El archivo no existe en la BD')

def ver_archivo():
    with open ('tienda.json', 'r', encoding='utf-8') as archivo:
        dato_tienda = json.load(archivo)
        
        for i in dato_tienda:
            print(f'producto: {i['nombre']}: {i['precio']}  {i['con_stock']}')

#agregar_producto()

ver_archivo()