#Setting up the Modules
import tkinter as tk         #Tkinter Modules
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

import csv                   #Csv and graph Modules
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from PIL import Image        #Other Modules   
from collections import Counter
import random
import time
import os
import math

def reset():                 #Function to clear and reset the frames (Tabs)

    main_window.unbind("<KeyPress>")            #Unbinding the start timer keybind
    main_window.unbind(dnfbind)                 #Unbinding all the keybinds
    main_window.unbind(addbind)
    main_window.unbind(deletebind)
    main_window.unbind(okbind)

    def resetting(frame):                       #Function to delete the frame
        for widget in frame.winfo_children():   #Clearing the Frame
            widget.destroy()
        frame.place_forget()                    #Deleting the Frame

    resetting(timer_frame)                      #Resetting every frame
    resetting(stats_frame)
    resetting(times_frame)
    resetting(session_frame)
    resetting(settings_frame)
    
def SettingsGUI():           #Function for settings interface                                   (SETTINGS INTERFACE)

    reset()                                                                                 #Removing the previous Frames

    settings_frame.place(relx = 0.55, rely = 0.5, relheight=1, relwidth=0.9, anchor=CENTER) #Creating the settings intenrface frame

    #Creating the frames - Settings and themes
    themes_frame = ctk.CTkScrollableFrame(settings_frame, fg_color = framecolour,
                    scrollbar_button_color = navcolour, scrollbar_button_hover_color = backgroundcolour)
    themes_frame.place(relx=0.335, rely=0.5, relheight=0.87, relwidth=0.6, anchor=CENTER)

    themes_frame.grid_columnconfigure(0, weight=1)                                          #Making the gridding adjust to frame size
    themes_frame.grid_columnconfigure(1, weight=8)
    themes_frame.grid_columnconfigure(2, weight=8)
    themes_frame.grid_columnconfigure(3, weight=8)
    themes_frame.grid_columnconfigure(4, weight=8)
    themes_frame.grid_columnconfigure(5, weight=8)

    settingschoosing_frame = ctk.CTkFrame(settings_frame, fg_color = framecolour, height=390, width=260)
    settingschoosing_frame.place(relx=0.815, rely=0.5, relheight=0.87, relwidth=0.3, anchor=CENTER)
    
    def settings():                             #Function for settings

        settingsfile = pd.read_csv("Users_Settings.csv")                                    #Reading the settings file

        ctk.CTkLabel(settingschoosing_frame,  text="Settings",                              #Creating the settings title label
                    font = ctk.CTkFont(family = "Calibri", size=20, weight="bold"),
                    fg_color = framecolour, text_color=titletextcolour
                    ).place(relx=0.5, rely=0.07, anchor=CENTER)
        
        validitylabel = ctk.CTkLabel(settingschoosing_frame, text = "", height = 3,         #Creating the validity label
                        font = ctk.CTkFont(family = "Calibri", size=10, weight="bold"),
                        fg_color = framecolour, text_color=validitytext)  
        validitylabel.place(relx=0.5, rely=0.13, anchor=CENTER)


        """Function for changing the scramble sizes"""

        def ScrambleSizes():                    #Function for changing the scramble sizes
            ttk.Separator(settingschoosing_frame, orient = 'horizontal', style='background.TSeparator'
                  ).place(relx=0.5, rely=0.16, anchor=CENTER, relwidth=0.81)                #Seperator

            ctk.CTkLabel(settingschoosing_frame, text = "Scramble Sizes", fg_color = framecolour, text_color=statstextcolour,
                    font = ctk.CTkFont(family = "Calibri", size=12, weight="bold")).place(relx=0.5, rely=0.2, anchor=CENTER)


            """3x3 Scramble Size"""

            threesize = ctk.CTkLabel(settingschoosing_frame, text_color=statstextcolour,    #Label for 3x3
                        text = ("3x3: "+str(scramble_three_size)), fg_color = framecolour,
                        font = ctk.CTkFont(family = "Calibri", size=15))
            threesize.place(relx=0.14, rely=0.26, anchor=W)

            def threeslider_event(value):       #Function to change the scramble size
                global scramble_three_size
                scramble_three_size = settingsfile.iloc[0, 1] = int(value)                  #Changing the scramble sizes
                settingsfile.to_csv("Users_Settings.csv", index=False)
                threesize.configure(text = ("3x3: "+str(scramble_three_size)))              #Updating the Label

            varthree = IntVar()                                                             #Creating a variable for the slide
            varthree.set(scramble_three_size)                                               #Setting the slider to the current scramble size

            ctk.CTkSlider(settingschoosing_frame, command=threeslider_event, button_color = navcolour,
                          width=100, number_of_steps=15, variable = varthree, from_=15, to=30,
                          progress_color = buttoncolour, button_hover_color = hovercolour
                        ).place(relx=0.5, rely=0.26, anchor=W)                              #Creating the slider for the 3x3 scramble size
            

            """2x2 Scramble Size"""

            twosize = ctk.CTkLabel(settingschoosing_frame, text_color=statstextcolour,      #Label for 2x2
                        text = ("2x2: "+str(scramble_two_size)), fg_color = framecolour,
                        font = ctk.CTkFont(family = "Calibri", size=15))
            twosize.place(relx=0.14, rely=0.33, anchor=W)

            def twoslider_event(value):         #Function to change the scramble size
                global scramble_two_size
                scramble_two_size = settingsfile.iloc[1, 1] = int(value)                    #Changing the scramble sizes
                settingsfile.to_csv("Users_Settings.csv", index=False)
                twosize.configure(text = ("2x2: "+str(scramble_two_size)))                  #Updating the Label

            vartwo = IntVar()                                                               #Creating a variable for the slide
            vartwo.set(scramble_two_size)                                                   #Setting the slider to the current scramble size

            ctk.CTkSlider(settingschoosing_frame, command=twoslider_event, button_color = navcolour,
                          width=100, number_of_steps=8, variable = vartwo, from_=7, to=15,
                          progress_color = buttoncolour, button_hover_color = hovercolour
                        ).place(relx=0.5, rely=0.33, anchor=W)                              #Creating the slider for the 2x2 scramble size
            

            """4x4 Scramble Size"""

            foursize = ctk.CTkLabel(settingschoosing_frame, text_color=statstextcolour,     #Label for 4x4
                        text = ("4x4: "+str(scramble_four_size)), fg_color = framecolour,
                        font = ctk.CTkFont(family = "Calibri", size=15))
            foursize.place(relx=0.14, rely=0.4, anchor=W)

            def fourslider_event(value):        #Function to change the scramble size
                global scramble_four_size
                scramble_four_size = settingsfile.iloc[2, 1] = int(value)                   #Changing the scramble sizes
                settingsfile.to_csv("Users_Settings.csv", index=False)
                foursize.configure(text = ("4x4: "+str(scramble_four_size)))                #Updating the Label

            varfour = IntVar()                                                              #Creating a variable for the slide
            varfour.set(scramble_four_size)                                                 #Setting the slider to the current scramble size

            ctk.CTkSlider(settingschoosing_frame, command=fourslider_event, button_color = navcolour,
                           width=100, number_of_steps=20, variable = varfour, from_=35, to=55,
                          progress_color = buttoncolour, button_hover_color = hovercolour
                        ).place(relx=0.5, rely=0.4, anchor=W)                               #Creating the slider for the 4x4 scramble size
            

        """Function for changing the average sizes"""

        def AverageSizes():                     #Function for changing the Average sizes
            global avgentry1, avgentry2

            ttk.Separator(settingschoosing_frame, orient = 'horizontal', style='background.TSeparator'
                  ).place(relx=0.5, rely=0.48, anchor=CENTER, relwidth=0.81)                #Seperator

            ctk.CTkLabel(settingschoosing_frame, text = "Display Averages", fg_color = framecolour, text_color=statstextcolour,
                    font = ctk.CTkFont(family = "Calibri", size=15, weight="bold")).place(relx=0.12, rely=0.54, anchor=W)

            #Screating a switch for the user to toggle showing scramble or not
            def switch_event():                 #Function to change state of the average showing or not
                global display_avg
                display_avg = settingsfile.iloc[3, 1] = switch_var.get()
                settingsfile.to_csv("Users_Settings.csv", index=False)                      #Changing the file variables

            switch_var = ctk.StringVar(value=str(display_avg))                              #String variable for the switch

            ctk.CTkSwitch(settingschoosing_frame, text="", command=switch_event, switch_width=40, button_color = navcolour,
                          variable=switch_var, onvalue="True", offvalue="False", progress_color = backgroundcolour, 
                          button_hover_color=hovercolour).place(relx=0.9, rely=0.54, anchor=CENTER)


            """Average Button 1"""

            def click1(event):                  #When the user clicks the entry box    
                avgentry1.delete(0, 'end')                                                  #Delete the text in the entry
            
            def OnEntryClick1(event):           #Function for when the user clicks on the entry
                global avg1
                value = avgentry1.get().strip()                                             #Getting the entry value
                try: 
                    avg1 = settingsfile.iloc[4, 1] = int(value)                             #Changing the variables
                    settingsfile.to_csv("Users_Settings.csv", index=False)                  #Changing the file variables
                    validitylabel.configure(text = "")

                except: validitylabel.configure(text = "Please Input a Integer (Number) for the averages")
       
            #Label for the first average entry box
            ctk.CTkLabel(settingschoosing_frame, text = "First Average:", font = ctk.CTkFont(family = "Calibri", size=15),
                        fg_color = framecolour, text_color=statstextcolour).place(relx=0.14, rely=0.62, anchor=W)

            avgvar1 = StringVar()                                                           #Creating a string variable for the entry

            avgentry1 = ctk.CTkEntry(settingschoosing_frame, height= 25, border_color=entrycolour,
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), textvariable = avgvar1,
                            fg_color = framecolour, text_color=statstextcolour, justify="left",)
            
            avgentry1.place(relx=0.88, rely=0.62, relwidth = 0.25, anchor=E)                #Creating the first average entry
            avgentry1.insert(0, avg1)                                                       #Putting a placeholder for the entry
            avgentry1.bind("<KeyRelease>", OnEntryClick1)                                   #Make the entry check if a key has been pressed
            avgentry1.bind("<Button-1>", click1)                                            #Make the entry check if it has been clicked


            """Average Button 2"""

            def click2(event):                  #When the user clicks the entry box    
                avgentry2.delete(0, 'end')                                                  #Delete the text in the entry

            def OnEntryClick2(event):           #Function for when the user clicks on the entry
                global avg2
                value = avgentry2.get().strip()                                             #Getting the entry value
                try: 
                    avg2 = settingsfile.iloc[5, 1] = int(value)                             #Changing the variables
                    settingsfile.to_csv("Users_Settings.csv", index=False)                  #Changing the file variables
                    validitylabel.configure(text = "")

                except: validitylabel.configure(text = "Please Input a Integer (Number) for the averages")

            #Label for the second average entry box
            ctk.CTkLabel(settingschoosing_frame, text = "Second Average:", font = ctk.CTkFont(family = "Calibri", size=15),
                        fg_color = framecolour, text_color=statstextcolour).place(relx=0.14, rely=0.69, anchor=W)

            avgvar2 = StringVar()                                                           #Creating a string variable for the entry

            avgentry2 = ctk.CTkEntry(settingschoosing_frame, width = 60, height= 25, border_color=entrycolour,
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), textvariable = avgvar2,
                            fg_color = framecolour, text_color=statstextcolour, justify="left",)
            
            avgentry2.place(relx=0.88, rely=0.69, relwidth = 0.25, anchor=E)                #Creating the second average entry
            avgentry2.insert(0, avg2)                                                       #Putting a placeholder for the entry
            avgentry2.bind("<KeyRelease>", OnEntryClick2)                                   #Make the entry check if a key has been pressed
            avgentry2.bind("<Button-1>", click2)                                            #Make the entry check if it has been clicked


            """Functions"""

            def avgleave(event):                #When the user's curser leaves the combo box

                #If the entries are left empty, replace them with the current average
                if avgentry1.get().strip() == "": avgentry1.insert(0, avg1)
                if avgentry2.get().strip() == "": avgentry2.insert(0, avg2)

                try: int(avgentry1.get())                                        #Seeing if the inputed text is invalid
                except: 
                    avgentry1.delete(0, 'end')                                   #If it is then replace entry with the previous average
                    avgentry1.insert(0, avg1)

                try: int(avgentry2.get())                                        #Seeing if the inputed text is invalid
                except: 
                    avgentry2.delete(0, 'end')                                   #If it is then replace entry with the previous average
                    avgentry2.insert(0, avg2)

                settingschoosing_frame.focus()                                   #Focus on the settings frame

            settingschoosing_frame.bind("<Motion>", avgleave)                    #Make the settings frame detect if the user left a widget


        """Function for changing the keybinds"""

        def Keybinds():                         #Function for changing the keybinds
            global oldbinds

            oldbinds = [dnfbind, addbind, okbind, deletebind]                               #Saving the current keybinds

            ttk.Separator(settingschoosing_frame, orient = 'horizontal', style='background.TSeparator'
                  ).place(relx=0.5, rely=0.767, anchor=CENTER, relwidth=0.81)               #Seperator

            ctk.CTkLabel(settingschoosing_frame, text = "Keybinds", fg_color = framecolour, text_color=statstextcolour,
                    font = ctk.CTkFont(family = "Calibri", size=12, weight="bold")).place(relx=0.5, rely=0.765, anchor=CENTER)


            """DNF Keybind"""

            def click1(event):                  #When the user clicks the entry box    
                dnfbindentry.configure(state = "normal")                                    #Enable the entry again
                dnfbindentry.delete(0, 'end')                                               #Delete the text in the entry
            
            def OnEntryClick1(event):           #Funcion for when the user types in the entry
                #If the entry is more than one letter then disable the entry
                if len(dnfbindentry.get()) < 1: pass
                else: dnfbindentry.configure(state = "disabled")

            def OnEntryRelease1(event):         #Function for when the user releases thier key
                global dnfbind

                dnfbind = settingsfile.iloc[26, 1] = dnfbindentry.get()                     #Changing the varaibles
                settingsfile.to_csv("Users_Settings.csv", index=False)                      #Updating the settings

                validitytext()                                                              #Check Validity of the new keybind
       
            ctk.CTkLabel(settingschoosing_frame, text = "DNF:", font = ctk.CTkFont(family = "Calibri", size=13),
                        fg_color = framecolour, text_color=statstextcolour).place(relx=0.14, rely=0.84, anchor=W)

            dnfbindentry = ctk.CTkEntry(settingschoosing_frame, width = 40, border_color=entrycolour,
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), height= 20,
                            fg_color = framecolour, text_color=statstextcolour, justify="left")
                            
            dnfbindentry.place(relx=0.3, rely=0.84, anchor=W)                               #Creating the dnf entry
            dnfbindentry.insert(0, dnfbind)                                                 #Putting a placeholder for the entry
            dnfbindentry.bind("<KeyPress>", OnEntryClick1)                                  #Make the entry check if a key has been pressed
            dnfbindentry.bind("<KeyRelease>", OnEntryRelease1)                              #Make the entry check if a key has been released
            dnfbindentry.bind("<Button-1>", click1)                                         #Make the entry check if it has been clicked


            """+2 Keybind"""

            def click2(event):                  #When the user clicks the entry box    
                addbindentry.configure(state = "normal")                                    #Enable the entry again
                addbindentry.delete(0, 'end')                                               #Delete the text in the entry
            
            def OnEntryClick2(event):           #Funcion for when the user types in the entry
                #If the entry is more than one letter then disable the entry
                if len(addbindentry.get()) < 1: pass
                else: addbindentry.configure(state = "disabled")

            def OnEntryRelease2(event):         #Function for when the user releases thier key
                global addbind

                addbind = settingsfile.iloc[27, 1] = addbindentry.get()                     #Changing the varaibles
                settingsfile.to_csv("Users_Settings.csv", index=False)                      #Updating the settings

                validitytext()                                                              #Check Validity of the new keybind
       
            ctk.CTkLabel(settingschoosing_frame, text = "+2:", font = ctk.CTkFont(family = "Calibri", size=13),
                        fg_color = framecolour, text_color=statstextcolour).place(relx=0.56, rely=0.84, anchor=W)

            addbindentry = ctk.CTkEntry(settingschoosing_frame, width = 40, border_color=entrycolour,
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), height= 20,
                            fg_color = framecolour, text_color=statstextcolour, justify="left")
            
            addbindentry.place(relx=0.68, rely=0.84, anchor=W)                              #Creating the +2 entry
            addbindentry.insert(0, addbind)                                                 #Putting a placeholder for the entry
            addbindentry.bind("<KeyPress>", OnEntryClick2)                                  #Make the entry check if a key has been pressed
            addbindentry.bind("<KeyRelease>", OnEntryRelease2)                              #Make the entry check if a key has been released
            addbindentry.bind("<Button-1>", click2)                                         #Make the entry check if it has been clicked


            """delete Keybind"""

            def click3(event):                  #When the user clicks the entry box    
                deletebindentry.configure(state = "normal")                                 #Enable the entry again
                deletebindentry.delete(0, 'end')                                            #Delete the text in the entry
            
            def OnEntryClick3(event):           #Funcion for when the user types in the entry
                #If the entry is more than one letter then disable the entry
                if len(deletebindentry.get()) < 1: pass
                else: deletebindentry.configure(state = "disabled")

            def OnEntryRelease3(event):         #Function for when the user releases thier key
                global deletebind

                deletebind = settingsfile.iloc[28, 1] = deletebindentry.get()               #Changing the varaibles
                settingsfile.to_csv("Users_Settings.csv", index=False)                      #Updating the settings

                validitytext()                                                              #Check Validity of the new keybind
       
            ctk.CTkLabel(settingschoosing_frame, text = "delete:", font = ctk.CTkFont(family = "Calibri", size=11),
                        fg_color = framecolour, text_color=statstextcolour).place(relx=0.14, rely=0.91, anchor=W)

            deletebindentry = ctk.CTkEntry(settingschoosing_frame, width = 40, border_color=entrycolour,
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), height= 20,
                            fg_color = framecolour, text_color=statstextcolour, justify="left")
            
            deletebindentry.place(relx=0.3, rely=0.91, anchor=W)                            #Creating the delete entry
            deletebindentry.insert(0, deletebind)                                           #Putting a placeholder for the entry
            deletebindentry.bind("<KeyPress>", OnEntryClick3)                               #Make the entry check if a key has been pressed
            deletebindentry.bind("<KeyRelease>", OnEntryRelease3)                           #Make the entry check if a key has been released
            deletebindentry.bind("<Button-1>", click3)                                      #Make the entry check if it has been clicked


            """ok Keybind"""

            def click4(event):                  #When the user clicks the entry box    
                okbindentry.configure(state = "normal")                                     #Enable the entry again
                okbindentry.delete(0, 'end')                                                #Delete the text in the entry
            
            def OnEntryClick4(event):           #Funcion for when the user types in the entry
                #If the entry is more than one letter then disable the entry
                if len(okbindentry.get()) < 1: pass
                else: okbindentry.configure(state = "disabled")

            def OnEntryRelease4(event):         #Function for when the user releases thier key
                global okbind

                okbind = settingsfile.iloc[29, 1] = okbindentry.get()                       #Changing the varaibles
                settingsfile.to_csv("Users_Settings.csv", index=False)                      #Updating the settings

                validitytext()                                                              #Check Validity of the new keybind
       

            ctk.CTkLabel(settingschoosing_frame, text = "ok:", font = ctk.CTkFont(family = "Calibri", size=13),
                        fg_color = framecolour, text_color=statstextcolour).place(relx=0.56, rely=0.91, anchor=W)

            okbindentry = ctk.CTkEntry(settingschoosing_frame, width = 40, border_color=entrycolour,
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), height= 20,
                            fg_color = framecolour, text_color=statstextcolour, justify="left")
            
            okbindentry.place(relx=0.68, rely=0.91, anchor=W)                               #Creating the ok entry
            okbindentry.insert(0, okbind)                                                   #Putting a placeholder for the entry
            okbindentry.bind("<KeyPress>", OnEntryClick4)                                   #Make the entry check if a key has been pressed
            okbindentry.bind("<KeyRelease>", OnEntryRelease4)                               #Make the entry check if a key has been released
            okbindentry.bind("<Button-1>", click4)                                          #Make the entry check if it has been clicked


            """Functions"""

            def avgleave(event):                #When the user's curser leaves the combo box
                global oldbinds, dnfbind, addbind, okbind, deletebind                       #Global all the keybinds

                #If the entries are left empty when the user leaves it, replace it with the current keybind
                if dnfbindentry.get().strip() == "": dnfbindentry.insert(0, dnfbind)
                dnfbindentry.configure(state = "normal")
                if addbindentry.get().strip() == "": addbindentry.insert(0, addbind)
                addbindentry.configure(state = "normal")
                if deletebindentry.get().strip() == "": deletebindentry.insert(0, deletebind)
                deletebindentry.configure(state = "normal")
                if okbindentry.get().strip() == "": okbindentry.insert(0, okbind)
                okbindentry.configure(state = "normal")

                def validity():                 #Checking validity function
                    binds = [dnfbind, addbind, deletebind, okbind]                          #Getting all the current keybinds

                    dict = Counter(binds)                                                   #now convert list of keybinds into dictionary

                    duplicate = False                                                       #Setting if there is a duplicate word to false 

                    for key in binds:           #traverse list of words and check which first word has frequency > 1
                        if dict[key]>1: duplicate = True                                    #If there is a duplicate word then set it to true

                    if duplicate == True: return(True)                                      #Return True if there is a duplicate
                    else: return(False)                                                     #Return False if there is not a duplicate

                if validity() == True:          #If the input is not valid code

                    dnfbind = settingsfile.iloc[26, 1] = oldbinds[0]                        #Changing the keybinds back to the old keybinds
                    addbind = settingsfile.iloc[27, 1] = oldbinds[1]
                    okbind = settingsfile.iloc[29, 1] = oldbinds[2]
                    deletebind = settingsfile.iloc[28, 1] = oldbinds[3]

                    settingsfile.to_csv("Users_Settings.csv", index=False)

                    dnfbindentry.delete(0, 'end')                                           #Empytying the text in the entries
                    addbindentry.delete(0, 'end')
                    deletebindentry.delete(0, 'end')
                    okbindentry.delete(0, 'end')

                    dnfbindentry.insert(0, dnfbind)                                         #Adding the old keybinds as a placeholder
                    addbindentry.insert(0, addbind)
                    deletebindentry.insert(0, deletebind)
                    okbindentry.insert(0, okbind)

                else: oldbinds = [dnfbind, addbind, okbind, deletebind]                     #If it is valid then save current keybinds

                settingschoosing_frame.focus()                                              #Focus back on the settings frame

            settingschoosing_frame.bind("<Motion>", avgleave)                               #Detect if the user has left a widget

            def validitytext():                 #Function for the validity text
                binds = [dnfbind, addbind, deletebind, okbind]                              #Getting all the current keybinds

                dict = Counter(binds)                                                       #now convert list of keybinds into dictionary

                duplicate = False                                                           #Setting if there is a duplicate word to false 

                for key in binds:               #traverse list of words and check which first word has frequency > 1
                    if dict[key]>1: duplicate = True                                        #If there is a duplicate word then set it to true

                if duplicate == True: validitylabel.configure(text = "Please do not have repeat keybinds")
                else: validitylabel.configure(text = "")                                    #Notify the user if input is invalid

        AverageSizes()                          #Calling all the settings functions
        ScrambleSizes()
        Keybinds()

    settings()                                  #Calling the settings interface


    """Themes"""

    def theme():                                #Function for the themes interface

        #Variable names of the desired colours
        variables = ["BackgroundColour","InputColour", "ButtonColour","NavColour", "HoverColour", "EntryColour"]

        ctk.CTkLabel(themes_frame,  text="Themes", fg_color = framecolour, text_color=titletextcolour,
                     font = ctk.CTkFont(family = "Calibri", size=20, weight="bold")         #Creating the Label for the themes title
                    ).grid(row = 0, column = 0, columnspan = (len(variables)), pady = (25,10))

        file = pd.read_csv("Users_Themes.csv")                                              #Reading the themes file


        """Changing the themes"""

        def changetheme(index):                 #Function for actauly changing the themes

            global navcolour, statstextcolour, titletextcolour, buttontextcolour, radiocolour, entrycolour, radiohovercolour
            global buttoncolour, backgroundcolour, framecolour, inputcolour, textcolour, hovercolour, timestextcolour
            global graphlinecolour, sessiontextcolour, labelcolour, labeltextcolour, graphcolour, validitytext

            settingsfile = pd.read_csv("Users_Settings.csv")                                #Reading the settings csv file

            #Code for changing the themes varaibles and updating the csv settings file

            backgroundcolour = settingsfile.iloc[6, 1] = file.loc[index, "BackgroundColour"]
            navcolour = settingsfile.iloc[7, 1] = file.loc[index, "NavColour"]
            framecolour = settingsfile.iloc[8, 1] = file.loc[index, "FrameColour"]
            textcolour = settingsfile.iloc[9, 1] = file.loc[index, "TextColour"]
            statstextcolour = settingsfile.iloc[10, 1] = file.loc[index, "StatsTextColour"]
            titletextcolour = settingsfile.iloc[11, 1] = file.loc[index, "TitleTextColour"]
            sessiontextcolour = settingsfile.iloc[12, 1] = file.loc[index, "SessionTextColour"]
            buttoncolour = settingsfile.iloc[13, 1] = file.loc[index, "ButtonColour"]
            buttontextcolour = settingsfile.iloc[14, 1] = file.loc[index, "ButtonTextColour"]
            hovercolour = settingsfile.iloc[15, 1] = file.loc[index, "HoverColour"]
            radiocolour = settingsfile.iloc[16, 1] = file.loc[index, "RadioColour"]
            entrycolour = settingsfile.iloc[17, 1] = file.loc[index, "EntryColour"]
            inputcolour = settingsfile.iloc[18, 1] = file.loc[index, "InputColour"]
            graphlinecolour = settingsfile.iloc[19, 1] = file.loc[index, "GraphLineColour"]
            labelcolour = settingsfile.iloc[20, 1] = file.loc[index, "LabelColour"]
            labeltextcolour = settingsfile.iloc[21, 1] = file.loc[index, "LabelTextColour"]
            graphcolour = settingsfile.iloc[22, 1] = file.loc[index, "GraphColour"]
            validitytext = settingsfile.iloc[23, 1] = file.loc[index, "ValidityText"]
            radiohovercolour = settingsfile.iloc[24, 1] = file.loc[index, "RadioHover"]
            timestextcolour = settingsfile.iloc[25, 1] = file.loc[index, "TimesTextColour"]

            settingsfile.to_csv("Users_Settings.csv", index=False)

            main_window.configure(fg_color = backgroundcolour)                              #Changing the theme of the main frames
            nav_frame.configure(background = navcolour)
            timer_frame.configure(fg_color = backgroundcolour)
            stats_frame.configure(fg_color = backgroundcolour)
            times_frame.configure(fg_color = backgroundcolour)
            session_frame.configure(fg_color = backgroundcolour)
            settings_frame.configure(fg_color = backgroundcolour)

            navigation_GUI()                                                                #Updating the navigation bar
            SettingsGUI()                                                                   #Updating the settings interface


        """Printing out all the themes"""

        def themelayouts(index, num):           #Function for printing out all the themes
            for i in range(len(variables)):
                if i == 0:                                                                  #Alternate between printing theme and seperator
                    ctk.CTkButton(themes_frame, hover = False, height=45, border_spacing = 0, command = lambda s=num: changetheme(s),
                            fg_color = file.loc[index, variables[i]], text = file.loc[index, "Name"], corner_radius=5,
                            text_color = file.loc[index, "TextColour"], font = ctk.CTkFont(family = "Calibri", size=15, weight="bold")
                            ).grid(row = index+1, column = i, padx = (40,1))
                elif i == 5: 
                    ctk.CTkButton(themes_frame, hover = False, height=45, border_spacing = 0, command = lambda s=num: changetheme(s),
                            fg_color = file.loc[index, variables[i]], text = "", corner_radius=4
                            ).grid(row = index+1, column = i, pady = 17, padx = (1, 40))
                else:                                                                       #Printing the seperator
                    ctk.CTkButton(themes_frame, hover = False, height=45, border_spacing = 0, command = lambda s=num: changetheme(s),
                            fg_color = file.loc[index, variables[i]], text = "", corner_radius=4
                            ).grid(row = index+1, column = i, pady = 17, padx = 1)
                
        def TotalSolves():                      #Calculate the total solves in the session
            with open("Users_Themes.csv") as csvfile:                                       #Opening the csv file
                return(sum(1 for line in csvfile)-2)                                        #Adding up all the themes
        
        j = -1
        for i in range(TotalSolves()):          #Correctly gridding all the themes
            j += 1                                                                          #Changing the function
            themelayouts(i,j)                                                               #Printing all the themes by calling the function

    theme()                                     #Calling the themes in  terface
    
def EditsessionGUI():        #Funtion for the Edit Sessions interface                           (EDIT SESSIONS MINI-INTERFACE)
    global deletesessionbutton, editsessionbutton, chosensessiontype, confirmbutton, validitylabel

    """Creating the edit sessions mini-interface"""
    Stats_frame = ctk.CTkFrame(session_frame, fg_color = framecolour,  width = 180, height = 295)
    Stats_frame.place(relx=0.857, rely=0.393, relheight=0.67, relwidth=0.22, anchor=CENTER)

    ctk.CTkLabel(Stats_frame, text = "["+session+"]",                                               #Sessions type
                 font = ctk.CTkFont(family = "Calibri", size=12),
                fg_color = framecolour, text_color=titletextcolour
        ).place(relx=0.5, rely=0.14, anchor=CENTER)
    
    ctk.CTkLabel(Stats_frame, text = sessionname,                                                   #Session name (Title)
                font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                fg_color = framecolour, text_color=titletextcolour
        ).place(relx=0.5, rely=0.08, anchor=CENTER)
    
    validitylabel = ctk.CTkLabel(Stats_frame, text = "", height = 3,                                #Label to show if the input is valid
                        font = ctk.CTkFont(family = "Calibri", size=10, weight="bold"),
                        fg_color = framecolour, text_color=validitytext)  
    validitylabel.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    ttk.Separator(Stats_frame, orient = 'horizontal', style='background.TSeparator'                 #Seperator
                  ).place(relx=0.5, rely=0.24, anchor=CENTER, relwidth=0.81)


    """Function which edits the sessions (name and type)"""

    def Editsession():
        global session, sessionname, validitylabel                          #Global Variables

        """All the functions"""

        def findrow():                           #Funtion to find the row the selected session is in
            rowfind=0
            with open('Users_Sessions.csv', 'rt') as f:                     #Opening the users sessions file
                reader = csv.reader(f, delimiter=',')
                for row in reader:                                          #Checking every row
                    for field in row:                                       #Checking every item in that row (session name and session type)
                        rowfind += 1
                        if rowfind %2 == 0:                                 #Only check the session names column in the file and not the session type
                            if field == sessionname:                        #Seeing if the session names in that row matches the selected session name
                                return(int(rowfind/2)-2)                    #Return the row value the session name is in

        def error(word):                        #Function to inform the user that thier input is invalid
            validitylabel.configure(text = word)                            #Placing a text explaining the error

        def editsessionstype():                 #Function to finalise and change the session type
            global session

            file = pd.read_csv("Users_Sessions.csv")                        #Opening the users sessions csv
            file.loc[findrow(), "Session Type"] = chosensessiontype.get()   #Updating the sessions type accordingly
            file.to_csv("Users_Sessions.csv", index=False)

            settingsfile = pd.read_csv("Users_Settings.csv")                #Updating the current selected session
            session = settingsfile.iloc[31, 1] = chosensessiontype.get()

            settingsfile.to_csv("Users_Settings.csv", index=False)

            SessionsGUI()                                                   #Resetting the sessions interface


        """Updating the sessions and validity checker"""

        if (nameentry2.get()).strip() != "":    #Function to see if the entered session name is empty

            filename = "Solved Times/"+(nameentry2.get())+".csv"                        #Choosing the correct file name

            #Seeing if the file name already exists, if it does, show an error
            if(os.path.exists(filename) and os.path.isfile(filename)): error(nameentry2.get()+" already exists")

            else:
                os.rename("Solved Times/"+sessionname+".csv", filename)                 #If name doesnt exist, rename the file to the entered name
                
                file = pd.read_csv("Users_Sessions.csv")                                #Opening the users sessions csv
                file.loc[findrow(), "Session Name"] = nameentry2.get()                  #Updating the sessions name accordingly  
                file.to_csv("Users_Sessions.csv", index=False)

                settingsfile = pd.read_csv("Users_Settings.csv")                         #Reading the settings csv file
                sessionname = settingsfile.iloc[30, 1] = nameentry2.get()                #Updating the current selected session

                settingsfile.to_csv("Users_Settings.csv", index=False)

                if chosensessiontype.get() != "": editsessionstype()                    #Checking if any session type is selected
                else: SessionsGUI()                                                     #If not the reset the sessions interface

        else:
            if chosensessiontype.get() != "": editsessionstype()                        #Checking if any session type is selected
            else: error("Fill in atleast 1 entry")                                      #If not then show an error (need atleast one input)


    """Creating all the inputs which allows the user to edit the sessions"""

    """Entry Box"""
    ctk.CTkLabel(Stats_frame, text = "Change Session Name", 
                font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                fg_color = framecolour, text_color=statstextcolour       
        ).place(relx=0.5, rely=0.32, anchor=CENTER)                     #Change Session Name Label
    
    def click(event):                                                   #When the user clicks the entry box    
        nameentry2.delete(0, 'end')                                     #Reset the font back to normal

    def sessionleave(event):                                            #When the user's curser leaves the combo box
        Stats_frame.focus()                                             #Focus back on the window

    #Creating the entry box
    nameentry2 = ctk.CTkEntry(Stats_frame, width = 140, 
                            font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                            fg_color = framecolour, text_color=statstextcolour, justify="center",
                            border_color=entrycolour)
    nameentry2.place(relx=0.5, rely=0.42, relheight=0.09, relwidth=0.8, anchor=CENTER)                

    nameentry2.bind("<Button-1>", click)                                #Make the entry box detect in the user has clicked on it 
    Stats_frame.bind("<Motion>", sessionleave)

    ttk.Separator(Stats_frame, orient = 'horizontal', style='background.TSeparator'
                  ).place(relx=0.5, rely=0.52, anchor=CENTER, relwidth=0.81)          #Seperator


    """Combo Box"""
    ctk.CTkLabel(Stats_frame, text = "Change Session Type", 
                font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                fg_color = framecolour, text_color=statstextcolour
        ).place(relx=0.5, rely=0.6, anchor=CENTER)                      #Change Session Type Label

    SESSIONTYPES = ["3x3", "2x2", "4x4"]                                #Types of items in the combobox
    chosensessiontype = StringVar()                                     #Creating a StringVar for the ComboBox

    #Creating the ComboBox
    sessionentrychange = ctk.CTkComboBox(Stats_frame, variable = chosensessiontype,
                values = SESSIONTYPES, font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                fg_color = framecolour, text_color=statstextcolour, state = "readonly", justify="center", 
                border_color = entrycolour, button_color = entrycolour, dropdown_text_color = statstextcolour,
                dropdown_font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                dropdown_fg_color = framecolour, dropdown_hover_color = hovercolour)
                
    sessionentrychange.place(relx=0.5, rely=0.7, relheight=0.09, relwidth=0.8, anchor=CENTER)
    
    ttk.Separator(Stats_frame, orient = 'horizontal', style='background.TSeparator'
                  ).place(relx=0.5, rely=0.8, anchor=CENTER, relwidth=0.81)          #Seperator


    #Confirm Button
    confirmbutton = ctk.CTkButton(Stats_frame, text = "Confirm", command = Editsession,
                        font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                        fg_color = buttoncolour, hover_color=hovercolour, text_color=buttontextcolour)
    confirmbutton.place(relx=0.5, rely=0.9, relheight=0.1, relwidth=0.85, anchor=CENTER)

def SolveStats(sessiontype): #Funtion for the Solved Statistics interface                       (SOLVED STATS MINI-INTERFACE)
    global session, sessionname, deletesessionbutton, editsessionbutton                             #Globalling the Variables

    #Setting the new session variables (the user has selected a new session)
    settingsfile = pd.read_csv("Users_Settings.csv")                        #Reading the settings csv file
    
    sessionname = settingsfile.iloc[30, 1] = ses.get()                      #Updating the current selected session
    session = settingsfile.iloc[31, 1] = sessiontype

    settingsfile.to_csv("Users_Settings.csv", index=False)


    """Functions for calculating the selected sessions statistics"""

    def FastestSolve():          #Find the fastest solve in the session
        try: return(min((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist()))    #Getting the best solve
        except: return("N/A")    #If there is no solves in the session then print "N/A"
        
    def TotalSolves():           #Calculate the total solves in the session
        with open("Solved Times/"+sessionname+".csv") as csvfile:
            return(sum(1 for line in csvfile)-1)                            #Summing up all the solves in the selected session

    def MeanCALC():              #Calculate Mean of all Solves
        try:
            times = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())        #Getting all the times

            return(round((sum(times)/len(times)),2))       #Calculating the average
        except: return(0)                                  #If there is no solves in the session then return "0"
    

    """Creating the selected sessions mini-interface"""

    Stats_frame = ctk.CTkFrame(session_frame, fg_color = framecolour,  width = 180, height = 295)
    Stats_frame.place(relx=0.857, rely=0.39, relheight=0.67, relwidth=0.22, anchor=CENTER)

    def creatinglabels(text, fontweight, x, y):                                                     #Function for creating the stats labels
        ctk.CTkLabel(Stats_frame, text = text,font = ctk.CTkFont(family = "Calibri", size=15, weight=fontweight),
            fg_color = framecolour, text_color=statstextcolour).place(relx=x, rely=y, anchor=W)

    creatinglabels("Total Solves", "bold", 0.15, 0.1)                                               #Total Solves Label
    creatinglabels(TotalSolves(), "normal", 0.3, 0.17)                                              #Total Solves
    creatinglabels("Session Mean", "bold", 0.15, 0.3)                                               #Session Mean Label
    creatinglabels(MeanCALC(), "normal", 0.3, 0.37)                                                 #Session Mean

    ttk.Separator(Stats_frame, orient = 'horizontal', style='background.TSeparator'                 #Seperator
                  ).place(relx=0.5, rely=0.485, anchor=CENTER, relwidth=0.81)

    creatinglabels("Best Solve", "bold", 0.15, 0.6)                                                 #Best Solve Label
    creatinglabels(FastestSolve(), "normal", 0.3, 0.67)                                             #Best Solve
    creatinglabels("Current AO"+str(avg1), "bold", 0.15, 0.8)                                       #Current Average Label
    creatinglabels(AverageCALC(avg1), "normal", 0.3, 0.87)                                          #Current Average Mean


    """Function to delete the users selected session"""

    def Deletesession(sessionname2):                                                        #Function to delete the users selected session
        global sessionname, session                                                         #Global the variables

        def TotalSessions():           #Calculate the total solves in the session
            with open("Users_Sessions.csv") as csvfile:
                return(sum(1 for line in csvfile)-1)
        
        if int(TotalSessions()) < 2:
            messagebox.showinfo(title="Warning Message!", message = 'You cannot delete your session "'+sessionname2+'" because you only have 1 session remaining')

        else:
            #Ask the user if they are sure that they want to delete thier selected session
            status = messagebox.askyesno(title="Warning Message!", message = 'Are you sure you want to delete your session "'+sessionname2+'"?')
            
            if status == True:                                                              #Seeing if the user agrees to deleting thier selected session
                filename = "Solved Times/"+sessionname2+".csv"                              #Getting the file name

                os.remove(filename)                                                         #Deleting the file

                def findrow():          #Funtion to find the row the selected session is in
                    rowfind=0
                    
                    with open('Users_Sessions.csv', 'rt') as f:         #Opening the users sessions file
                        reader = csv.reader(f, delimiter=',')
                        for row in reader:                              #Checking every row
                            for field in row:                           #Checking every item in that row (session name and session type)
                                rowfind += 1
                                if rowfind %2 == 0:                     #Only check the session names column in the file and not the session type
                                    if field == sessionname2:           #Seeing if the session names in that row matches the selected session name
                                        return(int(rowfind/2)-2)        #Return the row value the session name is in

                file = pd.read_csv('Users_Sessions.csv')                #Opening the users sessions file
                file = file.drop(file.index[findrow()])                 #Deleting the selected session
                file.to_csv('Users_Sessions.csv', index=False)

                try:
                    settingsfile = pd.read_csv("Users_Settings.csv")    #Setting the users new selected session to the default

                    sessionname = settingsfile.iloc[30, 1] = file.loc[0, "Session Name"]
                    session = settingsfile.iloc[31, 1] = file.loc[0, "Session Type"]

                    settingsfile.to_csv("Users_Settings.csv", index=False)

                except:
                    settingsfile = pd.read_csv("Users_Settings.csv")    #Setting the users new selected session to the default

                    sessionname = settingsfile.iloc[30, 1] = file.loc[1, "Session Name"]
                    session = settingsfile.iloc[31, 1] = file.loc[1, "Session Type"]

                    settingsfile.to_csv("Users_Settings.csv", index=False)

                SessionsGUI()                                           #Resetting the sessions interface

            else: pass                                                  #Ignore if the user doesnt agree to deleting the session


    """Creating the edit selected session mini-interface"""

    Editsolve_frame = ctk.CTkFrame(session_frame, fg_color = framecolour,  width = 180, height = 85)            #Creating the frame
    Editsolve_frame.place(relx=0.857, rely=0.85, relheight=0.2, relwidth=0.22, anchor=CENTER)                                    

    editsessionbutton = ctk.CTkButton(Editsolve_frame, text_color = buttontextcolour,                           #Creating the "edit" button
                                      font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                                      fg_color = buttoncolour, hover_color=hovercolour,
                                      text = "Edit", command = lambda: EditsessionGUI())    
    editsessionbutton.place(relx=0.5, rely=0.3, relheight=0.3, relwidth=0.85, anchor=CENTER)

    deletesessionbutton = ctk.CTkButton(Editsolve_frame, text_color = buttontextcolour,                         #Creating the "Delete button
                                        font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                                        fg_color = buttoncolour, hover_color=hovercolour,
                                        text = "Delete", command = lambda: Deletesession(sessionname))
    deletesessionbutton.place(relx=0.5, rely=0.7, relheight=0.3, relwidth=0.85, anchor=CENTER)   

def SessionsGUI():           #Function for Sessions interface                                   (SESSIONS INTERFACE)
    global nameentry, chosensession, ses, styl                                      #Global the variables 

    reset()                                                                         #Removing the previous Frames

    session_frame.place(relx = 0.55, rely = 0.5, relheight=1, relwidth=0.9, anchor=CENTER)

    Sessionlist_frame = ctk.CTkScrollableFrame(session_frame, fg_color = framecolour, height=380, width=580,
                                               scrollbar_button_color = navcolour, scrollbar_button_hover_color = backgroundcolour)
    Sessionlist_frame.place(relx=0.39, rely=0.5, relheight=0.9, relwidth=0.69, anchor=CENTER)


    Sessionlist_frame.grid_columnconfigure(0, weight=1)
    Sessionlist_frame.grid_columnconfigure(1, weight=1)
    Sessionlist_frame.grid_columnconfigure(2, weight=1)

    def TotalSessions():           #Calculate the total solves in the session
        with open("Users_Sessions.csv") as csvfile:
            return(sum(1 for line in csvfile))


    """Printing the all the Sessions into the scrollable frame"""
    
    ses = tk.StringVar()                                                            #Creating a StringVar for the Radio Buttons
    ses.set(sessionname)                                                            #Setting the default selected Radio Button the already seslected session
    
    file = pd.read_csv("Users_Sessions.csv")                                        #Opening the file which contains all the users sessions

    ctk.CTkLabel(Sessionlist_frame,  text="Sessions",
                font = ctk.CTkFont(family = "Calibri", size=20, weight="bold"),
                fg_color = framecolour, text_color=titletextcolour
                ).grid(row = 0, column = 0, columnspan = 3, pady = (25,10))

    styl = ttk.Style()
    styl.configure('background.TSeparator', background=framecolour)

    for sessionnum in range((TotalSessions()-1)*2):                                 #Function which prints out all of the users sessions in a list

        if sessionnum %2 == 0:                  #This function makes the program print the sessions in a alternating pattern e.g; session, line, session, line
            #RadioButton for the Session name
            Radiobutton(Sessionlist_frame, variable = ses, indicator = 0, borderwidth=0, height=2, activebackground= framecolour,
                               bg = framecolour, foreground = statstextcolour, font = ctk.CTkFont(family = "Calibri", size=22, weight="bold"),
                        value = (file.loc[((sessionnum)/2), "Session Name"]), text = (file.loc[((sessionnum)/2), "Session Name"]), 
                        command = lambda s=(file.loc[((sessionnum)/2), "Session Type"]): SolveStats(s), selectcolor=framecolour
                        ).grid(column = 0, row = sessionnum+1, pady = 10)
            
            #RadioButton for the Session type
            Radiobutton(Sessionlist_frame, variable = sessionname, indicator = 0, borderwidth=0, height=2, activebackground= framecolour,
                               bg = framecolour, foreground = sessiontextcolour, font = ctk.CTkFont(family = "Calibri", size=22, weight="bold"),
                        value = (file.loc[((sessionnum)/2), "Session Name"]), text = ("["+file.loc[((sessionnum)/2), "Session Type"]+"]"), 
                        command = lambda s=(file.loc[((sessionnum)/2), "Session Type"]): SolveStats(s), selectcolor=framecolour
                        ).grid(column = 1, row = sessionnum+1, pady = 10)
            
            #RadioButton for the actual button itself
            ctk.CTkRadioButton(Sessionlist_frame, variable = ses, hover_color = radiohovercolour, border_color = radiocolour,
                        value = (file.loc[((sessionnum)/2), "Session Name"]), text = "", fg_color = radiocolour,
                        command = lambda s=(file.loc[((sessionnum)/2), "Session Type"]): SolveStats(s)
                        ).grid(column = 2, row = sessionnum+1, pady = 10)
            
        else:                    #Place a seperator (line) after every other session placed (more minimal look)
            ttk.Separator(Sessionlist_frame, orient = 'horizontal', style='background.TSeparator').grid(column = 0, row = sessionnum+1, sticky="ew", padx=50, columnspan = 3)


    """Creating a function which allows the user to add new sessions"""

    def Addsession():            #Function to add a new session

        newsessionname = nameentry.get()                                            #Getting the inputed session name

        def error(text):         #Function to show the user that the input is invalid
            nameentry.configure(text_color = validitytext)                          #Changing the font and colour of the entry text to red
            nameentry.delete(0, 'end')                                              #Delete the already existing text in the entry
            nameentry.insert(0, text)                                               #Display error message on entry box
            session_frame.focus()                                                   #Focus back on the main window

        #Cheking if the inputted session name is valid
        if newsessionname != "Enter New Session Name" and newsessionname != "Session Name Already Exists" and newsessionname != "Please fill in both inputs":
            if chosensession.get() != "":                                           #Cheking if the inputted session type (combobox) is blank

                filename = "Solved Times/"+newsessionname+".csv"

                #Checking if the file name already exists, if it already exists, display an error "Session Name Already Exists"
                if(os.path.exists(filename) and os.path.isfile(filename)): error("Session Name Already Exists")

                else:       #Otherwise Create a New session
                    with open(filename, 'w', newline='') as file:                           #Creating the new file
                        writer = csv.writer(file)
                        writer.writerow(['Solved Time','Scramble','Type'])                  #Update the columns in the new file

                    file = open("Users_Sessions.csv",'a+')                                   
                    file.writelines([chosensession.get(), ",",newsessionname, "\n"])        #Updating the users sessions file
                    file.close()
                    
                    SessionsGUI()                                                           #Resetting the Sessions Interface

            else: error("Please fill in both inputs")                                       #Displaying errors if conditions are not met
        else: error("Please fill in both inputs")


    """Creating all the inputs which allows the user to add new sessions"""
    
    """Entry Box"""
    def click(event):                   #When the user clicks the entry box   
        nameentry.configure(text_color = statstextcolour) 
        nameentry.delete(0, 'end')                                                          #Delete already existing text

    def entryleave(event):              #When the user's curser leaves the entry box
        if (nameentry.get()).strip() == "":                                                 #Check if the entry box was empty
            nameentry.delete(0, 'end')                                                      #if it is, delete all possible spaces
            nameentry.insert(0, 'Enter New Session Name')                                   #Input 'Enter New Session Name'
            session_frame.focus()                                                           #Focus back on the window
        else: session_frame.focus()                                                         #Else just focus back on the window

    #Creating the entry box
    nameentry = ctk.CTkEntry(Sessionlist_frame, width = 260, fg_color = framecolour, height = 30,
                             font = ctk.CTkFont(family = "Calibri", size=13, weight="bold"), placeholder_text = 'Enter New Session Name'
                             ,justify="center", border_color=entrycolour, text_color=statstextcolour, placeholder_text_color = statstextcolour)
    
    nameentry.grid(column = 0, row = sessionnum+2, pady = 20, padx = (40, 4))

    nameentry.bind("<Button-1>", click)                                                     #Make the entry box detect in the user has clicked on it 
    nameentry.bind("<Leave>", entryleave)                                                   #Make the entry box detect if the user has left it
    
    """Combo Box"""
    def sessionleave(event):                                                                #When the user's curser leaves the combo box
        session_frame.focus()                                                               #Focus back on the window

    SESSIONTYPES = ["3x3", "2x2", "4x4"]                                                    #Types of items in the combobox
    chosensession = ctk.StringVar()                                                         #Creating a StringVar for the ComboBox

    #Creating the ComboBox
    sessionentry = ctk.CTkComboBox(Sessionlist_frame, variable = chosensession, width = 150, height = 30,
                values = SESSIONTYPES, font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                fg_color = framecolour, text_color=statstextcolour, state = "readonly", justify="center",
                border_color = entrycolour,  button_color = entrycolour, dropdown_text_color = statstextcolour,
                dropdown_font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"),
                dropdown_fg_color = framecolour, dropdown_hover_color = hovercolour)

    sessionentry.grid(column = 1, row = sessionnum+2, pady = 20, padx = 4)

    Sessionlist_frame.bind("<Motion>", sessionleave)                    #Make the combo box detect in the user has left it 
    sessionentry.bind('<<ComboboxSelected>>', sessionleave)             #Make the combo box detect in the user selected something

    """Add Sessions Button"""
    ses2 = tk.StringVar()
    ses2.set("placeholder")

    ctk.CTkRadioButton(Sessionlist_frame, variable = ses2, hover_color = radiohovercolour, 
                        border_color = radiocolour, fg_color = radiocolour,text = "", 
                        command = Addsession, corner_radius = 10, value = "placeholder"
                        ).grid(column = 2, row = sessionnum+2, pady = 10)

    SolveStats(session)                                                 #Calling the solved statistics mini-interface

def EditSolve(solveid):      #Editing the solves interface                                      (EDITING SOLVES MINI-INTERFACE)
    global timelabel, scramblelabel, SolvedStats_frame, addbutton, dnfbutton                #Global Variables


    """Creating all the Labels and buttons for the mini-interface"""
    
    #Creating the Solve States Frame
    SolvedStats_frame = ctk.CTkFrame(times_frame, fg_color = framecolour,  width = 400, height = 100)
    SolvedStats_frame.place(relx=0.47, rely=0.81, relheight=0.21, relwidth=0.95, anchor=CENTER)

    #Placing the filler Labels (the solved time and the scramble of that solve)
    timelabel = ctk.CTkLabel(SolvedStats_frame, text = "", fg_color = framecolour, text_color=statstextcolour,
                             font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"))
    timelabel.place(relx=0.18, rely=0.3, anchor=CENTER)

    validitylabel = ctk.CTkLabel(SolvedStats_frame, text = "Please select a solve first", height = 3,
                        font = ctk.CTkFont(family = "Calibri", size=12, weight="bold"),
                        fg_color = framecolour, text_color=validitytext)  
    validitylabel.place(relx=0.5, rely=0.3, anchor=CENTER)


    #Creating the buttons (+2, dnf, and delete solve)
    addbutton = ctk.CTkButton(SolvedStats_frame, width = 100, text_color = buttontextcolour, 
                                 font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                                 fg_color = buttoncolour, text = "+2", hover_color=hovercolour)
    addbutton.place(relx=0.2, rely=0.68, relheight=0.3, relwidth=0.25, anchor=CENTER)

    dnfbutton = ctk.CTkButton(SolvedStats_frame, width = 100, text_color = buttontextcolour, 
                                font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                                fg_color = buttoncolour, text = "DNF", hover_color=hovercolour)
    dnfbutton.place(relx=0.5, rely=0.68, relheight=0.3, relwidth=0.25, anchor=CENTER)

    deletebutton = ctk.CTkButton(SolvedStats_frame, width = 100, text_color = buttontextcolour, 
                                font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                                fg_color = buttoncolour, text = "Delete", hover_color=hovercolour)
    deletebutton.place(relx=0.8, rely=0.68, relheight=0.3, relwidth=0.25, anchor=CENTER)


    """All the Command Functions for the buttons"""

    def DNF(solveid):               #Editing the solves (DNF)

        def TotalSolves():          #Calculate the total solves in the session
            with open("Solved Times/"+sessionname+".csv") as csvfile:
                return(sum(1 for line in csvfile)-1)                                    #Counting every solve in the file
        
        file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Reading the csv file
        
        index = ((TotalSolves())-(solveid+1))                                           #Getting the row the time is in

        if file.loc[index, 'Type'] != "DNF":                                            #Cheking if the time is already a DNF
            if file.loc[index, 'Type'] == "+2":
                solvetime = file.iloc[-(solveid+1), 0]

                file.loc[index, 'Solved Time'] = str(round(float(solvetime - 2), 2))    #If not then adding 2s to the time
                file.loc[index, 'Type'] = "DNF"
                file.to_csv("Solved Times/"+sessionname+".csv", index=False)

                StatsGUI()

            else:
                file.loc[index, 'Type'] = "DNF"                                         #If not then make the time a DNF
                file.to_csv("Solved Times/"+sessionname+".csv", index=False)

                StatsGUI()                                                              #Resetting the Interface
        
        #If time is already a DNF then notify the user
        else: 
            scramblelabel.configure(text_color = validitytext, text = "                     This solve is already DNF",
                                      font = ctk.CTkFont(family = "Calibri", size=12, weight="bold")) 
            scrambleframe.configure(scrollbar_button_color = framecolour, scrollbar_button_hover_color = framecolour)  

    def edit(solveid):               #Editing the solves (+2)

        def TotalSolves():           #Calculate the total solves in the session
            with open("Solved Times/"+sessionname+".csv") as csvfile:
                return(sum(1 for line in csvfile)-1)                                    #Counting every solve in the file
        
        file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Reading the csv file
        
        solvetime = file.iloc[-(solveid+1), 0]                                          #Getting the selected time
        index = ((TotalSolves())-(solveid+1))                                           #Getting the row the time is in

        if file.loc[index, 'Type'] != "+2":                                             #Cheking if the time already has had a +2
            file.loc[index, 'Solved Time'] = str(round(float(solvetime + 2), 2))        #If not then adding 2s to the time
            file.loc[index, 'Type'] = "+2"

            file.to_csv("Solved Times/"+sessionname+".csv", index=False)

            StatsGUI()                                                                  #Resetting the Interface

        #If there is already a +2 then notify the user
        else: 
            scramblelabel.configure(text_color = validitytext, text = "                     This solve is already +2",
                                      font = ctk.CTkFont(family = "Calibri", size=12, weight="bold"))
            scrambleframe.configure(scrollbar_button_color = framecolour, scrollbar_button_hover_color = framecolour)

    def delete(solveid):            #Deleting the solves
        file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Opening the correct file
        file = file.drop(file.index[-(solveid+1)])                                      #Deleting the chosen time
        file.to_csv("Solved Times/"+sessionname+".csv", index=False)

        StatsGUI()                                                                      #Resetting the Interface


    """Seeing if a button has been selected (if so, config the button commands and labels accordingly"""

    try:
        file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Finding the correct time and scramble
        solvetime = file.iloc[-(solveid+1), 0]
        solvescramble = file.iloc[-(solveid+1), 1]

        timelabel.configure(text = solvetime)                                           #Changing the two labels
        validitylabel.configure(text = "")

        scrambleframe = ctk.CTkScrollableFrame(SolvedStats_frame, fg_color = framecolour, 
                                            orientation = "horizontal", width = 240, height= 20,
                                            scrollbar_button_hover_color = backgroundcolour,
                                            scrollbar_button_color = navcolour)
        scrambleframe.place(relx=0.6, rely=0.3, anchor=CENTER)

        scramblelabel = ctk.CTkLabel(scrambleframe, text = "", 
                                    font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"), 
                                    fg_color = framecolour, text_color=statstextcolour)
        scramblelabel.grid(column = 0, row = 0)
        scramblelabel.configure(text = solvescramble, font = ("Comfortaa", 10))

        addbutton.configure(command = lambda s=solveid: edit(s))                        #Changing all the button commands
        dnfbutton.configure(command = lambda s=solveid: DNF(s))
        deletebutton.configure(command = lambda s=solveid: delete(s))

    except:pass                                                                         #Ignore if there is an error (no button selected)

def SolvedTimes():           #Function for Solved Times interface                               (SOLVED TIMES INTERFACE)

    times_frame.place(relx = 0.775, rely = 0.5, relheight=1, relwidth=0.45, anchor=CENTER)      #Creating/Resetting the Frames

    SolvedTimes_frame = ctk.CTkScrollableFrame(times_frame, fg_color = framecolour, 
                                               scrollbar_button_color = navcolour, scrollbar_button_hover_color = backgroundcolour)
    
    SolvedTimes_frame.place(relx=0.47, rely=0.36, relheight=0.6, relwidth=0.95, anchor=CENTER)  #Creating a SolvedTimes frame

    SolvedTimes_frame.grid_columnconfigure(0, weight=1)                                         #Making the gridding adjust to frame size
    SolvedTimes_frame.grid_columnconfigure(1, weight=1)
    SolvedTimes_frame.grid_columnconfigure(2, weight=1)
    SolvedTimes_frame.grid_columnconfigure(3, weight=1)
            
    alltimes = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())         #Listing all the solved times in the session
    alltimes.reverse()                          #Reversing the list order so that the lastest solved times will appear first


    """Important Functions"""

    def label(text, col):                       #Function for the "+2", "dnf" labels

        def labelcreate(text, col, pad):        #Functions for creating the Label
            frame = ctk.CTkFrame(SolvedTimes_frame, width = 20, height= 20, fg_color=labelcolour, bg_color=buttoncolour)
            frame.grid(row = rownum+1, column = col, sticky = NE, pady=10, padx = pad)

            ctk.CTkLabel(frame, text = text, fg_color=labelcolour, text_color = labeltextcolour,
                        width=15, height=15, font = ctk.CTkFont(family = "Calibri", size=9, weight="bold")
                            ).place(relx=0.5, rely=0.5, anchor=CENTER)

        if col == 3: labelcreate(text, col, (10,32))
        else: labelcreate(text, col, 10)

                
    file = pd.read_csv("Solved Times/"+sessionname+".csv")                                      #Reading the chosen session fil

    def TotalSolves():                          #Calculate the total solves in the session
            with open("Solved Times/"+sessionname+".csv") as csvfile:
                return(sum(1 for line in csvfile)-1)


    """Printing the all the Solved Times into the scrollable frame"""

    global rownum
    rownum = 0
    
    ctk.CTkLabel(SolvedTimes_frame,  text="Times", font = ctk.CTkFont(family = "Calibri", size=20, weight="bold"),
                fg_color = framecolour, text_color=titletextcolour).grid(row = 0, column = 0, columnspan=4, pady = 10)
    
    def creatingbuttons(col, padleft, padright):
        global rownum

        ctk.CTkButton(SolvedTimes_frame,  text=alltimes[solve], command = lambda s=solve: EditSolve(s), 
                        height= 75, hover_color = hovercolour, fg_color=buttoncolour, text_color = timestextcolour,
                        font = ctk.CTkFont(family = "Calibri", size=15, weight="bold")
            ) .grid(row = rownum+1, column = col, padx = (padleft, padright), pady = 4)         #Creating the Buttons

        if file.loc[index, 'Type'] == "DNF": label("DNF", col)                                  #Checking the type of solve
        elif file.loc[index, 'Type'] == "+2": label("+2", col)
        if col == 3: rownum += 1                                                                #Gridding the next Solves Times buttons in the next row down

    for solve in range(len(alltimes)):                                      #Making a loop that loops for the number of total solves
        index = ((TotalSolves())-(solve+1))

        if (solve-0)%4 == 0: creatingbuttons(0, 25, 4)
        if (solve-1)%4 == 0: creatingbuttons(1, 4, 4)
        if (solve-2)%4 == 0: creatingbuttons(2, 4, 4)
        if (solve-3)%4 == 0: creatingbuttons(3, 4, 25)

def Graph():                 #Draw the Line Graph of all the times

    alltimes = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())         #Getting all the times
    timesnumber = list(range(len(alltimes)))                                                    #Getting the total number of solves

    graph_dictionary = {"Time": alltimes,                                                       #Turning the lists above into a dictionary
                        "Solve Number": timesnumber}
    
    dataframe = pd.DataFrame(graph_dictionary)                              #Create a "table" of the dictionary

    figure = plt.figure(figsize = (4.6, 2.1), dpi = 120)                    #Setting the size, resolution of the graph
    figure.set_facecolor(framecolour)                                       #Setting the Background Colour of the graph

    figure_plot = figure.add_subplot(1, 1, 1)                               #Setting the spacing of the plots [rows, columns, index position]
    figure_plot.patch.set_facecolor(graphcolour)

    line_graph = FigureCanvasTkAgg(figure, master = graph_frame)                                #Creating the Graph
    line_graph.get_tk_widget().place(relx=0.5, rely=0.57, relheight=0.8, relwidth=1, anchor=CENTER)

    dataframe = dataframe[["Time", "Solve Number"]].groupby("Solve Number").sum()               #Telling the graph how to graph the plots
    dataframe.plot(kind = 'line', legend = True, ax = figure_plot,                              #Making it into a Line Graph
                   color = graphlinecolour, fontsize = (6))

    figure_plot.set_title("")                                                                   #Making the graph "blank"
    figure_plot.set_xlabel(' ')
    figure_plot.set_ylabel(' ')
    plt.xticks([])

    #plt.axis("off")                                                                            #This was to only show the line

def StatsGUI():              #Function for statistics interface                                 (STATISTICS INTERFACE)
    global sta1_frame, sta2_frame, graph_frame

    """Functions to calculate the all the statistics"""
    def FastestSolve():          #Find the fastest solve in the session
        try: return(min((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist()))     #Getting the best solve
        except: return("N/A")                                                                        #If there is no solves, return "N/A"

    def TotalSolves():           #Calculate the total solves in the session
        with open("Solved Times/"+sessionname+".csv") as csvfile:                                    #Opening the csv file
            return(sum(1 for line in csvfile)-1)                                                     #Sum all the rows

    def MeanCALC():              #Calculate Mean of all Solves
        try:
            times = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())         #Getting all the times
            return(round((sum(times)/len(times)),2))                                                 #Calculating the average
        except: return(0)                                                                            #If there is no solves, return "0"

    reset()                      #Removing the previous Frame

    """Creating the statistics and solved times interface"""
    stats_frame.place(relx = 0.325, rely = 0.5, relheight=1, relwidth=0.45, anchor=CENTER)           #Creating/Resetting the Frames

    #Creating the new subframes
    sta1_frame = ctk.CTkFrame(stats_frame, fg_color = framecolour)
    sta2_frame = ctk.CTkFrame(stats_frame, fg_color = framecolour)

    graph_frame = ctk.CTkFrame(stats_frame, fg_color = framecolour)
    graph_frame.place(relx=0.5, rely=0.69, relheight=0.45, relwidth=0.86, anchor=CENTER)

    #Title of the session statistics label
    ctk.CTkLabel(stats_frame, text = sessionname+" Statistics", fg_color = backgroundcolour, text_color=textcolour,
            font = ctk.CTkFont(family = "Calibri", size=22, weight="bold")).place(relx=0.5, rely=0.09, anchor=CENTER)
    
    sta1_frame.place(relx=0.28, rely=0.3, relheight=0.28, relwidth=0.42, anchor=CENTER)              #Placing the subframes
    sta2_frame.place(relx=0.72, rely=0.3, relheight=0.28, relwidth=0.42, anchor=CENTER)

    def creatinglabels(frametype, text, fontweight, x, y):                                           #Function for creating the stats labels
        
        ctk.CTkLabel(frametype, text = text,font = ctk.CTkFont(family = "Calibri", size=15, weight=fontweight),
            fg_color = framecolour, text_color=statstextcolour).place(relx=x, rely=y, anchor=W)

    """Labels for subframe 1"""

    creatinglabels(sta1_frame, "Total Solves", "bold", 0.15, 0.2)                                    #Total Solves Label
    creatinglabels(sta1_frame, TotalSolves(), "normal", 0.3, 0.38)                                   #Total Solves
    creatinglabels(sta1_frame, "Session Mean", "bold", 0.15, 0.6)                                    #Session Mean Label
    creatinglabels(sta1_frame, MeanCALC(), "normal", 0.3, 0.78)                                      #Session Mean

    """Labels for subframe 2"""

    creatinglabels(sta2_frame, "Best Solve", "bold", 0.15, 0.2)                                      #Best Solve Label
    creatinglabels(sta2_frame, FastestSolve(), "normal", 0.3, 0.38)                                  #Best Solve
    creatinglabels(sta2_frame, "Current AO"+str(avg1), "bold", 0.15, 0.6)                            #Current Average Label
    creatinglabels(sta2_frame, AverageCALC(avg1), "normal", 0.3, 0.78)                               #Current Average Mean
    
    
    Graph()                 #Displaying the graph

    ctk.CTkLabel(graph_frame, text = "Time Trend", 
            font = ctk.CTkFont(family = "Calibri", size=19, weight="bold"),
            fg_color = framecolour, text_color=titletextcolour                          #Graph Label
            ).place(relx=0.5, rely=0.14, anchor=CENTER)

    SolvedTimes()           #Display all the Solved Times
    EditSolve('')           #Displaying Edit Solve Panel

def GenerateScramble():      #Function to generate a random Cube Scramble

    #Move types
    dir = ["", "'", "2"]            #Move Permutations

    if session == '3x3':    moves = ["U", "D", "F", "B", "R", "L"]                                      #Scrambles for a 3x3
    if session == '4x4':    moves = ["U", "D", "F", "B", "R", "L", "Uw", "Fw", "Rw", "Lw"]              #Scrambles for a 4x4
    if session == '2x2':    moves = ["U", "F", "R"]                                                     #Scrambles for a 2x2

    def valid(ar):                  #Checking if the next move is a valid move
        #Check if Move behind or 2 behind is the same as the random move
        #this gets rid of 'R R2' or 'R L R2' or similar for all moves
        for x in range(1, len(ar)):
            while ar[x][0] == ar[x-1][0]:
                ar[x][0] = random.choice(moves)
        for x in range(2, len(ar)):
            while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
                ar[x][0] = random.choice(moves)
        return ar
    
    def generate(scramble):
        #Make array of arrays that represent moves ex. U' = ['U', "'"]
        s = valid([[random.choice(moves), random.choice(dir)] for x in range(scramble)])

        #Format scramble to a string with movecount
        return (''.join(str(s[x][0]) + str(s[x][1]) + ' ' for x in range(len(s))))

    if session == '3x3': return(generate(scramble_three_size))              #Scramble generator for 3x3 sessions
    if session == '2x2': return(generate(scramble_two_size))                #Scramble generator for 2x2 sessions
    if session == '4x4': return(generate(scramble_four_size))               #Scramble generator for 4x4 sessions
    
class StopWatch(Frame):      #Timing Class that controls the stopwatch
    global Timer
                                                             
    def __init__(self, parent=None, **kw):          #Implementing a stop watch frame widget  
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()               
        self.makeWidgets()      

    def makeWidgets(self):                          #Making the time label
        global timeText                   
        timeText = ctk.CTkLabel(timer_frame, textvariable=self.timestr, 
                         font = ctk.CTkFont(family = "Calibri", size=100, weight="bold"),
                         fg_color = backgroundcolour, text_color=textcolour)
        self._setTime(self._elapsedtime)
        timeText.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    def _update(self):                              #Update the label with elapsed time
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):                       #Set the time string to Minutes:Seconds:Hundreths
        global minutes, seconds, hseconds
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100) 
        if minutes > 0:                             #When there is minutes
            self.timestr.set('%0d:%02d.%02d' % (minutes, seconds, hseconds))
        else:                                       #When there is no minutes
            self.timestr.set('%0d.%02d' % (seconds, hseconds))
        
    def Start(self):                                #Start the stopwatch, ignore if running
        global Timer        
        #Change Timer back to black when spacebar released                                            
        timeText.configure(text_color = textcolour, font = ctk.CTkFont(family = "Calibri", size=100, weight="bold", overstrike=0))

        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1    
    
    def Stop(self):                                 #Stop the stopwatch, ignore if stopped
        global Timer                               
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
            return self._elapsedtime
    
    def Reset(self):                                 #Reset the stopwatch
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
    
    def editedtime(self, text):                      #Updating the Labels for editing the times
        self.timestr.set(text)                       #Updating the label

        try:                                         #Updating the compare time labels
            lasttime = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())
            difference = lasttime[-1]-lasttime[-2]
            if lasttime[-1] > lasttime[-2]: comparetimelabel.configure(text = "(+"+str(round(difference, 2))+")")
            if lasttime[-1] <= lasttime[-2]: comparetimelabel.configure(text = "("+str(round(difference, 2))+")")
        except: pass

        #Updating the Average Labels
        Avg1Label.configure(text = ("AO"+str(avg1)+": "+ str(AverageCALC(avg1))))
        Avg2Label.configure(text = ("AO"+str(avg2)+": "+ str(AverageCALC(avg2))))

    """Future Improvement"""
    """def addedtime(self):
        if minutes > 0:                             #When there is minutes
            self.timestr.set('%0d:%02d.%02d' % (minutes, seconds+2, hseconds))
        else:                                       #When there is no minutes
            self.timestr.set('%0d.%02d' % (seconds+2, hseconds))"""

    def deletedtime(self):                           #Updating the Timer interface when the user deletes a solve
        lasttime = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())
        self.timestr.set(lasttime[-1])               #Setting the time to the previous solve time

        try:
            difference = lasttime[-1]-lasttime[-2]   #Updating the compare time labels
            if lasttime[-1] > lasttime[-2]: comparetimelabel.configure(text = "(+"+str(round(difference, 2))+")")
            if lasttime[-1] <= lasttime[-2]: comparetimelabel.configure(text = "("+str(round(difference, 2))+")")
        except: pass

        #Updating the Average Labels
        Avg1Label.configure(text = ("AO"+str(avg1)+": "+ str(AverageCALC(avg1))))
        Avg2Label.configure(text = ("AO"+str(avg2)+": "+ str(AverageCALC(avg2))))

def AverageCALC(num):        #Function for calculating averages
    global times
    
    try:         #Try function to see if there will be an error / see if there is enough recorded times
        times = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())[-num:]     #Getting all the times according to the average

        if len(times) >= num:                             #Checking to see if there is enough recorded times
            return(round((sum(times)/len(times)),2))      #Calculating the average
        else: return("N/A")                                 #If there is not enough recorded times, return "N/A"
    except: return("N/A")                                 #If there is an error, return "N/A"

def TimerGUI():              #Function for timer interface                                      (TIMER INTERFACE)
    global Timer, Scramble, Time, main_window, stopwatch_frame, Avg1Label, Avg2Label, comparetimelabel

    reset()         #Removing the previous Frame

    #Creating the timer interface
    timer_frame.place(relx = 0.55, rely = 0.5, relheight=1, relwidth=0.9, anchor=CENTER)
    stopwatch_frame = StopWatch(timer_frame)                    #Creating the timer frame

    timeText.place(relx=0.5, rely=0.45, anchor=CENTER)          #Placing the timer

    Scramble = GenerateScramble()                               #Generate a random scramble


    """Placing all the Lables"""

    SessionLabel = ctk.CTkLabel(timer_frame, text = sessionname, fg_color = backgroundcolour,                   #Session name
                    text_color=navcolour, font = ctk.CTkFont(family = "Calibri", size=15, weight="bold"))
    SessionLabel.place(relx=0.05, rely=0.07, anchor=W)

    if session == '4x4':                                                                                        #If session type is a 4x4
        Scramblesplit = Scramble.split(" ")                                                                     #Spliting the times in half
        part1 = " ".join(Scramblesplit[:math.ceil(scramble_four_size/2)+1])
        part2 = " ".join(Scramblesplit[-(math.floor(scramble_four_size/2)):-1])

        ScrambleLabel = ctk.CTkLabel(timer_frame, text = part1 + "\n" + part2, fg_color = backgroundcolour,     #Scramble Label for 4x4
                        text_color=textcolour, font = ctk.CTkFont(family = "Calibri", size=20, weight="bold"))
    else:
        ScrambleLabel = ctk.CTkLabel(timer_frame, text = Scramble, fg_color = backgroundcolour,                 #Scramble Label for 3x3
                        text_color=textcolour, font = ctk.CTkFont(family = "Calibri", size=25, weight="bold"))
        
    ScrambleLabel.place(relx=0.5, rely=0.15, anchor=CENTER)                                                     #Placing the Scramble Label

    comparetimelabel = ctk.CTkLabel(timer_frame, text = (""), height = 3, fg_color = backgroundcolour,          #Creating the Compare Label
                    text_color=titletextcolour, font = ctk.CTkFont(family = "Calibri", size=14, weight="bold"))
        
    comparetimelabel.place(relx=0.61, rely=0.56, anchor=W)                                                      #Placing the Compare Label

    if display_avg == "True":                                   #Placing the two average Labels If user selected it
        Avg1Label = ctk.CTkLabel(timer_frame, text = ("AO"+str(avg1)+": "+ str(AverageCALC(avg1))), text_color=textcolour,
                        fg_color = backgroundcolour, font = ctk.CTkFont(family = "Calibri", size=20, weight="bold"))
        Avg1Label.place(relx=0.5, rely=0.63, anchor=CENTER)

        Avg2Label = ctk.CTkLabel(timer_frame, text = ("AO"+str(avg2)+": "+ str(AverageCALC(avg2))),  text_color=textcolour,
                        fg_color = backgroundcolour, font = ctk.CTkFont(family = "Calibri", size=20, weight="bold"))
        Avg2Label.place(relx=0.5, rely=0.70, anchor=CENTER)


    """Starting the timer function"""

    Timer = False
    def key_pressed(event):
        global Timer, main_window

        def key_Released(event2):                   #Start the timer when spacebar is released
            global Timer
            stopwatch_frame.Start()
            ScrambleLabel.configure(text = "")      #Hiding the labels for a more clean aestetic
            if display_avg == "True":
                Avg1Label.configure(text = "")
                Avg2Label.configure(text = "")
            SessionLabel.configure(text = "")
            comparetimelabel.configure(text = "")

            main_window.unbind(dnfbind)                 #Unbinding all the keybinds
            main_window.unbind(addbind)
            main_window.unbind(deletebind)
            main_window.unbind(okbind)
            Timer = True      

        if event.char == " " and Timer == False:                                            #When spacebar is pressed, and not timing
            stopwatch_frame.Reset()                                                         #Resseting the timer when spacebar pressed
            timeText.configure(text_color = inputcolour)                                    #make timer green, indicates ready for timing
            main_window.bind("<KeyRelease-space>", key_Released)     

        if Timer == True:                                                                   #When timer is running and spacebar pressed
            global Time, Scramble, avg1, avg2, session, sessionname
            Time = stopwatch_frame.Stop()                                                   #Stopping the time
            Split_Time = (str(Time).split(".")[0])+"."+(str(Time).split(".")[1])[:2]        #Recording the time
            
            if float(Split_Time) > 0.4 and float(Split_Time) < 900:                         #Adding boundries to the time
                file = open("Solved Times/"+sessionname+".csv",'a+')                        #Uploading the time and scrable onto a csv file
                file.writelines([Split_Time, ",", Scramble, ",ok", "\n"])
                file.close()
            else:                                                                           #If the time does not sit between the boundry, dont record it
                file = pd.read_csv("Solved Times/"+sessionname+".csv")
                stopwatch_frame.editedtime(file.iloc[-1, 0])

            Scramble = GenerateScramble()                                                   #Generate a new scramble
            Timer = False
            if session == '4x4':                                                            #If the session is 4x4, then split the time label
                Scramblesplit = Scramble.split(" ")
                part1 = " ".join(Scramblesplit[:math.ceil(scramble_four_size/2)+1])
                part2 = " ".join(Scramblesplit[-(math.floor(scramble_four_size/2)):-1])

                ScrambleLabel.configure(text = part1 + "\n" + part2)
                
            else: ScrambleLabel.configure(text = Scramble)                                  #Otherwise just leave the label

            try:                                                                            #Try Calculating the difference of the two times
                lasttime = ((read_csv("Solved Times/"+sessionname+".csv"))['Solved Time'].tolist())
                difference = lasttime[-1]-lasttime[-2]                                      #Calculating the difference of the two times
                if lasttime[-1] > lasttime[-2]: comparetimelabel.configure(text = "(+"+str(round(difference, 2))+")")
                if lasttime[-1] <= lasttime[-2]: comparetimelabel.configure(text = "("+str(round(difference, 2))+")")
            except: pass                                                                    #If there is an error then pass

            if display_avg == "True":                                                       #Placing the two average Labels If user selected it
                Avg1Label.configure(text = ("AO"+str(avg1)+": "+ str(AverageCALC(avg1))))   #Updating the Averages
                Avg2Label.configure(text = ("AO"+str(avg2)+": "+ str(AverageCALC(avg2))))

            SessionLabel.configure(text = sessionname)                                      #Show the session name again

            main_window.unbind("<KeyRelease-space>")                                        #Make the code not check if spacebar is pressed

            main_window.bind(dnfbind, dnf)
            main_window.bind(addbind, edit)
            main_window.bind(deletebind, delete)
            main_window.bind(okbind, ok)

    main_window.bind("<KeyPress>", key_pressed)                                             #Make the code check if spacebar is pressed

    
    """Editing the solves functions"""

    def TotalSolves():                      #Calculate the total solves in the session
            with open("Solved Times/"+sessionname+".csv") as csvfile:
                return(sum(1 for line in csvfile)-2)                                        #Counting every solve in the file
            

    def dnf(event):                         #Function to make a solve dnf
        try:
            file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Reading the csv file
            solvetime = file.iloc[TotalSolves(), 0]                                         #Getting the selected time

            #Ask if the user is sure they want to dnf their time
            status = messagebox.askyesno(title="Warning Message!", message = 'Are you sure you want to DNF your time of '+str(solvetime)+'s?')

            def dnftime():                  #Function to actauly dnf the solve
                file.loc[TotalSolves(), 'Type'] = "DNF"                                     #Change the solve into a dnf
                file.to_csv("Solved Times/"+sessionname+".csv", index=False)
                    
                stopwatch_frame.editedtime("DNF")                                           #Update the Timer Label

            if status == True:                                                              #If they want to, then dnf thier solve
                if file.loc[TotalSolves(), 'Type'] == "+2":                                 #Making sure the solve isnt a +2 first

                    #If the solve is a +2, then minus 2 and then dnf the solve
                    file.loc[TotalSolves(), 'Solved Time'] = str(round(float(solvetime - 2), 2))
                    dnftime()                                                               #Make the solve a dnf

                else: dnftime()                                                             #Make the solve a dnf
        except: messagebox.showinfo(title="Warning Message!", message = 'You have no solves in your session to dnf')


    def edit(event):                        #Funtion to make a solve a +2
        print(TotalSolves())
        try:
            file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Reading the csv file
            solvetime = file.iloc[TotalSolves(), 0]                                         #Getting the selected time

            #Ask if the user is sure they want to +2 to their time
            status = messagebox.askyesno(title="Warning Message!", message = 'Are you sure you want to +2 to your time of '+str(solvetime)+'s?')

            if status == True:                                                              #If they want to, then +2 to thier solve
                if file.loc[TotalSolves(), 'Type'] != "+2":                                 #Cheking if the time already has had a +2

                    #If the solve isnt alreadt a +2, then +2 the solve
                    file.loc[TotalSolves(), 'Solved Time'] = str(round(float(solvetime + 2), 2))
                    file.loc[TotalSolves(), 'Type'] = "+2"                                  #Change the solve into a +2
                    file.to_csv("Solved Times/"+sessionname+".csv", index=False)

                    stopwatch_frame.editedtime(str(round(float(solvetime + 2), 2)))         #Update the Timer Label

        except: messagebox.showinfo(title="Warning Message!", message = 'You have no solves in your session to +2')


    def delete(event):                      #Deleting the solves
        try:
            file = pd.read_csv("Solved Times/"+sessionname+".csv")                          #Reading the csv file
            solvetime = file.iloc[TotalSolves(), 0]                                         #Getting the selected time

            #Ask if the user is sure they want to delete thier solve
            status = messagebox.askyesno(title="Warning Message!", message = 'Are you sure you want to delete your time of '+str(solvetime)+'s?')

            if status == True:                                                              #If they want to, then delete thier solve  
                file = file.drop(file.index[-1])                                            #Deleting the chosen time
                file.to_csv("Solved Times/"+sessionname+".csv", index=False)

                stopwatch_frame.deletedtime()                                      #Update the Timer Label

        except: messagebox.showinfo(title="Warning Message!", message = 'You have no solves in your session to delete')


    def ok(event):                          #Reseting thier time
        try:
            file = pd.read_csv("Solved Times/"+sessionname+".csv")                           #Reading the csv file
            solvetime = file.iloc[TotalSolves(), 0]                                          #Getting the selected time

            #Ask if the user is sure they want to reset thier time
            status = messagebox.askyesno(title="Warning Message!", message = 'Are you sure you want change your time of '+str(solvetime)+'s back to default?')

            if status == True:                                                               #If they want to, then reset thier time
                if file.loc[TotalSolves(), 'Type'] == "+2":

                    #If the solve is already a +2 then minus 2 and make it "ok"
                    file.loc[TotalSolves(), 'Solved Time'] = str(round(float(solvetime - 2), 2))
                    file.loc[TotalSolves(), 'Type'] = "ok"                                   #Change the solve into a "ok"
                    file.to_csv("Solved Times/"+sessionname+".csv", index=False)

                    stopwatch_frame.editedtime(str(round(float(solvetime - 2), 2)))          #Update the Timer Label

                else:
                    file.loc[TotalSolves(), 'Type'] = "ok"                                   #If solve is not a +2 then just make it "ok"
                    file.to_csv("Solved Times/"+sessionname+".csv", index=False)
                    
                    stopwatch_frame.editedtime(file.iloc[-1, 0])                             #Update the Timer Label

        except: messagebox.showinfo(title="Warning Message!", message = 'You have no solves in your session')


    #Keybinds of the editing solves
    main_window.bind(dnfbind, dnf)
    main_window.bind(addbind, edit)
    main_window.bind(deletebind, delete)
    main_window.bind(okbind, ok)

def navigation_GUI():        #Function for side navigation interface                            (NAVIGATION INTERFACE)
    global timer_img, stats_img, sessions_img, settings_img, tab                #Icons

    #Creating the side navigation interface
    nav_frame.place(relx = 0.05, rely = 0.5, relheight=1, relwidth=0.1, anchor=CENTER)
    nav_frame.grid_propagate(0)                                                 #Making it so that the frame size doesnt change with gridding

    #Creating the Images/Icons
    timer_img = ctk.CTkImage(Image.open('icons/timer.png'), size=(30, 30))
    stats_img = ctk.CTkImage(Image.open('icons/statistics.png'), size=(30, 30))
    sessions_img = ctk.CTkImage(Image.open('icons/sessions.png'), size=(30, 30))
    settings_img = ctk.CTkImage(Image.open('icons/setting.png'), size=(30, 30))
    
    #Creating the RadioButtons (Tabs)
    tab = StringVar()
    tab.set("Timer")

    ctk.CTkButton(nav_frame,command = TimerGUI, image = timer_img, fg_color = navcolour, 
                  hover_color=backgroundcolour, text="", width = 40).place(relx=0.5, rely=0.15, anchor=CENTER)
    
    ctk.CTkButton(nav_frame, command = StatsGUI, image = stats_img, fg_color = navcolour, 
                  hover_color=backgroundcolour, text="", width = 40).place(relx=0.5, rely=0.30, anchor=CENTER)
    
    ctk.CTkButton(nav_frame, command = SessionsGUI, image = sessions_img, fg_color = navcolour, 
                  hover_color=backgroundcolour, text="", width = 40).place(relx=0.5, rely=0.45, anchor=CENTER)
    
    ctk.CTkButton(nav_frame, command = SettingsGUI, image = settings_img, fg_color = navcolour, 
                  hover_color=backgroundcolour, text="", width = 40).place(relx=0.5, rely=0.9, anchor=CENTER)

def main():                  #Main function for all variables
    global nav_frame, main_window, timer_frame, stats_frame, times_frame, session_frame, settings_frame                 #Interfaces

    global scramble_three_size, scramble_two_size, scramble_four_size, display_avg                                      #Settings variables
    global avg1, avg2, session, sessionname, deletebind, addbind, okbind, dnfbind 
    
    global navcolour, statstextcolour, titletextcolour, buttontextcolour, radiocolour, entrycolour, radiohovercolour    #Themes 
    global buttoncolour, backgroundcolour, framecolour, inputcolour, textcolour, hovercolour, timestextcolour
    global graphlinecolour, sessiontextcolour, labelcolour, labeltextcolour, graphcolour, validitytext


    """Settings lists and variables"""
    file = pd.read_csv("Users_Settings.csv")                    #Users Settings
    scramble_three_size = int(file.iloc[0, 1])
    scramble_two_size = int(file.iloc[1, 1])
    scramble_four_size = int(file.iloc[2, 1])
    display_avg = (file.iloc[3, 1])
    avg1 = int(file.iloc[4, 1])
    avg2 = int(file.iloc[5, 1])

    dnfbind = file.iloc[26, 1]                                  #Users Settings
    addbind = file.iloc[27, 1]
    deletebind = file.iloc[28, 1]
    okbind = file.iloc[29, 1]
    
    backgroundcolour = file.iloc[6, 1]                          #Users Theme
    navcolour = file.iloc[7, 1]
    framecolour = file.iloc[8, 1]
    textcolour = file.iloc[9, 1]
    statstextcolour = file.iloc[10, 1]
    titletextcolour = file.iloc[11, 1]
    sessiontextcolour = file.iloc[12, 1]
    buttoncolour = file.iloc[13, 1]
    buttontextcolour = file.iloc[14, 1]
    hovercolour = file.iloc[15, 1]
    radiocolour = file.iloc[16, 1]
    entrycolour = file.iloc[17, 1]
    inputcolour = file.iloc[18, 1]
    graphlinecolour = file.iloc[19, 1]
    labelcolour = file.iloc[20, 1]
    labeltextcolour = file.iloc[21, 1]
    graphcolour = file.iloc[22, 1]
    validitytext = file.iloc[23, 1]
    radiohovercolour = file.iloc[24, 1]
    timestextcolour = file.iloc[25, 1]

    sessionname = file.iloc[30, 1]
    session = file.iloc[31, 1]

    """Tkinter Window and Frames"""
    main_window = ctk.CTk(fg_color = backgroundcolour)

    width = 940                                         # Width 
    height = 450                                        # Height

    screen_width = main_window.winfo_screenwidth()      # Width of the screen
    screen_height = main_window.winfo_screenheight()    # Height of the screen

    x = (screen_width/2) - (width/2)                    # Calculate Starting X and Y coordinates for Window
    y = (screen_height/2) - (height/2)

    main_window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    main_window.minsize(740, 380)
    main_window.maxsize(1100, 600)
    #main_window.resizable(False, False)

    main_window.title("Cube Timer Assessment - Leo Cao")
    
    #Creating all the interface frames
    nav_frame = Frame(main_window, background = navcolour)
    timer_frame = ctk.CTkFrame(main_window, fg_color = backgroundcolour)
    stats_frame = ctk.CTkFrame(main_window, fg_color = backgroundcolour)
    times_frame = ctk.CTkFrame(main_window, fg_color = backgroundcolour)
    session_frame = ctk.CTkFrame(main_window, fg_color = backgroundcolour)
    settings_frame = ctk.CTkFrame(main_window, fg_color = backgroundcolour)

    #Calling the Interfaces
    navigation_GUI()
    TimerGUI()

    main_window.mainloop()

main()

