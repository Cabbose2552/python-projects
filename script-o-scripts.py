import time
import random
import cv2
import gens
import mathops
import testops

from tkinter import *

pyver = '3.10.2'
version = '1.0.0'
pcnt = 1
cnt = 1
mult = 2
multnum = 1

while True:
        script = input("what script would you like? type list to display a list of scripts:")

        if script == ("list"):
                print("-----------------------------------------------------------------")
                print("|link, plays a simple blinking animation                        |")
                print("|                                                               |")
                print("|cnt, counts to infinity                                        |")
                print("|                                                               |")
                print("|pcnt, displays prime numbers to infinity(wip)                  |")
                print("|                                                               |")
                print("|mult, displays numbers multiplied by the entered value         |")
                print("|                                                               |")
                print("|stress-test-1/2, provides a simple stress test for your system.|")
                print("|                                                               |")
                print("|win, creates a window with the entered mesurements             |")
                print("|                                                               |")
                print("|xgen, generates a random xbox gift card code                   |")
                print("|                                                               |")
                print("|pgen, generates a random playstation gift card code            |")
                print("|                                                               |")
                print("|sgen, generates a random steam gift card code                  |")
                print("-----------------------------------------------------------------")

        elif script == "cnt":
            while True:
                cnt = cnt + 1
                print(cnt)

        elif script == ("xgen"):
                print("")
                nn = input("how many codes would you like:")
                print("")
                n = int(nn)
                def g(rolls):
                        data = "qwrtypdfghjkzxcvbnm2346789"
                        result = ""
                        while rolls >= 1:
                            c = random.choice(data)
                            result = c + result
                            rolls = rolls - 1
                        return result

                for x in range(n):
                        print(g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5))
                print("")
        elif script == ("sgen"):
                print("")
                nn = input("how many codes would you like:")
                print("")
                n = int(nn)
                def g(rolls):
                        data = "qwrtypdfghjkzxcvbnm2346789"
                        result = ""
                        while rolls >= 1:
                            c = random.choice(data)
                            result = c + result
                            rolls = rolls - 1
                        return result

                for x in range(n):
                        print(g(4)+"-"+g(6)+"-"+g(5))
                print("")
        elif script == ("pgen"):
                print("")
                nn = input("how many codes would you like:")
                print("")
                n = int(nn)
                def g(rolls):
                        data = "qwrtypdfghjkzxcvbnm234678923467892346789"
                        result = ""
                        while rolls >= 1:
                            c = random.choice(data)
                            result = c + result
                            rolls = rolls - 1
                        return result

                for x in range(n):
                        print(g(4)+"-"+g(4)+"-"+g(4))
                print("")

        elif script == ("mult"):
            print("")
            multnum = input("enternumber to mupltiply by:")
            print("")
            multnumint = int(multnum)
            while True:
                mult= mult * multnumint
                print(mult)

        elif script == ("info"):
                print("======================")
                print("author: nathan nolan||")
                print("======================")
                print("version:", version, "     ||")
                print("======================")
                print("python ver:", pyver, " ||")
                print("======================")
                
        elif script == ("stress-test-1"):
            while True:
                mult= mult * 99999999999
                print(mult)
                
        elif script == ("stress-test-2"):
            while True:
                mult= mult * mult
                print(mult)

        elif script == ("blink"):
                for x in range(10):
                        print("-w-")
                        time.sleep(0.1)
                        print("owo")
                        time.sleep(0.1)
                        print("OwO")
                        time.sleep(0.1)
                        print("owo")
                        time.sleep(0.1)

        elif script == ("pcnt"):
            print("this is a work in progress")
            
        elif script == ("clear"):
            for x in range(40):
                    print("")

        elif script == ("win"):
            winw = input("window width:")
            winh = input("window height:")
            # declare the window
            window = Tk()
            # set window title
            window.title("Python GUI App")
            # set window width and height
            window.configure(width=winw, height=winh)
            # set window background color
            window.configure(bg='lightblue')
            window.mainloop()

        elif script == ("penis") or ("dick") or ("cock") or ("balls"):
                print("tee hee, thats a bad word")

        else:
            print("######################")
            print("#error invalid target#")
            print("######################")

