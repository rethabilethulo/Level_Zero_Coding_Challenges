def fahrenheit_temp(c):
    fahrenheit = (c *(9/5)) + 32
    return fahrenheit

def celsius_temp(f):
    celsius = (f - 32) * (5/9)
    return celsius

print(f"Temperature is ", fahrenheit_temp(100) ,"fahrenheit")
print(f"Temperature is" ,celsius_temp(100) ,"degrees celsius")