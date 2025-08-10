c= float(input("Digite el primer numero: "))
b= float(input("Digite el segundo numero: "))
a= float(input("Digite el tercer numero: "))

print(f"El primero numero digitado es: {c} y es de tipo {type(c)}")
print (f"El segundo numero digitado es: {b} y es de tipo {type(b)}")
print (f"El segundo numero digitado es: {a} y es de tipo {type(a)}")

print(f"La escuacion quedaria de esta forma: (({c}+5)({b}^2-3({a})({c}))*{a}^2)/4({a})")

resultado= ((c+5)*(b**2-3*a*c)*a**2)/(4*a)

print(f"El resultado es: {resultado}")