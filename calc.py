import tkinter as tk
from PIL import Image, ImageTk

class FancyCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Fancy Calculator")
        self.master.configure(bg='#2E2E2E')

        # Entry widget for display
        self.result_var = tk.StringVar()
        entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 18), bd=10, insertwidth=4, width=14, justify='right', bg='#4D4D4D', fg='white')
        entry.grid(row=0, column=0, columnspan=4)

        # Load animated calculator GIF
        calculator_image = Image.open('animated_calculator.gif')  # Replace 'animated_calculator.gif' with the path to your animated GIF
        calculator_image.thumbnail((100, 100))  # Adjust the size if needed
        calculator_image = ImageTk.PhotoImage(calculator_image)

        calculator_label = tk.Label(self.master, image=calculator_image, bg='#2E2E2E')
        calculator_label.grid(row=0, column=4, rowspan=5, sticky='nsew')

        # Button styles
        button_style = {'padx': 20, 'pady': 20, 'font': ('Arial', 14), 'bg': '#666666', 'fg': 'white', 'activebackground': '#999999', 'activeforeground': 'white'}

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val, col_val = 1, 0

        for button_text in buttons:
            tk.Button(self.master, text=button_text, command=lambda text=button_text: self.on_button_click(text), **button_style).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            new_text = current_text + button_text
            self.result_var.set(new_text)

def main():
    root = tk.Tk()
    app = FancyCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
