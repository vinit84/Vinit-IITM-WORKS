def is_function(domain,fun):
    for i in domain:
        for key in fun.keys():
            if i==key:
                return True #what actually returns does :- it only checks one condition at a one time 
            else:
                return False
print(is_function([5, 2, 4],{1: 5, 2: 6, 4: 7}))