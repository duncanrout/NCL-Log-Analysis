from collections import Counter

f= open("vsftpd.log","r")
f1 = f.readlines()

a_list = []

total_sum = 0

for x in f1:

    if("[ftpuser]" in x and "DOWNLOAD" in x):
        a_list = x.split()
        total_sum = total_sum + int(a_list[len(a_list) - 3])
        #print(a_list[len(a_list) - 3])
        


print(total_sum)
    
f.close()



        
