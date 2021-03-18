from collections import Counter

f= open("netflow.txt","r")
f1 = f.readlines()

a_list = []
b_list = []

for x in f1:
    
    a_list.append(x.split()[4])

for y in a_list:

    b_list.append(y.split(':')[0])


print(len(Counter(b_list).keys()))
    
f.close()



        
