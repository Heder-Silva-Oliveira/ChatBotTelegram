import hashlib


print('*'*30)

def codigo(text, valor):
    texto = text

    menu = valor

    if menu == 1:
        resultado = hashlib.md5(texto.encode('utf-8'))
        print('A hash é: ', resultado.hexdigest())
    elif menu == 2:
        resultado = hashlib.sha1(texto.encode('utf-8'))
        print('A hash é: ', resultado.hexdigest())
    elif menu == 3:
        resultado = hashlib.sha256(texto.encode('utf-8'))
        print('A hash é: ', resultado.hexdigest())
    elif menu == 4:
        resultado = hashlib.sha512(texto.encode('utf-8'))
        print('A hash é: ', resultado.hexdigest())
    else:
        print("ALGO DEU ERRADO")