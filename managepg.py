import os,shutil
x=input('enter the city')
y=input ('enter drawer no')
z=input ('enter file name')
Path=" "
if os.path.exists(os.path.join(path,x)):
     if os.path.exists(os.path.join(path,x,y)):
                    def oper(f):
                         return{'r': 'remove' , 'm':'move'}.get(f,-1)
          inp=input ('press r to remove and m to move')
           t=oper(inp)
           if t.lower()== 'remove':
              for files in os.listdir(os.path.join(path,x,y)):
                      if z in files:
                          os.unlink(z)
                      else: 
                              print('file does not exist')
            elif t.lower()=='move'  :          
                for files in os.listdir(os.path.join(path,x,y)):
                    if z in files:
                    	a=input('enter drawer no ti move the file')
                    	 If os.path.exists(os.path.join(path,x,a)):
                    	 	des=os.path.join(path,x,a)
                    	 	shutil.move(z,des)
                    	 	
                    	else:
                    		des=os.path.join(path,x,a)
                    		os.mkdir(path)
                    		shutil.move(z,path)
                else:
                    print('invalid input')     	
     else:
     	 print('drawer does not exist')   
else:
	print('invalid city name')        	        