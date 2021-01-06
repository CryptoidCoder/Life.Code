import tkinter as tk
import threading
seconds = 0
minutes = 0
hours = 0
days = 0

print("")
print("How many times faster than than real life (e.g. '10' means that for every 10 seconds in real life there would be 100 seconds in the game")
print("1 would mean it would be realtime - this would work more as a kind of life calendar.")

speed = int(input("I find up to 50 is okay: ")) #the amount of time faster than real world
speed = 1 / speed #how long it is to a minute in game



def clock():
	def Draw(seconds, minutes):
		frame=tk.Frame(root,width=100,height=100,relief='solid',bd=1)
		frame.place(x=10,y=10)

		secondslabel=tk.Label(frame,text='Seconds: ')
		secondstext=tk.Label(frame,text=seconds)

		minuteslabel=tk.Label(frame,text='Minutes: ')
		minutestext=tk.Label(frame,text=minutes)

		secondslabel.pack()
		secondstext.pack()

		minuteslabel.pack()
		minutestext.pack()

	def Refresher():
		global seconds
		global minutes
		global hours
		global days

		global speed

		seconds += 1

		if seconds == 60:
			minutes += 1
			seconds = 0

		elif minutes == 60:
			hours += 1
			minutes = 0

		Draw(seconds, minutes)
		threading.Timer(speed, Refresher).start()

	root=tk.Tk()
	root.title("Life Clock") 
	Refresher()
	root.mainloop()
	return seconds,' Seconds & ', minutes, 'Minutes'

time = clock()
print("You left when the clock was at: ", time)