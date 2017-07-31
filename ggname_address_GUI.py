# Program name: ggname_address_GUI.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: Print out your name, address at the window


import tkinter

class NameGui:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for the information.

        self.info = tkinter.StringVar() # To update info_label
        self.info_label = tkinter.Label(self.info_frame, \
                                    textvariable=self.info)
        self.info_label.pack(side='left')

        # Create and pack the button widgets.
        self.show_button = tkinter.Button(self.button_frame, \
                                     text='Show Info', \
                                     command=self.showInfo)
        self.quit_button = tkinter.Button(self.button_frame, \
                                text='Quit', \
                                command=self.main_window.destroy)
        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')


        self.info_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The showInfo method is the callback function for
    # the show_button widget.

    def showInfo(self):
        self.show = 'Giovanna Gorski\n56904 Sundown Rd\nSouth Bend, IN, 46619'
        self.info.set(self.show)

# Create an instance of the NameGui class.
test_avg = NameGui()



        
