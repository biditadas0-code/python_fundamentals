# 1. Variables, Strings, Lists, Dictionaries, and Loops
username = "Developer"
skills_learned = ["variables", "strings", "lists", "dictionaries", "loops"]

user_profile = {
    "name": username,
    "level": "Beginner",
    "topics": skills_learned
}

print(f"--- Welcome, {user_profile['name']}! ---")
print("Core topics to master:")
for topic in user_profile["topics"]:
    print(f"  - {topic}")


# 2. Functions, Arguments, and Return Values
def celsius_to_fahrenheit(celsius):
    """Converts Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32


# 3. Exercise 1: FizzBuzz
def fizz_buzz(limit=15):
    print("\n--- Running FizzBuzz ---")
    for i in range(1, limit + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# 4. Exercise 2: Word Counter
def count_words(sentence):
    """Counts the number of words in a given string."""
    words = sentence.split()
    return len(words)


# Execution block
if __name__ == "__main__":
    # Test Temperature Converter
    c_temp = 25
    f_temp = celsius_to_fahrenheit(c_temp)
    print(f"\n--- Temperature Converter ---")
    print(f"{c_temp}°C is equal to {f_temp}°F")

    # Run FizzBuzz
    fizz_buzz(15)

    # Test Word Counter
    sample_text = "Python fundamentals are fun and powerful"
    print(f"\n--- Word Counter ---")
    print(f"Sentence: '{sample_text}'")
    print(f"Total Words: {count_words(sample_text)}")

    # 4. Basic Data Structures (Lists & Dictionaries)
def manage_inventory():
    """Demonstrates basic operations with lists and dictionaries."""
    items = ["apple", "banana", "cherry"]
    prices = {"apple": 1.20, "banana": 0.50, "cherry": 2.00}
    
    print(f"Inventory Items: {items}")
    print(f"Banana Price: ${prices['banana']}\n")

if __name__ == "__main__":
    # (Keep your existing code above, and add this at the very end:)
    print("--- 4. Data Structures Test ---")
    manage_inventory()