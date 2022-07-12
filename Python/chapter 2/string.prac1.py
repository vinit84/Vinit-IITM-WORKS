name,char=input("enter comma separated name and character :-").split(",")
print(f"length of your name {len(name.strip())}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}")

