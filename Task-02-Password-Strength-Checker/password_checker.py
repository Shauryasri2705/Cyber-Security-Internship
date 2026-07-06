# Password Strength Checker

password = input("Enter your password: ")

score = 0

# Check Length
if len(password) >= 8:
    score += 1
else:
    print("- Password should be at least 8 characters long.")

# Check Uppercase
if any(c.isupper() for c in password):
    score += 1
else:
    print("- Add at least one uppercase letter.")

# Check Lowercase
if any(c.islower() for c in password):
    score += 1
else:
    print("- Add at least one lowercase letter.")

# Check Number
if any(c.isdigit() for c in password):
    score += 1
else:
    print("- Add at least one number.")

# Check Special Character
special = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

if any(c in special for c in password):
    score += 1
else:
    print("- Add at least one special character.")

print("\nPassword Strength")

if score <= 2:
    print("Weak")

elif score == 3 or score == 4:
    print("Medium")

else:
    print("Strong")