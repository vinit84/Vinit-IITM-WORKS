#Python flowchart 

print("Travel from city A to city B")
Time=(int(input("Enter Time in Hours :-")))
print(f"Within {Time} Hours you want to reach To City B")
Longer=int(input("Define Longer distance In Km :-"))
print(f"Destination is {Longer} Longer")

#Calculating for Train Flowhart In which Time required is greater than Longer Distance

if(Time >= Longer):
    #Here we are deciding if price is higher go with Train otherwise if price is less then go with Coach
    Price = int(input("Enter Price :-"))
    Higher = int(input("Define Higher :-"))
    if (Price >= Higher):
        print("Train")
    else:
        print("Coach")
#Calculating for Flight Flowhart In which Time required is Shorter  than Longer Distance     
else:
    #Here we are deciding if price is higher go with daytime flight otherwise if price is less then go with redeyeflight
    Price=int(input("Enter price :-"))
    Higher=int(input("Define Higher :-"))
    if (Price >= Higher):
        print("Daytime Flight")
    else:
        print("Red eye Flight")
    

