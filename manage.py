import os,shutil,sys
x=input('enter the city')
y=input ('enter drawer no')
z=input ('enter file name')
pat="/storage/emulated/0/Android/data/ru.iiec.pydroid3"
def oper(f):
    return{'r':'remove','m':'move'}.get(f,-1)
if os.path.exists(os.path.join(pat,x)):
     if os.path.exists(os.path.join(pat,x,y)):
         inp=input('press r to remove and m to move')
         t=oper(inp)
         print(t +' operation')
         if (t.lower()== 'remove'):
              for files in os.listdir(os.path.join(pat,x,y)):
                     
                      if (z in files):
                          os.rmdir(os.path.join(pat,x,y,z))
                          print('file removed')
                      else: 
                          sys.exit('file does not exist')
                          break
         elif t.lower()=='move':       
                for files in os.listdir(os.path.join(pat,x,y)):
                    if z in files:
                    	a=input('enter drawer no to move the file')
                    	if os.path.exists(os.path.join(pat,x,a)):
                    	 	des=os.path.join(pat,x,a)
                    	 	src=os.path.join(pat,x,y,z)
                    	 	print(shutil.move(src,des))
                    	 	
                    	else:
                    		des=os.path.join(pat,x,a)
                    		os.mkdir(des)
                    		print('drawer created')
                    		src=os.path.join(pat,x,y,z)
                    		shutil.move(src,des)
                    		print('file moved successfully')
                    else:
                    	sys.exit('file does not exist')
                    	break
         else:
               print('invalid input')     	
     else:
     	 print('drawer does not exist')   
else:
	print('invalid city name')        	        