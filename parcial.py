import json

def leer_json(file_path):
    """
    Lee un archivo JSON de entrada
    Recibe un string y devuelve una lista de datos del archivo.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
        return[]

def imprimirLista(datos):
    """
    Imprime la lista de datos
    Recibe una lista diccionario.
    """
    if not datos:
        print("No hay datos para mostrar.")
        return

    titulos = datos[0].keys()
    titulo = " / ".join(titulos)
    print(titulo)
#Separa con /
    for servicio in datos:
        fila = " / ".join(str(servicio[clave]) for clave in titulos)
        print(fila)

def asignarTotales(datos):
    """
    Le agrega el total de cada servicio haciendo cantidad * precio.
    Recibe una lista diccionario y deuelve la lista diccionario actualizada con el total.
    """
    calcularTotal = lambda cantidad, precio: cantidad * precio
    
    for servicio in datos:
        idServicio = servicio['id_servicio']
        cantidad = None
        precio = None
        for serv in datos:
            if serv['id_servicio'] == idServicio:
                cantidad = int(serv['cantidad'])
                precio = float(serv['precioUnitario'])
                break
        
        if cantidad is not None and precio is not None:
            servicio['totalServicio'] = calcularTotal(cantidad, precio)
    
    return datos


def filtrar(datos,filtro):
    """
    Filtra los servicios por tipo.
    Recibe una lista diccionario y un filtro(tipo), devuelve la lista nueva que cumple con el filtro.
    """
    servicios = []
    for servicio in datos:
        if servicio['tipo'] == filtro:
            servicios.append(servicio)
    return servicios

def nuevoArchivo (rutaDeARchivo, datos):
    """
    Guarda los datos en un nuevo Archivo JSON.
    Recibe una ruta de ubicacion del archivo y los datos.
    """
    with open(rutaDeARchivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def ordenarServicios(datos):
    """
    Ordena los servicios por su descripcion.
    Recibe la lista diccionario de los servicios y devuelve la lista ordenada.
    """
    ordenados = sorted(datos, key=lambda x: x['descripcion'])
    return ordenados

def menu():
    """
    muestra un menu y ejecuta las opciones seleccionadas
    """
    datos = []
    while True:
        print("\nMenú:")
        print("1 Cargar archivo")
        print("2 Imprimir lista")
        print("3 Asignar totales")
        print("4 Filtrar por tipo")
        print("5 Mostrar servicios")
        print("6 Guardar servicios")
        print("7 Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            pathARchivo = input("Ingrese el nombre del archivo: ")
            datos = leer_json(pathARchivo)
            if datos:
                print("Archivo cargado .")
                
        elif opcion == '2':
            imprimirLista(datos)
                
        elif opcion == '3':
            if datos:
                datos = asignarTotales(datos)
                print("Totales asignados.")
            else:
                print("No hay datos cargados. Cargar un archivo primero.")
                
        elif opcion == '4':
            if datos:
                tipo = input("Tipo de servicio: 1-MINORISTA 2-MAYORISTA 3-EXPORTAR: ")
                filtrados = filtrar(datos, tipo)
                #Directororio de salida debe escribirse la ubicacion del archivo junto con su nombre de archivonuevo.
                directorioSalida = input("Ingresear directorio del archivo + su nombre de archivo: ")
                nuevoArchivo(directorioSalida, filtrados)
                print(f"Archivo nuevo guardado en {directorioSalida}.")
            else:
                print("No hay datos cargados. Cargar un archivo primero.")
                
        elif opcion == '5':
            if datos:
                datosOrdenados = ordenarServicios(datos)
                imprimirLista(datosOrdenados)
            else:
                print("No hay datos cargados. Cargar un archivo primero.")
                
        elif opcion == '6':
            if datos:
                rutaSalida = input("Ingrese el nombre del archivo de salida: ")
                nuevoArchivo(rutaSalida, datos)
                print(f"Datos guardados en {rutaSalida}.")
            else:
                print("No hay datos cargados. Cargar un archivo primero.")
                
        elif opcion == '7':
            print("Saliendo...")
            break
            
        else:
            print("Opción no válida.")

if __name__ == "__main__":

    #Ubicacion del archivo en mi PC
    ubicacionArchivo = "C:/Users/lauta/OneDrive/Escritorio/utnfra/Parcial 1 Labo/data.json"
    datos = leer_json(ubicacionArchivo)
    menu()
