import sys

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
            
def check():
    while 1 == 1:
        numero = int(input("¿Qué número quieres buscar?: "))
        if numero in lista:
            print("Está")
        else:
            print("No está. Prueba otra vez")
            numero
        pregunta = raw_input("¿Quieres buscar otro numero?(y/n): ")
        if pregunta == "y":
            check()
        elif pregunta == "n":
            sys.exit(0)
              
if __name__ == "__main__":
    n = 0
    lista = []
    print("Este es un programa para saber si un número está en la secuencia de Fibonacci o no.")
    while n < 10:
        n += 1
        lista.append(fib(n))
    check()
    
    

    
    
