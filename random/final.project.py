import tkinter as tk

class game(tk.Frame):
    def __init__(self, master):
        super(game, self).__init__(master)
        self.lives = 3
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg,  )
        self.canvas.pack
        self.pack    
    pass


class Gameobject(object):
    def __init__(self, camvas, item):
        self.canvas = canvas
        self.item = item

    def get_postion(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item)

    def __init__(self, canvas, x, y, hits):
        #YOUDO-18:  create a width variable for self and initialize to 75
        #YOUDO-19:  create a height variable for self and initialize to 20
        #YOUDO-20:  create a hits variable for self and initialize to hits 
        color = Brick.COLORS[hits]
        #YOUDO-21:  create an x1 variable and set to x - self's width / 2
        #YOUDO-22:  create an y1 variable and set to y - self's height / 2
        #YOUDO-23:  create an x2 variable and set to x + self's width / 2
        #YOUDO-24:  create an y2 variable and set to y + self's height / 2
        #YOUDO-25:  use create_rectangle on canvas to create an item variable with x1, y1, x2, y2, color, tags="brick"        
        super(Brick, self).__init__(canvas, item)


        def hit(self):
        #YOUDO-26:  subtract one from self.hits
        #YOUDO-27:  check if self.hits is equal to 0.  If it is call self.delete().  If not 
        #YOUDO-27-part2:  call self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])
        pass #YOUDO-28:  Remove this pass    


if __name__ == "__main__":
    root = tk.Tk
    root.title("breakout")
    game = game(root)
    root.mainloop()



lives = 3
root = tk.tk()
frame = tk.frame(root)
frame.pack()
canvas.pack()
root.title("breakout")
root.mainloop()