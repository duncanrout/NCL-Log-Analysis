from collections import Counter

f= open("route53.log","r")
f1 = f.readlines()

a_list = []
mostFreq = 0

for x in f1:

    city = (x.split()[7])
    city = city[:3]
    a_list.append(city)

occurence_count = Counter(a_list) 
print(occurence_count.most_common(10))

f.close()



        
