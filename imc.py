altura = float(input("Informe sua altura: "))
peso = float(input("Informe seu peso: "))

imc = peso / (altura**2)
imc = round(imc, 2)

print(imc)

if imc <=18.5: 
    print("Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Peso normal")

elif imc >= 25 and imc < 30:
    print("Gordinho")

elif imc >= 30 and imc < 40:
    print("Gordão")

else: 
    print("Gordo pra caralho")