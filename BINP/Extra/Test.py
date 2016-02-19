import tkinter

__author__ = 'Owain'


class MineSweeper(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.labelVariable = tkinter.StringVar()

        self.radio_var = tkinter.StringVar()

        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        label = tkinter.Label(self, text="Kies een moeilijkheidsgraad", compound="center")
        label.grid(column=0, row=0, columnspan=2, sticky='EW')

        button = tkinter.Button(self, text=u"Makkelijk!",
                                command=self.on_button_click(0))
        button.grid(column=0, row=1)

        button = tkinter.Button(self, text=u"Normaal",
                                command=self.on_button_click(1))
        button.grid(column=1, row=1)

        button = tkinter.Button(self, text=u"Moeilijk!",
                                command=self.on_button_click(2))
        button.grid(column=2, row=1)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(False, False)

        self.update()
        self.geometry(self.geometry())

    def on_button_click(self, val):
        print("Click jeej, {}".format(val))

    def on_press_enter(self, event):
        print("Enter jeej")

if __name__ == "__main__":
    app = MineSweeper(None)
    app.title("Test")
    app.mainloop()
