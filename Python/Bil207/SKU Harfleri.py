def S():
    print("         ")
    print(" ******* ")    
    print("*********")    
    print("**       ")    
    print("***      ")    
    print(" *****   ")    
    print("   ***** ")    
    print("      ***")    
    print("       **")      
    print("*********")    
    print(" ******* ") 
    print("         ",end=" ")

def K():
    print("         ")  
    print("**     **")    
    print("**    ** ")    
    print("**   **  ")    
    print("** **    ")    
    print("****     ")    
    print("****     ")    
    print("**  **   ")    
    print("**   **  ")      
    print("**    ** ")    
    print("**     **")   
    print("         ",end=" ") 

        
def U():
    print("         ")
    print("**     **")    
    print("**     **")    
    print("**     **")    
    print("**     **")         
    print("**     **")    
    print("**     **")          
    print("**     **")    
    print("**     **")      
    print("*********")    
    print(" ******* ")
    print("         ",end=" ")
        
def Girdi():
    global x
    x = input("Lütfen K/S/U Harflerinden Anlamsız Harf Bloğu Yazın: ")
    x.upper() 
    for i in x:
        if i == "U":
            U()
        elif i == "S":
            S()    
        elif i == "K":
            K()
            
Girdi()