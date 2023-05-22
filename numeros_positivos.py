
print("debes ingresar 10 numeros positivos");
i = 0
numeros = []
while(i < 10):
    r = int(input(f"ingresa el numero {i+1}: "))
    if(r>0):
        i = i + 1
        numeros.append(r);
    else:
        print("solo puedes ingresar numeros positivos")

print(list)
    
