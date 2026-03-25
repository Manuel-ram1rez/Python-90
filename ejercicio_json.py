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

resultado = leer_archivo_(200)
#-----join() por estetica
estetica = ', '.join(resultado)
print(estetica)