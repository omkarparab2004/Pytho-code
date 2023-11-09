# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

# Test the conversion functions
celsius_temperature = 25.0
kelvin_temperature = celsius_to_kelvin(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {kelvin_temperature} Kelvin")

kelvin_temperature = 298.15
celsius_temperature = kelvin_to_celsius(kelvin_temperature)
print(f"{kelvin_temperature} Kelvin is equal to {celsius_temperature} degrees Celsius")
