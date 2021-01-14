import PySimpleGUI as sg

bg = "#161b22"

layout = [
    [sg.Text("Size", background_color=bg), sg.Spin([i for i in range(1,20)], initial_value=8, size=(3,10))],
    
    [sg.HSeparator()],
    
    [sg.Text("Select the character's type you want", background_color=bg)],
    [sg.CBox("Lowercase", background_color=bg, default=True, disabled=True)],
    [sg.CBox("Uppercase", background_color=bg)],
    [sg.CBox("Number", background_color=bg)],
    [sg.CBox("Symbol", background_color=bg)],
    
    [sg.HSeparator()],
    
    [sg.Text("Password", background_color=bg), sg.InputText(size=(20,10))],
    
    [sg.HSeparator()],
    
    [sg.Button("Generate"), sg.Button("Close")]
]

windows = sg.Window("Password creator", layout, background_color="#161b22")

while True:
    event, values = windows.read()
    if event == "Close" or event == sg.WINDOW_CLOSED:
        break

windows.close()