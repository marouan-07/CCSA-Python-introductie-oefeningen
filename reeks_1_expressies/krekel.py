N = int(input ("Het aantal waargenomen tjirps per minuut: "))

TF = 50 + (N - 40) / 4

TC = 10 + (N - 40) / 7

print (f"temperatuur (Fahrenheit): {TF:.2f}")
print (f"temperatuur (Celcius): {TC}")