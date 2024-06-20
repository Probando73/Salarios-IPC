### Datos ###
ipc = {'Enero': 20.6,
       'Febero': 13.2,
       'Marzo': 11.0,
       'Abril': 8.8,
       'Mayo': 4.2,
       }

sueldo = {'Enero': 460.293,
          'Febero': 552.352,
          'Marzo': 625.999,
          'Abril': 707.379,
          'Mayo': 782.499,
          'Junio': 829.449,

          }

variacion_sueldo = {}

contador = 1

lista_sueldo = []
lista_meses = []

for x in sueldo.values():
    lista_sueldo.append(x)

for x in sueldo.keys():
    lista_meses.append(x)

variacion = []

longitud = len(lista_sueldo) - 1

for x in range(longitud):
    variacion = round(
        ((lista_sueldo[contador] / lista_sueldo[contador-1])-1)*100, 2)
    contador += 1
    variacion_sueldo[lista_meses[contador - 1]] = variacion

for x in longitud:
    print(f'En'{}
print(variacion_sueldo)
