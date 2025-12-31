def convert(fraction):
    try:
        x, y = fraction.split("/")
        numerator = int(x)
        denominator = int(y)

        if denominator == 0:
            raise ValueError

        # Reject negative values
        if numerator < 0 or denominator < 0:
            raise ValueError

        # Reject improper fractions like 5/4
        if numerator > denominator:
            raise ValueError

        percentage = int((numerator / denominator) * 100)
        return percentage

    except (ValueError, ZeroDivisionError):
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    while True:
        fuel_level = input("Fuel level in fraction (e.g. 1/4, 1/2, 3/4): ").strip()
        try:
            percentage = convert(fuel_level)
            print(gauge(percentage))
            break
        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()