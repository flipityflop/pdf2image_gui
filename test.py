import PySimpleGUI as sg

def a_callback_function():
    print(f'In callback function')

layout = [ [sg.Output(s=(60,10))],
           [sg.Button('Button 1'), sg.Button('Button2', key=a_callback_function), sg.Button('Exit')]  ]

window = sg.Window('Function as Key', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if callable(event):
        event()

window.close()