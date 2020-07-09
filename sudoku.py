import sys
a=[] 
a = [list(map(int,input().split())) for i in range(9)]
for i in range(9):
     print("\n")
     for j in range(9):
         print(a[i][j],end="")

ab=[0]*9
count=0
for i in range(9):
    ab=[0]*9
    for j in range(9):
        ab[a[i][j]-1]+=1
    for k in range(9):
           if(ab[k]>1):
               print("sudoko is wrong")
               exit()
ab=[0]*9               
for i in range(9):
    ab=[0]*9
    for j in range(9):
        ab[a[j][i]-1]+=1
    for k in range(9):
           if(ab[k]>1):
               print("sudoko is wrong")
               exit()               
               
'''               
ab=[0]*9
c=0
d=3
e=0
f=3
for i in range(9):

    ab=[0]*9
    for j in range(c,d):
        count+=1
        for k in range(e,f):
            ab[a[j][k]-1]+=1

            
    for k in range(9):
           if(ab[k]>1):
               print("sudoko is wrong")
               exit()
    
    if(count==3):
        e+=3
        f+=3
        c=3
        d=6
    if(count==6):
        e+=3
        f+=3
        c=6
        d=9   
print("correct")        
            
            
    

         
         

         
'''
