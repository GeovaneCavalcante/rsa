import random


def mod(a, b):
    if(a < b):
        return a
    else:
        c = a % b
        return c


def totiente(n, p, q):

    tot = (p - 1) * (q - 1)

    return tot


def chave_privada(toti, e):
    d = 0
    while(mod(d*e, toti) != 1):
        d += 1
    return d


def chave_publica(num):
    def mdc(n1, n2):
        rest = 1
        while(n2 != 0):
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2, num)
        if(mdc(num, e) == 1):
            return e


def cifrar(msg, e, n):

    tam = len(msg)
    i = 0
    lista = []
    while(i < tam):
        letter = msg[i]
        k = ord(letter)
        k = k**e
        d = mod(k, n)
        lista.append(d)
        i += 1
    return lista


def descifra(cifra, n, d):

    lista = []
    i = 0
    tamanho = len(cifra)

    while i < tamanho:
        result = cifra[i]**d
        texto = mod(result, n)
        letra = chr(texto)
        lista.append(letra)
        i += 1
    return lista


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


p = int(input("Digite um número primo: "))
q = int(input("Digite outro número primo diferente: "))

if not (is_prime(p) and is_prime(q)):
    raise ValueError('Não é número primo.')
elif p == q:
    raise ValueError('p e q são iguais')

n = p * q



totiente_n = totiente(n, p, q)
e = chave_publica(totiente_n)

chave_publica = (n, e)

print("Sua chave pública é : " + str(chave_publica))

msg = str(input("Digite a mensagem: "))

msg_cifrada = cifrar(msg, e, n)
print("Mensagem cifrada: ")

cifrada_msg = ''

for x in msg_cifrada:
    cifrada_msg += str(x)

print(cifrada_msg)

chave_pri = chave_privada(totiente_n, e)

print("Sua chave privada é : " + str(chave_pri))

msg_usuario = descifra(msg_cifrada, n, chave_pri)

print("\nMensagem original: ")
print(''.join(msg_usuario))
