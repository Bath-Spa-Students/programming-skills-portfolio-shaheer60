def describe_city(city, country="Default Country"):
    print(f"{city} is in {country}.")

# Function called for 3 different cities
describe_city("Reykjavik", "Iceland")
describe_city("Tokyo", "Japan")
describe_city("New York")  # default conntry value will be used
