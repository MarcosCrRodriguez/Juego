import json

def generar_json(ruta_json:str, lista_datos:dict)->int:
    '''
    Brief: Genero un archivo json, en donde guardo los datos pasados por parametros
    Parameters: ruta_json -> donde se guardara el archivo json
                lista_formateada -> lista de personajes 
    '''
    retorno = -1

    with open(ruta_json, 'w') as archivo:
        json.dump(lista_datos, archivo, indent=4)
        retorno = 1

    return retorno

def leer_json(ruta_json:str)->dict:
    '''
    Brief: Lee un archivo json, en el que tomo la informacion dentro del archivo y lo muestro por pantalla den forma de lista
    Parameters: ruta_json -> donde esta hubicado el archivo json
    '''
    with open(ruta_json, 'r') as archivo:
        lista_dict = json.load(archivo)
        # for dato in lista_dict:
        #     print(dato)

    return lista_dict