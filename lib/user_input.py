# user_input.py
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_str_input(prompt):
    return input(prompt)
