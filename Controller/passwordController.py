from View.passwordView import *
from Model.passwordModel import *

window = createWindow()

while True:
    event, values = window.read()
    if event == "Close" or event == sg.WINDOW_CLOSED:
        break
    if event == "Generate":
        passwordSize = window.Element("-passwordSize-").Get()
        lowercase = window.Element("-lowercase-").get()
        uppercase = window.Element("-uppercase-").get()
        number = window.Element("-number-").get()
        symbol = window.Element("-symbol-").get()
        window.Element("-password-").update(generator(passwordSize, lowercase, uppercase, number, symbol))

window.close()