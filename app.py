#name = input('What is your name? ')
#color = input('What is your favorite color? ')
#print(name + ' likes ' + color)

#birth_year = input('Birth year: ')
#age = 2022 - int(birth_year)
#print(age)

# weight_lbs = input('What is your weight(lbs)? ')
# kg = int(weight_lbs) * 0.45
# print(kg)weight_lbs = input('What is your weight(lbs)? ')
# # kg = int(weight_lbs) * 0.45
# # print(kg)

# price = 1000000
# good_credit = False
# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

# #has_high_income = False
# has_good_credit = True
# has_criminal_record = True
#
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
# else:
#     print("Not eligible for a loan, applicant has a criminal record")

# temperature = 30
#
# if temperature > 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's neither a hot not cold day")

# name = input("What is your name? ")
# # if len(name) < 3:
# #     print("Name must be at least 3 characters long")
# # elif len(name) > 50:
# #     print("Name can be a maximum of 50 characters")
# # else:
# #     print("Looks good!")

# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# elif unit.upper() == "K":
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# i=1
# while i <= 5:
#     print('*' * i)
#     i=i+1
# print("Done")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry you failed")


# command = ""
# started = False
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#         print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped...")
#         print("Car stopped.")
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit
#         """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry, I don't understand that!")

# for item in range(100+1):
#     print(item)

# prices=[10,20,30]
# total=0
# for price in prices:
#     total+=price
# print(total)

#
# numbers=[2,2,2,2,8,8]
# for i in numbers:
#     output = ''
#     for count in range(i):
#         output+= 'x'
#     print(output)
#
# numbers=[2,2,4,6,3,4,6,1]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, "!") + ' '
print(output)

