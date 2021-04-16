# Testing async window, see if can have a slider
# that adjusts the size of text displayed
'''
import PySimpleGUI as sg


fontSize = 12
chats= open('/home/maroon/Desktop/messenger/chats/inbox.txt','r').readlines()


row1=[sg.Image(r'/home/maroon/Desktop/messenger/Images/header1.png')]



lef_col = [[sg.Text("Inbox", font="Helvetica "  + str(50), key='text')]
          [sg.Listbox(values=chats, size=(43, 3), key='-LIST-', enable_events=True)],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit',button_color=('white', 'red'))]]

rig_col = [[sg.Text("Computer Center", font="Helvetica "  + str(50), key='text')],
          [sg.Listbox(values=chats, size=(43, 3), key='-LIST-', enable_events=True)]
          [sg.Input(key='-IN-'),
          [sg.Button('Send')]]

layout=[row1,
       [sg.Column()]]

sz = fontSize
window = sg.Window("Font size selector", layout, grab_anywhere=False)
# Event Loop
while True:
    event, values= window.read()
    if event == sg.WIN_CLOSED:
        break
    sz_spin = int(values['spin'])
    sz_slider = int(values['slider'])
    sz = sz_spin if sz_spin != fontSize else sz_slider
    if sz != fontSize:
        fontSize = sz
        font = "Helvetica "  + str(fontSize)
        window['text'].update(font=font)
        window['slider'].update(sz)
        window['spin'].update(sz)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

print("Done.")
window.close()


'''
import PySimpleGUI as sg

#sg.theme('black')  # please make your windows colorful
#sg.SystemTray.notify('Welcome to Intra-University Messenger', 'Connecting to server...')

chats= open('/home/maroon/Desktop/messenger/chats/inbox.txt','r').readlines()
fontSize = 12
cs= open('/home/maroon/Desktop/messenger/Inbox.txt','r').readlines()

lef_col = [
		      #[sg.Text('This is my pink color'),sg.Text(size=(12,1),colors=('pink','blue'))],

		      #sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),
           #sg.Slider(range=(6,172), orientation='h', size=(10,20),
           #change_submits=True, key='slider', font=('Helvetica 20')),
          [sg.Text("Inbox", font="Helvetica "  + str(50), key='text')],
          [sg.Input("Search: ",key='-IN-')],
          [sg.Listbox(values=chats, size=(44, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Show'), sg.Button('Exit',button_color=('white', 'red'))]]

rig_col=[[sg.Text("Computer Center DTU", font="Helvetica "  + str(25), key='text')],
        [sg.Listbox(values=cs, size=(84, 12), key='-LIST-', enable_events=True)],
        [sg.Input(key='-IN-'),sg.Button('Send')]]


t1 = [[sg.Image(r'/home/maroon/Desktop/messenger/Images/header1.png')],
    
    [   sg.Column(lef_col),
        sg.VSeperator(),
        sg.Column(rig_col),
    ]
]
t2=[[sg.Image(r'/home/maroon/Desktop/messenger/Images/header1.png')],
    [sg.Text("FUCK OFF !!! Nothing to help you.", font="Helvetica "  + str(50), key='text')]]

layout = [[sg.TabGroup([[sg.Tab('Messages', t1, tooltip='All Messages come here'), sg.Tab('Help', t2)]], tooltip='need help?')]]       


window = sg.Window('Delhi Technological University', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    #if event == 'Show':
        # change the "output" element to be the value of "input" element
        #window['-OUTPUT-'].update(values['-IN-'])

window.close()

'''import PySimpleGUI as sg

sg.theme('green')  # please make your windows colorful
#sg.SystemTray.notify('Welcome to Intra-University Messenger', 'Connecting to server...')

chats= open('/home/maroon/Desktop/messenger/chats/inbox.txt','r').readlines()
fontSize = 12


layout = [[sg.Image(r'/home/maroon/Desktop/messenger/Images/header1.png')],
          #[sg.Text('This is my pink color'),sg.Text(size=(12,1),colors=('pink','blue'))],

          #sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),
           #sg.Slider(range=(6,172), orientation='h', size=(10,20),
           #change_submits=True, key='slider', font=('Helvetica 20')),
           [sg.Text("Inbox", font="Helvetica "  + str(50), key='text')],
          [sg.Listbox(values=chats, size=(25, 12), key='-LIST-', enable_events=True)],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    #if event == 'Show':
        # change the "output" element to be the value of "input" element
        #window['-OUTPUT-'].update(values['-IN-'])

window.close()
'''