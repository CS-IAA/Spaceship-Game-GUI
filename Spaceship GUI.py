'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Spaceship Game(GUI)
Version .1
'''

global count #to make sure that planet code entrable only on the first planet departure
count = 0
global counter #num of planets
counter = 0
global score #highscore
score = 0

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo #popup

root = Tk() #creates GUI
root.title("Spaceship Game") #title

def about():
    messagebox.showinfo("Version .1", "In this game, you will be exploring planets to earn as many points as possible \
to win!\n\
If you are successful, then you can become a self-proclaimed hero! However, if you lose...\n\
Please remember to enter the correct weight and speed of the ship!\n\
Enjoy!")

def hel():
    messagebox.showinfo("Help", "Please select a country to which you would like to travel to and enter your name into the entry widget. Please remember that the velocity \
you enter is the velocity it takes to get off of the planet that you are located in. You are not entering in your requested planet's velocity because you are not on that planet. \
You get only one time to enter in a planet code which is at the begenning of the game when you first press the launch button. After that, it is locked and can no longer be accessible. \
Your name is also locked after you first enter it in. The rest of the widgets remain unlocked throughout the game and the locked ones are only unlocked at the end of the game, which is \
your death.")

def check0():
    global count
    global uname
    uname = name.get("1.0", END)
    uname = uname.replace("\n", "", 1)  # gets rid of the FIRST new line after the uname.get
    count += 1
    planetc = pcode.get("1.0", END) #gets what user typed in as planet code
    planetc = planetc.replace("\n", "", 1)  # gets rid of the FIRST new line after the pcode.get
    if count > 1:
        pcode.config(state=DISABLED) #disables planet code. only first time possible.
        check()
    else:
        pcode.delete("1.0", END)  # deletes given planet code from textbox
        pcode.config(state=DISABLED) #disables it so it cant be used again
        if planetc == "Torch":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Mercury")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Mercury!\nThe planet code is Torch.") #messagebox popup
        elif planetc == "Sunset":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Venus")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Venus!\nThe planet code is Sunset.") #messagebox popsup
        elif planetc == "Nova":
            #messagebox popsup
            showinfo("Location", "Sorry, but you are already on Earth. Please try another planet code or start anew.")
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            pcode.config(state=NORMAL) #makes planet code writable by user so they can try again
            count = 0  # so that count wont be greater than 1
            #gives user another oppurtnity to enter planet code
        elif planetc == "Redy":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Mars")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Mars!\nThe planet code is Redy.")
        elif planetc == "Colossal":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Jupiter")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Jupiter!\nThe planet code is Colossal.")
        elif planetc == "Ringy":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Saturn")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Saturn!\nThe planet code is Ringy.")#messagebox with planet and planet code
        elif planetc == "Aqua":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Uranus")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Uranus!\nThe planet code is Aqua.") #messagebox with planet and planet code
        elif planetc == "Mystic":
            PC.config(state=NORMAL)  # makes normal so location can be edited
            PC.delete("1.0", END)  # deletes given planet location from textbox
            PC.insert(END, "Neptune")  # adds planet location into text widget
            PC.config(state=DISABLED) #disables again so it is only read-only
            box1.select_clear(0, END)  # clears planet choice
            name.config(state=NORMAL)  # makes normal so location can be edited
            name.delete("1.0", END)  # deletes given planet location from textbox
            name.insert(END, "")  # adds planet location into text widget
            velocity.set('')  # clears velocity
            weight.set('')  # clears weight
            showinfo("Location", "Welcome to Neptune!\nThe planet code is Mystic.")
        else: #if they do wrong code
            if planetc == "": #so that on first try they click launch w/o typing ANYTHING it doesnt say wrong planet cod
                pcode.config(state=DISABLED)  # disables planet code. only first time possible.
                check()
            else:
                showinfo("Location","Sorry, but that is the wrong planet code. Please try another again or start anew.")
                box1.select_clear(0, END)  # clears planet choice
                name.config(state=NORMAL)  # makes normal so location can be edited
                name.delete("1.0", END)  # deletes given planet location from textbox
                name.insert(END, "")  # adds planet location into text widget
                velocity.set('')  # clears velocity
                weight.set('')  # clears weight
                pcode.config(state=NORMAL) #makes planet code writable by user since they did wrong one
                count = 0 #so that count wont be greater than 1


def check():
    # checks to make sure that the user has done everything before writing to a file
    if len(box1.curselection()):
        if len(name.get("1.0","end-1c")) > 0:
            if len(velocity.get()):
                if len(weight.get()):
                    # only if user completes everything
                    data()
                else:
                    showinfo("Error", "Please enter in all of the information!") #popup if they dont enter something
            else:
                showinfo("Error", "Please enter in all of the information!")  # popup if they dont enter something
        else:
            showinfo("Error", "Please enter in all of the information!")  # popup if they dont enter something
    else:
        showinfo("Error", "Please enter in all of the information!")  # popup if they dont enter something

def data():
    name.config(state=DISABLED) #disables so another name cant be written midway through game
    PC.config(state=NORMAL)  # makes normal so location can be edited
    PCP = PC.get("1.0", END)
    PCP = PCP.replace("\n", "", 1)
    PC.config(state=DISABLED)
    #checks to see what planet location they are at.
    if PCP == "Earth":
        Earth() #takes user to earth where it sees if entered velocity/weight is enough to take off
    elif PCP == "Mercury":
        Mercury()
    elif PCP == "Venus":
        Venus()
    elif PCP == "Mars":
        Mars()
    elif PCP == "Jupiter":
        Jupiter()
    elif PCP == "Saturn":
        Saturn()
    elif PCP == "Uranus":
        Uranus()
    elif PCP == "Neptune":
        Neptune()

def placement():
    global counter
    global score
    global uname
    global count

    outfile = open("highscores.txt", "a")
    file = (uname + ' ' + str(score)+'\n')
    outfile.write(file)
    outfile.close()
    infile = open("highscores.txt", "r")
    content = infile.readlines()
    content = [x.strip() for x in content] # creates a list with the users in differnet elements(have commas seperating)
    z = sorted(content, key = lambda x: int(x.split(" ")[1]), reverse = True)
    new1 = " ".join(z[:1])
    new2 = " ".join(z[1:2])
    new3 = " ".join(z[2:3])

    showinfo('High Scores', "\t" + "TOP 3 HIGH SCORES\n===========================\n" + new1+"\n"+new2+'\n'+new3)
    infile.close()

    box1.select_clear(0, END)  # clears planet choice
    name.config(state=NORMAL)  # makes normal so location can be edited
    name.delete("1.0", END)  # deletes given planet location from textbox
    name.insert(END, "")  # adds planet location into text widget
    velocity.set('')  # clears velocity
    weight.set('')  # clears weight
    PC.config(state=NORMAL)  # makes normal so location can be edited
    PC.delete("1.0", END)  # deletes given planet location from textbox
    PC.insert(END, "Earth")  # adds text into text widget
    PC.config(state=DISABLED)
    pcode.config(state=NORMAL)  # makes planet code writable by user
    count = 0  # so that count wont be greater than 1
    counter = 0 #sets planets visited back to zero since they died
    score = 0

def Earth():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Earth")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Earth":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0: #incase they enter a negative number
                if float(velocity.get()) > 13:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 9:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location","Welcome to " +plan+"!\nThe planet code is "+planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup


    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a positive number for velocity and weight.") #popup

def Mercury():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Mercury")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Mercury":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 5:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 2:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup


    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

def Venus():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Venus")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Venus":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 12:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 8:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds textbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup

    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

def Mars():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Mars")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Mars":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get())>= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 8:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 4:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup

    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

def Jupiter():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Jupiter")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Jupiter":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 69:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 65:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup

    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

def Saturn():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Saturn")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Saturn":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 41:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 37:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup

    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

def Uranus():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Uranus")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Uranus":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 24:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 20:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup

    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

def Neptune():
    try:
        global count
        global counter
        global score
        #changes to their current location
        PC.config(state=NORMAL)  # makes normal so location can be edited
        PC.delete("1.0", END)  # deletes given planet location from textbox
        PC.insert(END, "Neptune")  # adds text into text widget
        PC.config(state=DISABLED)
        plan = box1.get(ANCHOR)
        if plan == "Neptune":
            showinfo("Error", "Sorry, but you are already on this planet. Please choose another planet.")  # popup
        else:
            if float(weight.get()) >= 0 and float(velocity.get()) >= 0:
                if float(velocity.get()) > 33:
                    showinfo("Error", "I'm sorry, you were too fast and have crashed. Please try again!")  # popup
                    placement()
                elif float(velocity.get()) < 29:
                    showinfo("Error", "I'm sorry, you were too slow and have crashed. Please try again!")
                    placement()
                else:
                    showinfo("Location", "Welcome to " + plan + "!\nThe planet code is " + planet_d[plan])
                    PC.config(state=NORMAL)  # makes normal so location can be edited
                    PC.delete("1.0", END)  # deletes given planet location from textbox
                    PC.insert(END, box1.get(ANCHOR))  # adds listbox choice into text widget
                    PC.config(state=DISABLED)
                    box1.select_clear(0, END)  # clears planet choice
                    velocity.set('')  # clears velocity
                    weight.set('')  # clears weight
                    counter += 1
                    score = counter * 100 + score
            else:
                showinfo("Error", "Please enter only a positive number for velocity and weight.")  # popup

    except ValueError: #so user wont to non-integer for velocity,weight
        showinfo("Error", "Please enter only a number for velocity and weight.")  # popup

root.option_add('*tearOff', FALSE) #gets rid of dashed line
menu = Menu(root) #creates menu
root.config(menu=menu) #adds ability to create options

subMenu = Menu(menu) #creats submenu
menu.add_cascade(label="File", menu=subMenu) # creates a memu option
subMenu.add_command(label="Exit", command=root.destroy) #file option

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu) #creates another memu option
helpMenu.add_command(label="About", command=about) #file option
helpMenu.add_command(label="Help", command=hel) #file option

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

velocity = StringVar()
weight = StringVar()
code = StringVar()

planet_l= ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']#list of planets
planet_d ={'Mercury': "Torch", 'Venus': "Sunset", 'Earth': "Nova", 'Mars': "Redy", 'Jupiter': "Colossal", \
           'Saturn': "Ringy", 'Uranus': "Aqua", 'Neptune': "Mystic"}
planet = StringVar(value=planet_l)

box1 = Listbox(mainframe, height=5, listvariable=planet, exportselection=0) #planets
box1.grid(column = 1, row = 2, sticky = (N,W,E,S))
#creates listbox which has all the planets. listvariable acceses the planets and adds to listbox

s = ttk.Scrollbar(mainframe, orient=VERTICAL, command=box1.yview) #creating a scroll bar for the listbox(box1)
s.grid(column=1, row=2, sticky=(N,S,E))
box1['yscrollcommand'] = s.set #makes the scroll moveable

ttk.Label(mainframe, text="Planets").grid(column=1, row=1, sticky = (N,W)) #Planet tag

#labels which is name, velocity, weight to left of the entry widgets
ttk.Label(mainframe, text="Name").grid(column=2, row=1, sticky=(N,W))
ttk.Label(mainframe, text="Velocity").grid(column=2, row=2, sticky=(N,W))
ttk.Label(mainframe, text="Weight").grid(column=2, row=2, sticky=W)

ttk.Label(mainframe, text="Location").grid(column=2, row=2, sticky=(S,W)) #labels location of the planet
ttk.Label(mainframe, text="Planet Code").grid(column=2, row=3, sticky=W) #labels planet code area

PC = Text(mainframe,wrap=WORD, width=11, height=1)
#text widget that has location of planet. wrap makes sure that a word doesn't strech onto more than one line
PC.grid(column=3, row = 2, sticky=(S,W)) #graph on diff line else "no index"
PC.insert(END, "Earth") #adds text into text widget
PC.config(state = DISABLED)

name = Text(mainframe,wrap=WORD, width=11, height=1)
#text widget that has location of planet. wrap makes sure that a word doesn't strech onto more than one line
name.grid(column=3, row=1, sticky=(N,W)) #graph on diff line else "no index"
name.insert(END, "") #adds text into text widget

#user enters their chosen velocity and weight into the entry widgets
ttk.Entry(mainframe, width=15, textvariable=velocity).grid(column=3, row=2, sticky=(N,W))
ttk.Entry(mainframe, width=15, textvariable=weight).grid(column=3, row=2, sticky=W)

pcode = Text(mainframe,wrap=WORD, width=11, height=1)
#text widget where user enters their planet code. wrap makes sure that a word doesn't strech onto more than one line
pcode.grid(column=3, row=3, sticky=W)
pcode.insert(END, "") #adds text into text widget
pcode.grid(column=3, row=3, sticky=W)

ttk.Button(mainframe, text="Launch", command=check0).grid(column=1, row=3, sticky = (N,W)) #takes to launch function

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#continues the loop
root.mainloop()
