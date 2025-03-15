import os

home_path = os.path.expanduser("~")  # Automatically points to your home folder
contents = os.listdir(home_path)

print("Contents of Home Directory:")
for item in contents:
    print(item)
    


