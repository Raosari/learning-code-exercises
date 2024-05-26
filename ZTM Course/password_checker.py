import re

user_name = "Raosari"
new_pass = "1234rao5ari@"
lenght_of_pass = len(new_pass)
hidden_password = "*" * lenght_of_pass

# print(f"Hello {user_name}!, your new password {hidden_password} is {lenght_of_pass} characters long")
# At least 8 char long
# Contain any sort letters, numbers, at least 1 special char

#Pattern to Minimum eight characters, at least one uppercase letter, one lowercase letter and one number:
pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$")

if pattern.search(new_pass) and lenght_of_pass > 8:
    print(f"Hello {user_name}!, your new password {hidden_password} is {lenght_of_pass} characters long")
else:
    print('your password doesnt accomplish the minimum requieriments')
