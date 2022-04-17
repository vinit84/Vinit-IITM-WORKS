alpha ='abcdefghijklmnopqrstuvwxyz'
i = 23

#print(alpha[i])
#print(alpha[i+1])
#print(alpha[i+2])
#print(alpha[i+3])

print(alpha[i%26])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26]) # here what's actually happening is when 25+2 = 27 %(Modulo) 26 ==>the remainder will be 1