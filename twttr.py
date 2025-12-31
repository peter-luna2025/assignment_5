VOWELS = "aeiouAEIOU"

def shorten(text: str) -> str:
    """Return text with vowels removed, preserving case."""
    no_vowels = ""
    for char in text:
        if char.lower() not in VOWELS:  # check lowercase only for membership
            no_vowels += char           # keep original case
    return no_vowels

def main():
    tweet_txt = input("Input: ")
    print(shorten(tweet_txt))

if __name__ == "__main__":
    main()
