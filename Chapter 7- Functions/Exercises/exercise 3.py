def make_shirt(size, message):
    print(f"Making a {size}-sized shirt with the message: '{message}'.")

# The function is called by using positional arguments
make_shirt("Medium", "Hello, World!")

# The function is called using key words
make_shirt(size="Large", message="Python Lover")
