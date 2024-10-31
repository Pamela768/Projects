from tkinter import *
import tkinter.ttk as ttk
from random import randint
from PIL import Image, ImageTk
from time import sleep

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Snakes & Ladders")

        # Create frames for different screens
        self.frame1 = Frame(self)
        self.frame2 = Frame(self)
    

        self.position = 0  # Player 1's position
        self.position2 = 0
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 93, 80: 99}
        self.snakes = {17: 7, 54: 34, 62: 18, 70: 37, 87: 45, 92: 73, 95: 77, 99: 79}

        # Buttons to switch between modes
        ttk.Button(self.frame1, text="Play Alone", command=lambda:(self.show_frame2(), self.button_pressed("alone"), self.player2_label.pack_forget())).pack(pady=10)
        ttk.Button(self.frame1, text="Play Against Computer", command= lambda:(self.show_frame2(), self.button_pressed("computer"), self.player2_label.pack(), self.show_player2())).pack(pady=10)
        self.player1_label= ttk.Label(self.frame2, text="Your position is 0" )
        self.player2_label = ttk.Label(self.frame2, text = "Opponent position is 0")
        self.player1_label.pack()
        self.player2_label.pack()
        self.dice = ttk.Button(self.frame2, text ="Dice", command = None )
        self.dice.pack(padx= 10)
        self.frame1.pack()

        # Load the board image
        image_path = r"C:\Users\Pamela\Documents\GTB\Project\S&Ls.py\download2.jpg"
        try:
            self.pic = ImageTk.PhotoImage(Image.open(image_path))  # Store as an instance variable
            self.canvas = Canvas(self.frame2, width=self.pic.width(), height=self.pic.height())
            self.canvas.create_image(0, 0, image=self.pic, anchor=NW)
            self.player1 = self.canvas.create_oval(7, 205, 17, 215, fill="blue")
            
            
           
            self.canvas.pack()
            print("Image loaded successfully!")
        except Exception as e:
            print(f"Error loading image: {e}")
        
        
      
        
        

        # Board coordinates
        self.board_mapping = {
           # Row 1 (Left to Right)
    1: (8, 215),  2: (31, 215),  3: (54, 215),  4: (77, 215),  5: (100, 215),
    6: (123, 215),  7: (146, 215),  8: (169, 215),  9: (192, 215),  10: (215, 215),

    # Row 2 (Right to Left)
    11: (215, 192),  12: (192, 192),  13: (169, 192),  14: (146, 192),  15: (123, 192),
    16: (100, 192),  17: (77, 192),  18: (54, 192),  19: (31, 192),  20: (8, 192),

    # Row 3 (Left to Right)
    21: (8, 169),  22: (31, 169),  23: (54, 169),  24: (77, 169),  25: (100, 169),
    26: (123, 169),  27: (146, 169),  28: (169, 169),  29: (192, 169),  30: (215, 169),

    # Row 4 (Right to Left)
    31: (215, 146),  32: (192, 146),  33: (169, 146),  34: (146, 146),  35: (123, 146),
    36: (100, 146),  37: (77, 146),  38: (54, 146),  39: (31, 146),  40: (8, 146),

    # Row 5 (Left to Right)
    41: (8, 123),  42: (31, 123),  43: (54, 123),  44: (77, 123),  45: (100, 123),
    46: (123, 123),  47: (146, 123),  48: (169, 123),  49: (192, 123),  50: (215, 123),

    # Row 6 (Right to Left)
    51: (215, 100),  52: (192, 100),  53: (169, 100),  54: (146, 100),  55: (123, 100),
    56: (100, 100),  57: (77, 100),  58: (54, 100),  59: (31, 100),  60: (8, 100),

    # Row 7 (Left to Right)
    61: (8, 77),  62: (31, 77),  63: (54, 77),  64: (77, 77),  65: (100, 77),
    66: (123, 77),  67: (146, 77),  68: (169, 77),  69: (192, 77),  70: (215, 77),

    # Row 8 (Right to Left)
    71: (215, 54),  72: (192, 54),  73: (169, 54),  74: (146, 54),  75: (123, 54),
    76: (100, 54),  77: (77, 54),  78: (54, 54),  79: (31, 54),  80: (8, 54),

    # Row 9 (Left to Right)
    81: (8, 31),  82: (31, 31),  83: (54, 31),  84: (77, 31),  85: (100, 31),
    86: (123, 31),  87: (146, 31),  88: (169, 31),  89: (192, 31),  90: (215, 31),

    # Row 10 (Right to Left)
    91: (215, 8),  92: (192, 8),  93: (169, 8),  94: (146, 8),  95: (123, 8),
    96: (100, 8),  97: (77, 8),  98: (54, 8),  99: (31, 8),  100: (8, 8)
        }
        

    def show_frame1(self):
        """Display the main menu."""
        self.frame1.pack()
        self.frame2.pack_forget()

    def show_frame2(self):
        """Switch to the individual game screen."""
        self.frame1.pack_forget()
        self.frame2.pack()
        
    

    def alone(self):
        """Play a turn for the individual player."""
        
        dice = randint(1, 6)
        print(f"Dice rolled to {dice}")
       
        # Calculate new position
        new_position = self.position + dice
        self.player1_label.config(text= f"You rolled a {dice}, Your position is now: {new_position}")


        if new_position > 100:
            print(f"You overshot 100! Stay at {self.position}")
            self.player1_label.config (text= f"You overshot 100! Stay at {self.position}")
        else:
            self.position = new_position

        # Check for ladders or snakes
        if self.position in self.ladders:
            self.player1_label.config (text= f"You landed on {self.position}. You have climbed to {self.ladders[self.position]}")
            self.position = self.ladders[self.position]
            print(f"You climbed a ladder to {self.position}")
            
            
        elif self.position in self.snakes:
            self.player1_label.config (text= f"You landed on {self.position}.  You have slid to {self.snakes[self.position]}")
            self.position = self.snakes[self.position]
            print(f"You slid down a snake to {self.position}")

        # Move the player's token
        x, y = self.board_mapping[self.position]
        self.canvas.coords(self.player1, x, y, x + 10, y + 10)

        # Check for win condition
        if self.position == 100:
            print("Player 1 has won!")
            self.player1_label.config(text= f"You won!!!")
            
            
    def show_player2(self):
            if not hasattr(self, 'player2'):
                self.player2 = self.canvas.create_oval(5, 212, 15, 222, fill="red")          
            
    def computer(self):
        dice = randint(1,6)
        dice_2 = randint(1,6)
        print(f'You rolled a {dice}')
        
        new_position = self.position + dice
        
        if new_position > 100:
            print(f"You overshot 100! Stay at {self.position}")
        else:
            self.position = new_position
        if self.position in self.ladders:
            self.position = self.ladders[self.position]
            print(f"You climes to {self.position}")
        elif self.position in self.snakes:
            self.position  = self.snakes[self.position]
            print(f"You slid down a snake to {self.position}")
        
        x, y = self.board_mapping[self.position]
        self.canvas.coords(self.player1, x, y, x + 10, y + 10)
        
       
         # Check for win condition
        if self.position == 100:
            print("Player 1 has won!")
        
        
        self.player1_label.config(text= f"You rolled a {dice}. Your position is now {new_position}")
            
            
            
        sleep(2)
        new_position2 = self.position2 + dice_2
        if new_position2 >100:
            print(f"Your opponent has overshot.  Stay at {self.position2}")
        else:
            self.position2 = new_position2
        if self.position2 in self.ladders:
            self.position2 = self.ladders[self.position2]
            print(f"Your opponent just climbed a ladder, They have moved to {self.position2}")
        elif self.position2 in self.snakes:
            self.position2  = self.snakes[self.position2]
            print(f"Your opponent slid down a snake to {self.position2}")
        
    
        a,b = self.board_mapping[self.position2]
        self.canvas.coords(self.player2, a+2, b+2, a+ 12, b + 12)
        
         # Check for win condition
        if self.position2 == 100:
            print("Your opponent has won, You have lost")

        
        self.player2_label.config(text= f"Your opponent's rolled a {dice}. Your opponent position is {new_position2}")
            
            
    def button_pressed(self, mode):
        """Handle button press and perform actions based on mode."""
        if mode == "alone":
            self.dice.config(command=self.alone)
        elif mode == "computer":
            self.dice.config(command=self.computer)
           

# Run the app
app = MyApp()
app.mainloop()
