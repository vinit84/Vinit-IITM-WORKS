


a = "VINIT"
print(a.lower()) # CONVERTS a string into lower case
print(a.isupper()) # returns true if all characters of the string are Upper case

#---------------------------------------------------------------------------------------------

b = "vinit"
print(b.upper()) # string into uppercase
print(b.islower()) # returns true if all characters of the string are lower case

#---------------------------------------------------------------------------------------------

# An application of lower and upper case

name,n1=(input("enter your name and first letter of your name :-")).split(",")
length=len(name)
print(f"character count : {name.lower().count(n1.lower())}")

#---------------------------------------------------------------------------------------------

c = "vinit"
print(c.capitalize()) #converts first character to upper case

#---------------------------------------------------------------------------------------------

d = "vinit upadhyay"
print(d.title()) #converts the first character of each word to upper case 
print(d.istitle())
D = "Vinit Upadhyay"
print(D.istitle()) # returns true if the string follows the rules of a title.

#---------------------------------------------------------------------------------------------

e = "VINIT"
print(e.swapcase()) # swaps cases, lower case becomes upper case and vice versa

#---------------------------------------------------------------------------------------------

f = '123'
print(f.isdigit())#Returns true if all the characters in the string are digit

#---------------------------------------------------------------------------------------------

g = 'abc'
print(g.isalpha())#Returns true if all the characters in the string are in alphabets.

#---------------------------------------------------------------------------------------------

h = 'abc123'
print(h.isalnum())#Returns true if all characters in the string are alpha-numeric
H = 'abc123@#*'
print(H.isalnum())

#---------------------------------------------------------------------------------------------

i = "----PYTHON----"
print(i.strip('-')) #Returns the trimmed version of the string

#---------------------------------------------------------------------------------------------

j = "----Python----"
print(j.lstrip('-')) #Returns the left trim version of the string

#---------------------------------------------------------------------------------------------

k = "----Python----"
print(k.rstrip('-')) #Returns the Right trim version of the string

#---------------------------------------------------------------------------------------------

# Application of r and l strip 

name=("      Harshit       ")
dots=".................... Idhar hai strip "
add=name+dots
print(name.lstrip(" ")+dots)
print(name.rstrip(" ")+dots)
print(name.strip(" ")+dots)


l = "Programming"
print(l.startswith('P')) #True if the string is starting with the specified value
print(l.startswith('p')) #True if the string is starting with the specified value

#---------------------------------------------------------------------------------------------

m = "Programming"
print(m.endswith('g')) #True if the string is Ending with the specified value
print(m.endswith('G')) #True if the string is Ending with the specified value

#---------------------------------------------------------------------------------------------

n = "Programming is Like a heaven"
print(n.count('a'))

#---------------------------------------------------------------------------------------------

o = '9082685211'
print(o.index('1'))

#---------------------------------------------------------------------------------------------

p = input("Say Hello to me with smily :-")
print(p.replace(':)','😊'))

#---------------------------------------------------------------------------------------------



#Practice replace 

#replace problem 3 doublespace with single spaces 

string = " this  is the string where doublespaces  will be replaced with single space"
string = string.replace("  "," ")
print(string)


#---------------------------------------------------------------------------------------------


#write a program to fill in a letter template given below with name and date ?

print("/n")
letter = '''Dear <|NAME|>,
             A letterhead is the heading at the top of a sheet of letter paper (stationery). 
That heading usually consists of a name and an address, and a logo or corporate design, and sometimes a background pattern. The term "letterhead" is often used to refer to the whole sheet imprinted with such a heading. Many companies and individuals prefer to create a letterhead template in a word processor or other software application.

This generally includes the same information as pre-printed stationery but without the additional costs involved. Letterhead can then be printed on stationery (or plain paper) as needed on a local output device or sent electronically. That heading usually consists of a name and an address, and 
a logo or corporate design, and sometimes a background pattern. The term "letterhead" is often used to refer to the whole sheet imprinted with such 
a heading. 

The term "letterhead" is often used to refer to the whole sheet imprinted with such a heading. Many companies and individuals prefer to create a letterhead template in a word processor or other software application.

<|DATE|>
    '''

name = input("enter your name :- ")
date = input ("enter today's date :- ")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)




#strings methods by Harshit 


string="she is beautiful and she is good in dance"
a=string.find("is")
b=string.find("is",5)
print(a,b)


#---------------------------------------------------------------------


#sentar method program

name=input("enter your name :-")
print(name.center(len(name) + 8 ,"*"))


#----------------------------------------------------------------------

#Strings are immutale 

name=input("enter your name :-")
name+= ("@student.onlinedegree"+".iitm.ac.in")
print(name)










