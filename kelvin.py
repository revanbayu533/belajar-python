kelvin = int(input("Masukkan Suhu Kelvinnya \t\t: "))

celcius = kelvin - 273
fahrenheit = (9/5 * kelvin) - 459.67
reamur = 4/5 * (kelvin - 273)

print(f"Kelvinnya: {kelvin}°K Ke Celcius Menjadi\t: {celcius}°C")
print(f"Kelvinnya: {kelvin}°K Ke Fahrenheit Menjadi\t: {fahrenheit}°F")
print(f"Kelvinnya: {kelvin}°K Ke Reamur Menjadi\t: {reamur}°R")