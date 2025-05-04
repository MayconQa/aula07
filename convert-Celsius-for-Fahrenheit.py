
def celsius_para_fahrenheit(celsius: float) -> float:
    """
    Converte Celsius para Fahrenheit.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

fahrenheit = float(input("Informe a temperatura em Celsius: "))

fahrenheit = celsius_para_fahrenheit(fahrenheit)
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")

