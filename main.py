def name_get():
  name = str(input("Type your name: "))
  if name:
    print ("Hi " + str(name))
  else:
    print("How are you") 
  return 
  
name_get()