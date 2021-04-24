from pathlib import Path
import os
drawer=[]
cities=[]
for i in range(0,500):
    a=input('Enter City')
    b=input('Enter Drawer no.')
    c=input("Enter File Name")
    if a in set(cities):
        if b not in set(drawer):
            drawer.append(b)
            Path(f'/home/by/yash/{a}/{b}').mkdir()
            f=open(f'/home/by/yash/{a}/{b}/{c}','w+')
        else:
            f=open(f'/home/by/yash/{a}/{b}/{c}','w+')
    else:
        drawer.append(b)
        cities.append(a)
        print(set(cities))
        print(set(drawer))
        Path(f'/home/by/yash/{a}').mkdir()
        Path(f'/home/by/yash/{a}/{b}').mkdir()
        f=open(f'/home/by/yash/{a}/{b}/{c}','w+')    
       