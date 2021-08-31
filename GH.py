import hashlib

print('*'*30)
texto = input("Digite o texto: ")

menu = int(input('''----MENU:ESCOLHA O TIPO DE HASH----
                 1) MD5
                 2)SHA1
                 3)SHA256
                 4)SHA512
                 digite o tipo de hash: '''))

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