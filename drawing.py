import turtle
from  pixart import *
def main():
    turta = turtle.Turtle()  # Create the turtle object
    turta.speed(0)  
    turta.penup()
    turta.goto(x, y)  
    turta.pendown()

    #draw_color_pixel('red',turta) # Part 1 

    #draw_pixel('5', turta) # Part 1 
    
    #draw_line_from_string('01A753421', turta) # Part 1 

    
    #if not draw_line_from_string('01Y753421', turta):   # Part 1 
        #print("Invalid color encountered.") # Part 1
        
    #draw_shape_from_string(turta)  # Part 1 
    
    draw_grid(turta) # Part 2 
    
    #draw_shape_from_file(turta) # Part 3 
    
    turtle.exitonclick() 
    


if __name__ == "__main__": # part 4
    main()
