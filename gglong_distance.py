# Program name: long_distance.py
# Author: Giovanna Gorski
# Date last updated: 7/18/2017
# Purpose: Calculate the cost of long distances call. Program for final exam SDEV 220


import tkinter
import tkinter.messagebox

class LongDistance:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create two frames. One for the Radiobuttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.test1_frame = tkinter.Frame(self.main_window)
        
        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = tkinter.IntVar()
        
        # Set the intVar object to 1.
        self.radio_var.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame, \
                    text='Daytime (6:00 am - 5:59 pm), $0.07/minute', variable=self.radio_var, \
                    value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, \
                    text='Evening (6:00 pm - 11:59 pm),$0.12/minute', variable=self.radio_var, \
                    value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, \
                    text='Off-Peak (midnight - 5:59 am), $0.05/minute', variable=self.radio_var, \
                    value=3)

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        #create the frame for test1
        #the frame will be used by the user to input the call in minutes
        self.test1_label = tkinter.Label(self.test1_frame, \
                                         text='Enter the length of the call (in minutes):')
        self.test1_entry = tkinter.Entry(self.test1_frame, \
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')
        

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame, \
                      text='Calculate cost', command=self.calc_Cost)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                      text='Quit', command=self.main_window.destroy)

        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.test1_frame.pack()
        self.bottom_frame.pack()
        
        
        # Start the mainloop.
        tkinter.mainloop()

    # The show_choice method is the callback function for the
    # OK button.
    
    def calc_Cost(self):
        #Self.cal get the minutes inputed by the user and convert it to a float
        self.calc=float(self.test1_entry.get())
        #Self op get the radio option chose and convert it to a int
        self.op=int(self.radio_var.get())
        #The validations below will calculate the cost by the option of the user
        if self.op==1:
            self.result=round(0.07*self.calc,2)
        elif self.op==2:
            self.result=round(0.12*self.calc,2)
        elif self.op==3:
            self.result=round(0.05*self.calc,2)
        #The round method was called because I found that some of the numbers
        #was going to display extremely big numbers
        #Display the calculation
        tkinter.messagebox.showinfo('Call cost', 'The cost of the call is: $' +\
                              str(self.result))

# Create an instance of the MyGUI class.
my_gui = LongDistance()
