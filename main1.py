# try:
#     file = open("a_file.txt")
#     a_dictionay = {"key": "value"}
#     print(a_dictionay["dsdsfs"])
# except FileNotFoundError:
#     file = open("a_file.txt", "a")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"THe key{error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
# raise
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human heights should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)