import lista


class Listas:
    lista = ["p", "y", "t", "h", "o", "n"]

    lista[2:]  ## thon
    lista [:2] ## py
    lista[1:3] ## yt
    lista[0:3:2] ## pt
    lista[::] ## python
    lista[::-1] ## nohtyp


    numeros = [1, 30, 21, 2, 9, 65, 34]
    pares = [numero for numero in numeros if numero % 2 == 0]
    print(pares)