# Imprime números del 1 al 30, pero:
# - Si divisible por 3: "Fizz"
# - Si divisible por 5: "Buzz"
# - Si divisible por ambos: "FizzBuzz"

# ESCRIBE TU CÓDIGO AQUÍ:

numero=30 #Puede cambiar con un input

for i in range(1,numero +1):

    if i%3==0:
        if i%5==0:
            print('FizzBuzz')
        else:
            print('Fizz')
    
    elif i%5==0:
        print('Buzz')
    
    else:
        print(f'{i}')