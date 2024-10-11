import turtle 

pixel = 30
x = -300 
y = 300 

def get_color(color):
    if color == '0':
        return 'black'
    elif color == '1':
        return 'white'
    elif color == '2':
        return 'red'
    elif color == '3':
        return 'yellow'
    elif color == '4':
        return 'orange'
    elif color == '5':
        return 'green'
    elif color == '6':
        return 'yellowgreen'
    elif color == '7':
        return 'sienna'
    elif color == '8':
        return 'tan'
    elif color == '9':
        return 'gray'
    elif color == 'A':
        return 'darkgray'
    else:
        return None  

def draw_color_pixel(color_string, turta):
    """Draws a single pixel of the given color."""
    turta.fillcolor(color_string)
    turta.begin_fill()  
    for i in range(4):  
        turta.forward(pixel)  
        turta.right(90)  
    turta.end_fill()  
    turta.forward(pixel)  

def draw_pixel(color_string, turta):
    """Draws a colored pixel by using get_color and draw_color_pixel"""
    color = get_color(color_string)  
    if color:  
        draw_color_pixel(color, turta)  

def draw_line_from_string(color_string, turta):
    
    for char in color_string:  # Loop through every character in the string
        color = get_color(char)  # Get the corresponding color
        if color is None:  # Check if the color is invalid
            return False  
        draw_pixel(char, turta)  # Draw a pixel for every valid character
    return True  # Return True if all pixels were drawn 

def draw_shape_from_string(turta):
    """asks the user for a color  and draws similar rows to what the user inputed"""
    new_y = y
    while True:  
        color_string = input("Pick a colors from 0 to 9 and A: ")
        if not color_string:  
            print("No input entered. ")
            break
        if not draw_line_from_string(color_string, turta):  
            print("Invalid color entered.")
            break
        
        turta.penup()  
        new_y = new_y - pixel  
        turta.goto(x, new_y)  
        turta.pendown()  
        
def draw_grid(turta):
    """draw a 20x20 checkerboard """
    new_y = y
    for row in range(20):
        if row % 2 == 0:
            color_string = '02' * 10  
        else:
            color_string = '20' * 10
            
        draw_line_from_string(color_string, turta)  
        
        turta.penup()  
        new_y = new_y - pixel  
        turta.goto(x, new_y)  
        turta.pendown()  

def draw_shape_from_file(turta):
    """ask the user to provide a text file and if its invalid return a FileNotFoundError"""
    new_y = y
    file_path = input("Enter the path of a txt file: ")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                color_string = line.strip()  
                if not color_string:  
                    continue
                if not draw_line_from_string(color_string, turta):  
                    print("Invalid color  in the file.")
                    break
                
                turta.penup()  
                new_y = new_y - pixel  
                turta.goto(x, new_y)  
                turta.pendown()  
    except FileNotFoundError:
        print("File not found")
        

