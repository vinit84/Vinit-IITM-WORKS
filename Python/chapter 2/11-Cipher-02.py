alpha ="abcdefghijklmnopqrstuvwxyz"
v = "vinit"

# I expect to output wjoju

t=''
i = 0
k=1 # here we initialized 1 with k so that we can make chnages here and it will affect over thier it handles shift of name with 1 variable 2 var and so on.  
t=t+(alpha[ ( (  (alpha.index(v[i]))   +k) % 26 )] )
t=t+(alpha[ ( (  (alpha.index(v[i+1])) +k)%26) ] )
t=t+(alpha[ ( (  (alpha.index(v[i+2])) +k)%26)])
t=t+(alpha[ ( (  (alpha.index(v[i+3])) +k)%26)])
t=t+(alpha[ ( (  (alpha.index(v[i+4])) +k)%26)])
print(t)