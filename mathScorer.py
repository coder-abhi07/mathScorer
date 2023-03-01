import tkinter
import random
import time


score = 0
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
result = num1 + num2
timeleft = 30

def add():
    return num1 + num2

def mul():
    return num1 * num2

def div():
    return num1 // num2

def sub():
    return num1 - num2

operation = {'-' : sub, '/' : div, '*' : mul, '+' : add}
op = random.choice(list(operation.keys()))

def calculate(op):
    return operation[op]()

def start(event):
    if timeleft == 30:
        countdown()	 
    question()

def question():
    global score
    global timeleft
    
    if timeleft > 0:
        global num1, num2, result, operation
        
        
        e.focus_set()
        
        result = 0
        for i in e.get():
            if (i.isdigit()):
                result = result *10 + int(i)
        if (e.get()[0] == '-'):
            result *= -1

        actualResult = calculate(op)
        if result == actualResult:  
            score += 1
        else:
            score -= 1  
        label.config(text = "")
        label.config(fg = "red",text = str(num1)+ ' ' + op +" "+str(num2), font = ('Helvetica', 60))
        time.sleep(2)
        e.delete(0, tkinter.END)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)

        label.config(fg = "Black",text = str(num1)+ ' ' + op +" "+str(num2), font = ('Helvetica', 60))
        scoreLabel.config(text = "Score: " + str(score))


def countdown():

    global timeleft
    if timeleft > 0:

        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))
    
        timeLabel.after(1000, countdown)



root = tkinter.Tk()

root.maxsize = (400, 400)
root.minsize = (400, 400)



canvas = tkinter.Canvas(root, width=400, height=400,  highlightthickness = 0)
canvas.pack()
imgDir = r"C:\Users\monster pc\Downloads\mathImg.png"


background_image = tkinter.PhotoImage(file=imgDir)
canvas.create_image(0, 0, anchor=tkinter.NW, image=background_image)

instruction = tkinter.Label(root, text = "Type the solution and press enter",font = ('Helvetica', 15), highlightthickness=0, highlightbackground=None)

scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Helvetica', 20), highlightthickness=0, highlightbackground=None)
scoreLabel.pack()


timeLabel = tkinter.Label(root, text = "Time left: " + str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()



num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
label = tkinter.Label(root, font = ('Helvetica', 60))
label.config(text = str(num1)+ ' '+op + " "+str(num2))
label.pack()


e = tkinter.Entry(root)

e.pack()


e.focus_set()
canvas.create_window(200,50, window =instruction)
canvas.create_window(200, 80, window =scoreLabel)
canvas.create_window(200, 120, window = timeLabel)
canvas.create_window(200, 200, window = label)
canvas.create_window(200, 250, window = e)


while root.bind('<Return>', start):
    root.update()

