def main():
    plate = input("Plates:  ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha):
        return False

    if not s.isalnum():
        return False

    has_number = False
    for char in s:
        if char.isdigit():
            has_number = True
            if char == "0":
                return False
            break
        elif has_number:
            return False

    return True


if __name__ == "__main__":
    main()
