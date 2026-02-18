import sys

LENGTH_UNITS = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000.0,
    'inches': 0.0254,
    'ft': 0.3048,
    'yards': 0.9144,
    'miles': 1609.344
}

WEIGHT_UNITS = {
    'mg': 0.001,
    'g': 1.0,
    'kg': 1000.0,
    'oz': 28.3495,
    'lb': 453.592
}

def convert_temperature(value, from_u, to_u):
    """Handles Celcius, Fahrenheit logic."""
    if from_u == 'c' and to_u == 'f':
        return (value * 9/5) + 32
    if from_u == 'f' and to_u == 'c':
        return (value - 32) * 5/9
    return value

def main():
    if len(sys.argv) < 4:
        print("Usage: python converter.py <value> <from_unit> <to_unit>")
        print("Example: python converter.py 10 km miles")
        return
    
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Error: The first argument must be a number.")
        return
    
    from_u = sys.argv[2].lower()
    to_u = sys.argv[3].lower()

    # 1. Check Length
    if from_u in LENGTH_UNITS and to_u in LENGTH_UNITS:
        # Value -> Meters -> Target
        meters = value * LENGTH_UNITS[from_u]
        result = meters / LENGTH_UNITS[to_u]
        print(f"{value} {from_u} is {result:.4f} {to_u}")

    # 2. Check Weight
    elif from_u in WEIGHT_UNITS and to_u in WEIGHT_UNITS:
        # Value -> Grams -> Target
        grams = value * WEIGHT_UNITS[from_u]
        result = grams / WEIGHT_UNITS[to_u]
        print(f"{value} {from_u} is {result:.4f} {to_u}")

    # 3. Check Temperature
    elif (from_u in ['c', 'f'] and to_u in ['c', 'f']):
        result = convert_temperature(value, from_u, to_u)
        print(f"{value} {from_u.upper()} is {result:.2f} {to_u.upper()}")
    
    else:
        print(f"Error: Cannot convert from {from_u} to {to_u}. Ensure units are in the same category.")

if __name__ == "__main__":
    main()