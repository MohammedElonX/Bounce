# Imported files
from tkinter import *
import random
import time

# Window
game = Tk()
game.title("Bounce")
game.resizable(0,0)
game.wm_attributes("-topmost", 1)
#game.iconbitmap(file="C:/Users/ISHAAQ MUHAMMAD/Desktop/bounce.png")

canvas = Canvas(game, width=500, height=500, bd=0, highlightthickness=5)
canvas.pack()

game.update()

# Classes
class Ball:
	def __init__(self, canvas, paddle, color):
		self.paddle = paddle
		self.canvas = canvas
		self.id = canvas.create_oval(10,10,25,25, fill = color)
		self.canvas.move(self.id, 245, 100)
		start = [-3,-2,-1,0,1,2,3]
		random.shuffle(start)
		self.x=start[0]
		self.y=-3
		self.canvas_width = self.canvas.winfo_width()
		self.canvas_height = self.canvas.winfo_height()
		self.hit_bottom = False

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
			return False

	def draw(self):
			self.canvas.move(self.id, self.x, self.y)
			pos = self.canvas.coords(self.id) # This returns a list(array) i/e[x1,y1,x2,y2]
			if pos[1] <= 0:
				self.y=3
			if pos[3] >= self.canvas_height:
				self.hit_bottom = True
				canvas.create_text(245,100, text="Game Over!")
			if pos[0] <= 0:
				self.x=3
			if pos[2] >= self.canvas_width:
				self.x=-3
			if self.hit_paddle(pos) == True:
				self.y=-3

class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas
		self.id = self.canvas.create_rectangle(0,0,100,10, fill=color)
		self.canvas.move(self.id, 200,450)
		self.x=0
		self.canvas_width = self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

	def draw(self):
		self.canvas.move(self.id, self.x, 0)
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x=0
		if pos [2] >= self.canvas_width:
			self.x=0

	def turn_left(self, event):
		self.x=-2

	def turn_right(self, evt):
		self.x=2


# Objects
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')


# Keeps app functionalities running 
while 1:
	if ball.hit_bottom == False:
		ball.draw()
		paddle.draw()
	try:
		game.update_idletasks()
		game.update()
		time.sleep(0.01)
	except:
		pass

game.update()

game.mainloop()
