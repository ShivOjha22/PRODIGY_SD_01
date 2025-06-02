def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == "celsius" or unit == "c":
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"\n{value}° Celsius is:")
        print(f"{f:.2f}° Fahrenheit")
        print(f"{k:.2f} Kelvin")
    elif unit == "fahrenheit" or unit == "f":
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"\n{value}° Fahrenheit is:")
        print(f"{c:.2f}° Celsius")
        print(f"{k:.2f} Kelvin")
    elif unit == "kelvin" or unit == "k":
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"\n{value} Kelvin is:")
        print(f"{c:.2f}° Celsius")
        print(f"{f:.2f}° Fahrenheit")
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")

def main():
    while True:
        try:
            temp_value = float(input("\nEnter the temperature value: "))
            temp_unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")
            convert_temperature(temp_value, temp_unit)
        except ValueError:
            print("Please enter a valid numeric temperature.")

        again = input("\nDo you want to convert another temperature? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
