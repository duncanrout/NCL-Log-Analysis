from collections import Counter

f= open("payments.log","r")
f1 = f.readlines()

a_list = []

total_sum = 0
count = 0
highest = 0
float(highest)

for x in f1:

    if("Request" in x):
    
        a_list = x.split()

        for y in a_list:

            if("StateOrProv" in y):
                #print(y)
                #print("")

                b_list = y.split("StateOrProvince")

                print(b_list[1])
                
                #c_list = b_list[4].split(">")
               # print(c_list)

                

                #if(c_list[1] != "1.00"):
                    #print(float(c_list[1]))

                    
                    #total_sum = total_sum + float(c_list[1])
                   # if(float(c_list[1]) > highest):
                        
                      # highest = float(c_list[1])
            
                

                

        
        #total_sum = total_sum + int(a_list[len(a_list) - 3])
        #print(a_list[len(a_list) - 3])

        
        #OrderTotal currencyID="USD">932.56<
        


print(highest)
    
f.close()



        
