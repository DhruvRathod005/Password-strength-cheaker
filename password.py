password = input("Enter your password: ")

has_length = False
has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

if len(password) >= 8:
    has_length = True

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

conditions_met = sum([has_length, has_upper, has_lower, has_digit, has_special])

print("\n--- Result ---")

if conditions_met == 5:
    print("Password Strength: Very Strong")
elif conditions_met == 4:
    print("Password Strength: Strong")
elif conditions_met == 3:
    print("Password Strength: Medium")
elif conditions_met == 2:
    print("Password Strength: Normal")
else:
    print("Password Strength: Weak")

if conditions_met < 5:
    print("Please fulfill these conditions to make it Very Strong:")
    if not has_length:
        print("- Must be at least 8 characters long.")
    if not has_upper:
        print("- Must include at least one uppercase letter (A-Z).")
    if not has_lower:
        print("- Must include at least one lowercase letter (a-z).")
    if not has_digit:
        print("- Must include at least one number (0-9).")
    if not has_special:
        print("- Must include at least one special character (!, @, #, etc.).")
