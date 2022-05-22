import PySimpleGUI as sg

sg.change_look_and_feel('GreenTan')

layout = [
    [sg.Text('Enter distance in kms'), sg.Input(key='-KILO-', do_not_clear=False, size=(5,1))],
    [sg.Text(size=(5,1), justification='right', key='-OUT-KM-'), sg.Text('Kilometers = '), sg.Text(size=(5,1), key='-OUT-MIL-'), sg.Text(' miles')],
    [sg.Button('Convert', bind_return_key = True), sg.Button('Quit')]
    ]

window = sg.Window('Kilometer to Mile Conversion', layout)

while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        break
    window['-OUT-KM-'].update(values('-KILO-'))
    window['-OUT-MIL-'].update(float(values['-KILO-']))*0.6214



window.close()