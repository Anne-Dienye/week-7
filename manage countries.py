#coding
def manage_countries():
    countries = {}  # Dictionary to store country-capital pairs
    while True:
        country = input("Wales (or type 'exit' to quit): ").strip().lower()
        if country == "exit":
            break
        
        if country in countries:
            print(f"The capital of {country.capitalize()} is {countries[country]}.")
        else:
            capital = input(f"I don't know the capital of {country.capitalize()}. Please enter it: ").strip()
            countries[country] = capital
            print(f"Thank you! The capital of {country.capitalize()} has been set to {capital}.")

# Run the program
manage_countries()