nomEmpre=str(input("digite la empresa a la que pertenece: "))
nombre=str(input("digite su primer nombre: "))
subNombre=nombre[0]
nombre2=str(input("digite su segundo nombre: "))
subNombre2=nombre2[0]
apellido=str(input("digite su primer apellido: "))
subApellido=apellido[0]
naci=str(input("digite su año de nacimiento: "))
ultimos=naci[2:4]

print("su correo es: "+subNombre+subNombre2+apellido+str(ultimos)+"@"+nomEmpre+".com")