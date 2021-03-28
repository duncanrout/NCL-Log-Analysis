from collections import Counter

f= open("route53.log","r")
f1 = f.readlines()

a_list = []
mostFreq = 0

for x in f1:

    minute = (x.split(':')[1])
    a_list.append(minute)
    print(minute)
    
occurence_count = Counter(a_list) 
print(occurence_count.most_common(1)[0][0])

f.close()



        
