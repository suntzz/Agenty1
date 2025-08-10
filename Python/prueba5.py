num1=int(input("digite un numero de 3 digitos: "))
num2=int(input("digite un numero de 1 digito: "))

cond=(num1%100)%num2==0 and (num2**2<(num1%100))

print("se cumplen las condiciones?:",cond)