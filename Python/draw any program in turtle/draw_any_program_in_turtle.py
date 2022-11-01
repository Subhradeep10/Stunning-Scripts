import turtle 

  
# creating turtle pen 

t = turtle.Turtle() 

  
# taking input for the no of the sides of the polygon 

n = int(input("Enter the no of the sides of the polygon : ")) 

  
# taking input for the length of the sides of the polygon 

l = int(input("Enter the length of the sides of the polygon : ")) 

  

  

for _ in range(n): 

    turtle.forward(l) 

    turtle.right(360 / n)