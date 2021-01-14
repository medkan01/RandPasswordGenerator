import PySimpleGUI as sg

BG = "#161b22"

def createWindow():
    """
        Create a default window.

    Returns:
    
        - Window: Default window.
    """
    layout = [
        [sg.Text("Size", background_color=BG), sg.Spin([i for i in range(1,20)], initial_value=8, size=(3,10))],
        
        [sg.HSeparator()],
        
        [sg.Text("Select the character's type you want", background_color=BG)],
        [sg.CBox("Lowercase", background_color=BG, default=True, disabled=True)],
        [sg.CBox("Uppercase", background_color=BG)],
        [sg.CBox("Number", background_color=BG)],
        [sg.CBox("Symbol", background_color=BG)],
        
        [sg.HSeparator()],
        
        [sg.Text("Password", background_color=BG), sg.InputText(size=(20,10))],
        
        [sg.HSeparator()],
        
        [sg.Button("Generate"), sg.Button("Close")]
    ]

    window = sg.Window("Password creator", layout, background_color="#161b22")
    return window