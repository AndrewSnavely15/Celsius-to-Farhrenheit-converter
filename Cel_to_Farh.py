import tkinter

class temperature:
    def __init__(self):
        # Creates main window
        self.main_window = tkinter.Tk()
        self.temp_frame = tkinter.Frame(self.main_window)
        self.calculate_frame = tkinter.Frame(self.main_window)
        self.solution_frame = tkinter.Frame(self.main_window)
        
        self.temp_label = tkinter.Label(self.temp_frame, \
                                        text = "Enter a temperature in Celsius: ")
        self.temp_entry = tkinter.Entry(self.temp_frame, width = 5)
        self.temp_label.pack(side = "left")
        self.temp_entry.pack(side = "left")
        
        # Creates a button to calulate the temperature
        self.calculate_button = tkinter.Button(self.calculate_frame, \
                                               text = 'Calculate', command = self.Cel_to_Farh)
        self.calculate_button.pack(side = "left")
        
        self.sol_label = tkinter.Label(self.solution_frame, \
                                       text = "The temperature in Farhrenheit is: ")
        # Creates an empty string and assigns the output for Farhrenheit
        self.set_Farh = tkinter.StringVar()
        self.solution_label = tkinter.Label(self.solution_frame, \
                                            textvariable = self.set_Farh)
        self.sol_label.pack(side = 'left')
        self.solution_label.pack(side = 'left')
        
        self.temp_frame.pack()
        self.calculate_frame.pack()
        self.solution_frame.pack()
        tkinter.mainloop()
        
    def Cel_to_Farh(self):
         self.celsius = float(self.temp_entry.get())
         # formula to convert from C to F
         self.Farh = float(self.celsius * float(9/5)) + 32
         self.set_Farh.set(self.Farh)
# Creates instance
temp = temperature()
        