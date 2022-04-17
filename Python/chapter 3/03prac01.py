# if condition 
#Let us consider the movie "Avengers". This is a 13+ Movie


birth_year = int(input("PLease enter your birth year  :-"))
print(birth_year)

current_year = 2022

age = current_year-birth_year
print(f'Your age is :-',+age)

if (age<13):
    print("You are under age, you cannot watch this movie")
else:
    print("You are old enough to watch Avengers, Enjoy!")
