# Program name: ggproperty_tax_GUI.py
# Author: Giovanna Gorski
# Date last updated: 7/17/2017
# Purpose: Property tax and Assessment value program with GUI.

import tkinter

class Property:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the frames.
        self.test1_frame = tkinter.Frame(self.main_window)
        self.assess_frame = tkinter.Frame(self.main_window)
        self.tax_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for input property value.
        self.test1_label = tkinter.Label(self.test1_frame, \
                        text='Enter the property value:$ ')
        self.test1_entry = tkinter.Entry(self.test1_frame, \
                                         width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create and pack the widgets for the assessment.
        self.result_label = tkinter.Label(self.assess_frame, \
                        text='Assessment Value: $')
        self.assess = tkinter.StringVar() # To update avg_label
        self.assess_label = tkinter.Label(self.assess_frame, \
                                    textvariable=self.assess)
        self.result_label.pack(side='left')
        self.assess_label.pack(side='left')

        # Create and pack the widgets for the tax.
        self.result2_label = tkinter.Label(self.tax_frame, \
                        text='Tax Value: $')
        self.tax = tkinter.StringVar() # To update assess_label
        self.tax_label = tkinter.Label(self.tax_frame, \
                                    textvariable=self.tax)
        self.result2_label.pack(side='left')
        self.tax_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame, \
                                     text='Calculate', \
                                     command=self.calc_property)
        self.quit_button = tkinter.Button(self.button_frame, \
                                text='Quit', \
                                command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.test1_frame.pack()
        self.assess_frame.pack()
        self.tax_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The calc_avg method is the callback function for
    # the calc_button widget.

    def calc_property(self):
        # Get the three test scores and store them
        # in variables.
        self.test1 = float(self.test1_entry.get())

        # Calculate the assessment value of the property.
        self.assessmnt = self.test1*0.60

        # Update the labels widget by storing
        # the value of self.assess and self.tax in the StringVar
        # object referenced by tax and assess.
        self.taxes = ((self.assessmnt//100)*0.75)
        self.assess.set(self.assessmnt)
        self.tax.set(self.taxes)

# Create an instance of the TestAvg class.
test_property = Property()



        
