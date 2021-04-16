import PySimpleGUI as sg

sg.theme('green')  # please make your windows colorful
sg.SystemTray.notify('Welcome to Intra-University Messenger', 'Connecting to server...')
layout = [[sg.Image(r'/home/maroon/Desktop/messenger/Images/header1.png')],
		  #[sg.Text('This is my pink color'),sg.Text(size=(12,1),colors=('pink','blue'))],
		  [sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()