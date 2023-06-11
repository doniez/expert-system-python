from difflib import *
import  csv
import tkinter as tk
from tkinter import font


def btn_clicked():
    canvas.delete("wlcmmsg")
    canvas.delete("choix1")
    canvas.delete("choix2")
    canvas.delete("choix3")
    canvas.delete("choixinput")
    
    
    choice = int(choix1input.get())

    if choice == 1:
        list_country()

    elif choice == 2:
        expertSystem()

    elif choice == 3:
        exit()

    else:
        print(choice)
        print("Invalid option.")

    
def btn_clickedlv2():
    print(int(choix1input.get()))
    global a
    a = int(choix1input.get())
    window.destroy()


def select():   
    canvas.create_text(
        610.0, 35.0,
        text = "Expert system",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(36.0)))


    canvas.create_text(
        577.5, 85.0,
        text = "Welcome to the Geographic Information Expert System!",
        fill = "#64d86b",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('wlcmmsg',))


    canvas.create_text(
        577.5, 135.0,
        text = "1. List the countries.",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix1',))

    canvas.create_text(
        577.5, 185.0,
        text = "2. Ask our Expert system for suggestions to LIVE, WORK or TRAVEL in different countries",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix2',))

    canvas.create_text(
        577.5, 235.0,
        text = "3. Exit",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix3',)
        )


    canvas.create_text(
        577.5, 400.0,
        text = "choice=",
        fill = "#64d86b",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choixlabel',)
        )


    global choix1input;
    choix1input=tk.Entry( font="15",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
    )

    choix1input.place(
        x = 625, y = 385,
        width = 30,
        height = 28)


    button_img_0 = tk.PhotoImage(file = f"button_img_0.png")
    button_text_font_0 = font.Font(family='Roboto-Black', size=int(13.0))
    global b0
    b0 = tk.Button(
        image = button_img_0,
        text = 'Next',
        compound = 'center',
        fg = '#ffffff',
        font = button_text_font_0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = 'flat')

    b0.place(
        x = 532, y = 460,
        width = 156,
        height = 52)
    #window.resizable(False, False)
    window.mainloop()

    


def list_country():
    canvas.delete("choixlabel")
    choix1input.destroy()
    b0.destroy()
    
    file = open("countryList.txt", "r")
    count = 0
    canvas.create_text(
        577.5, 85.0,
        text = "The countries you can go to are:",
        fill = "#64d86b",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('countrylisttitle',))

    i=150 
    j=0
    for line in file:
        
        con = line[0:]
        count += 1
        if(count%5==0):
            i+=50
            j=0
        
        
    
        print(str(count) + '.', con.upper(),)
        canvas.create_text(
        150+(j*200), i,
        text = con.upper(),
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('countrylisttitle',))
        j+=1

    
        
    

def liveSuggestion(countryDetails):
    l = []
    c = []

    print("What kind of Population Desnity do you prefer?\n1.High\n2.Low\n")
    b = int(input())
    if(b == 1):
        l.append("high")
    elif(b == 2):
        l.append("low")
    else:
        print("Invalid selection")
        exit()

    print("What kind of Climate do you prefer?\n1.Cold\n2.Moderate\n3.Hot\n")
    c = int(input())
    if(c == 1):
        l.append("cold")
    elif(c == 2):
        l.append("moderate")
    elif(c ==3):
        l.append("hot")
    else:
        print("Invalid selection")
        exit()

    print("What kind of Government do you prefer?\n1.Democracy\n2.Communist\n3.Monarchy\n4.Republic\n5.Federal")
    g = int(input())
    if(g == 1):
        l.append("democracy")
    elif(g == 2):
        l.append("communist")
    elif(g ==3):
        l.append("monarchy")
    elif(g == 4):
        l.append("republic")
    elif(g ==5):
        l.append("federal")
    else:
        print("Invalid selection")
        exit()

    print("What is your religion?\n1.Christianity\n2.Buddhism\n3.Hinduism\n4.Islam\n5.Atheist")
    r = int(input())
    if(r == 1):
        l.append("christianity")
    elif(r == 2):
        l.append("buddhism")
    elif(r ==3):
        l.append("hinduism")
    elif(r == 4):
        l.append("islam")
    elif(r ==5):
        l.append("atheist")
    else:
        print("Invalid selection")
        exit()

    possibleCountry = []
    for item in countryDetails:
        if countryDetails[item]["average weather"] == l[1] and countryDetails[item]["type of government"] == l[2] and countryDetails[item]["major religion"] == l[3]:
            possibleCountry.append(item)

    if possibleCountry != []:
        window = tk.Tk()
        window.geometry("1220x660")
        window.configure(bg = "#ffffff")
        canvas = tk.Canvas(
            window,
            bg = "#ffffff",
            height = 660,
            width = 1220,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        print("Your possible choices are: ")
        canvas.create_text(
            577.5, 85.0,
            text = "Your possible choices are:",
            fill = "#64d86b",
            font = ("Comfortaa-Regular", int(20.0)),
            tags=('wlcmmsg',))

        j=135.0
        for item in possibleCountry:
            canvas.create_text(
            577.5, j,
            text = item.upper(),
            fill = "#000000",
            font = ("Comfortaa-Regular", int(20.0)),
            tags=('wlcmmsg',))
            j+=50
            print(item.upper())
    else:
        print("Such a rare combination is not available among the top 40 rich countries of the world!")

def workSuggestion(countryDetails):
    x = int(input('What is your work preference?:\n1. Business\n2. Job\n'))
    wp = False #Work preference F: Business T: Job
    ie = False #F: Import  T: Export
    fdomain = 0
    jobtype = 0    # 1: Startup 2: Local business 3: MNC
    l = []
    if x == 1:

        wp = False
        xa = int(input('Choose the type of trade:\n1.Imports\n2.Exports\n'))

        if xa == 1:
            l.append("import")

        elif xa == 2:
            l.append("export")

        else:
            print("Wrong input")

        print("Your field:")
        fdomain = int(input('1. Technology\n2. Manufacturing\n3. Tourism\n4. Infrastructure\n'))
        if fdomain == 1:
            l.append("technology")

        elif fdomain == 2:
            l.append("manufacturing")

        elif fdomain == 3:
            l.append("tourism")

        elif fdomain == 4:
            l.append("infrastructure")

        else:
            print("Wrong input")
            exit()

        possibleCountry = []
        for item in countryDetails:
            if countryDetails[item]["trade type"] == l[0] and countryDetails[item]["field domain"] == l[1]:

                possibleCountry.append(item)

        if possibleCountry != []:
            print("Your possible choices are: ")
            window = tk.Tk()
            window.geometry("1220x660")
            window.configure(bg = "#ffffff")
            canvas = tk.Canvas(
                window,
                bg = "#ffffff",
                height = 660,
                width = 1220,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)
            canvas.create_text(
                577.5, 85.0,
                text = "Your possible choices are:",
                fill = "#64d86b",
                font = ("Comfortaa-Regular", int(20.0)),
                tags=('wlcmmsg',))

            j=135.0
            for item in possibleCountry:
                canvas.create_text(
                577.5, j,
                text = item.upper(),
                fill = "#000000",
                font = ("Comfortaa-Regular", int(20.0)),
                tags=('wlcmmsg',))
                j+=50
                print(item.upper())
                for item in possibleCountry:
                    print(item.upper())
        else:
            print("Such a rare combination is not available among the top 40 rich countries of the world!")

    elif x == 2:
        l = []
        wp = True
        print("Your field:")
        fdomain = int(input('1. Technology\n2. Manufacturing\n3. Tourism\n4. Infrastructure\n'))

        if fdomain == 1:
            l.append("technology")

        elif fdomain == 2:
            l.append("manufacturing")

        elif fdomain == 3:
            l.append("tourism")

        elif fdomain == 4:
            l.append("infrastructure")

        else:
            print("Wrong input")
            exit()

        possibleCountry = []
        for item in countryDetails:
            if countryDetails[item]["field domain"] == l[0]:

                possibleCountry.append(item)

        if possibleCountry != []:
            print("Your possible choices are: ")
            window = tk.Tk()
            window.geometry("1220x660")
            window.configure(bg = "#ffffff")
            canvas = tk.Canvas(
                window,
                bg = "#ffffff",
                height = 660,
                width = 1220,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            canvas.place(x = 0, y = 0)
            canvas.create_text(
                577.5, 85.0,
                text = "Your possible choices are:",
                fill = "#64d86b",
                font = ("Comfortaa-Regular", int(20.0)),
                tags=('wlcmmsg',))

            j=135.0
            for item in possibleCountry:
                canvas.create_text(
                577.5, j,
                text = item.upper(),
                fill = "#000000",
                font = ("Comfortaa-Regular", int(20.0)),
                tags=('wlcmmsg',))
                j+=50
                print(item.upper())
                for item in possibleCountry:
                    print(item.upper())
        else:
            print("Such a rare combination is not available among the top 40 rich countries of the world!")
    else:
        print("wrong input")
        exit()

def tourismSuggestion():
    tourism = {}
    placeList = []
    f = open("Tourism.csv")
    try:
        reader = csv.reader(f)
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].lower()
            placeList.append(row)
    finally:
        f.close()

    l = len(placeList)
    for i in range(1, l):
        tourism[placeList[i][0]] = {}

    for i in range(1, l):
        for j in range(len(placeList[0])):
            if placeList[0][j] != "" and placeList[i][j] != "":
                tourism[placeList[i][0]][placeList[0][j]] = placeList[i][j]

    l = []

    print("What is your total budget (per person) ?\n1. Under 3,800 Tunisian Dinar\n2. Between 3,800 and 7600 Tunisian Dinar\n3. Above 7600 Tunisian Dinar\n")

    c = int(input())
    if(c == 1):
        l.append(1900)
    elif(c == 2):
        l.append(5700)
    elif(c ==3):
        l.append(9500)
    else:
        print("Invalid option")
        exit()

    print("What type of place do you wanna go?\n1. Historical Place\n2. Hill Station\n3. Desert Safari\n4. Beaches\n")

    p = int(input())

    if(p == 1):
        l.append("historical")
    elif(p == 2):
        l.append("hill station")
    elif(p ==3):
        l.append("desert")
    elif(p == 4):
        l.append("beach")
    else:
        print("Invalid option")
        exit()

    window = tk.Tk()
    window.geometry("1220x660")
    window.configure(bg = "#ffffff")
    canvas = tk.Canvas(
        window,
        bg = "#ffffff",
        height = 660,
        width = 1220,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    canvas.create_text(
        577.5, 85.0,
        text = "The top places you can visit are",
        fill = "#64d86b",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('wlcmmsg',))

    j=135.0
    for item in tourism:
        if float(tourism[item]["budget"]) == l[0] and tourism[item]["type of place"] == l[1]:
            ch=item.upper() + ","+tourism[item]["country"].upper()
            canvas.create_text(
            577.5, j,
            text = ch ,
            fill = "#000000",
            font = ("Comfortaa-Regular", int(20.0)),
            tags=('wlcmmsg',))
            j+=50

def askQuestion(countryDetails):

    canvas.create_text(
        577.5, 85.0,
        text = "Choose the question you want to ask:",
        fill = "#64d86b",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('wlcmmsg',))


    canvas.create_text(
        577.5, 135.0,
        text = "1. I want to migrate to another country.",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix1',))

    canvas.create_text(
        577.5, 185.0,
        text = "2. I want to work in a country where I can earn most money. Where should I go?",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix2',))

    canvas.create_text(
        577.5, 235.0,
        text = "3 . I want to travel to exotic places in the world. Can you suggest me some?",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix3',)
        )
    
    canvas.create_text(
        577.5, 285.0,
        text = "4 .Exit",
        fill = "#000000",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choix3',)
        )


    canvas.create_text(
        577.5, 400.0,
        text = "choice=",
        fill = "#64d86b",
        font = ("Comfortaa-Regular", int(20.0)),
        tags=('choixlabel',)
        )


    global choix1input;
    choix1input=tk.Entry( font="15",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
    )

    choix1input.place(
        x = 625, y = 385,
        width = 30,
        height = 28)


    button_img_0 = tk.PhotoImage(file = f"button_img_0.png")
    button_text_font_0 = font.Font(family='Roboto-Black', size=int(13.0))
    global b0
    b0 = tk.Button(
        image = button_img_0,
        text = 'Next',
        compound = 'center',
        fg = '#ffffff',
        font = button_text_font_0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clickedlv2,
        relief = 'flat')

    b0.place(
        x = 532, y = 460,
        width = 156,
        height = 52)
    window.mainloop()

    if(a == 1):
        liveSuggestion(countryDetails)
    elif(a == 2):
        workSuggestion(countryDetails)
    elif(a ==3):
        tourismSuggestion()
    elif(a==4):
        exit()
    else:
        print("Invalid option!")

def expertSystem():
    countryDetails = {}
    countryList = []
    f = open("countries.csv")
    try:
        reader = csv.reader(f)
        for row in reader:
            for i in range(len(row)):
                row[i] = row[i].lower()
            countryList.append(row)
    finally:
        f.close()

    l = len(countryList)
    for i in range(1, l):
        countryDetails[countryList[i][0]] = {}

    for i in range(1, l):
        for j in range(len(countryList[0])):
            if countryList[0][j] != "" and countryList[i][j] != "":
                countryDetails[countryList[i][0]][countryList[0][j]] = countryList[i][j]

    askQuestion(countryDetails)

window = tk.Tk()
window.geometry("1220x660")
window.configure(bg = "#ffffff")
canvas = tk.Canvas(
    window,
    bg = "#ffffff",
    height = 660,
    width = 1220,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
select()