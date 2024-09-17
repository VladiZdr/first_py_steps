from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QGridLayout, QHBoxLayout, QPushButton, QVBoxLayout

#---------------------------------------------------
#elemnts for calculator

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My calc")
main_window.resize(300, 300)

expression_text = QLineEdit()
calc_b = QGridLayout()
clear_buttons = QHBoxLayout()

clear_expr_b = QPushButton("Clear")
delete_last_input_b = QPushButton("<")

clear_buttons.addWidget(clear_expr_b)
clear_buttons.addWidget(delete_last_input_b)

#---------------------------------------------------
#All the functionality behind buttons

def button_clicked():
    expression = expression_text.text()
    pressed_b = app.sender()
    last_input = pressed_b.text()

    if last_input == "=":
        try:
            res = eval(expression)
            expression_text.setText(str(res))
        except Exception as er:
            print("error: ", er)
    elif last_input == "Clear":
        expression_text.clear()
    elif last_input == "<":
        expression_text.setText(expression[:-1])
    else:
        expression_text.setText(expression+last_input)

#---------------------------------------------------
#give the functionality to the buttons

clear_expr_b.clicked.connect(button_clicked)
delete_last_input_b.clicked.connect(button_clicked)

buttons = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "0", ".", "=", "+", ]
row = 0
col = 0

for button_text in buttons:
    button = QPushButton(button_text)
    button.clicked.connect(button_clicked)
    calc_b.addWidget(button, row, col)
    col += 1
    if col > 3:
        col = 0
        row += 1

#---------------------------------------------------
#create GUI and run

def run_calc():

    layout = QVBoxLayout()
    layout.addWidget(expression_text)
    layout.addLayout(calc_b)
    layout.addLayout(clear_buttons)

    main_window.setLayout(layout)
    main_window.show()
    app.exec_()