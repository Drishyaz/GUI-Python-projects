import PySimpleGUI as pg
import os

def newFile():
    window['-TEXT-'].update("")
    window['-FILE NAME-'].update("untitled.txt")

def openFile():
    try:
        file_name = pg.popup_get_text('Enter the file name you want to open: ',title = 'Open File')
        current_direc = os.getcwd()
        file_location = os.path.join(current_direc,file_name)
        if os.path.exists(file_location):
            with open(file_location) as f:
                lines = f.read()
                
            window['-TEXT-'].update(lines)
            window['-FILE NAME-'].update(file_name)
        else:
            pg.popup('The file \''+ file_name + '\' does not exist.')

    except TypeError:
        pass

def saveFile():
    try:
        file_name = pg.popup_get_text('Enter file name to save as:', title = 'Save File')
        text = values['-TEXT-']
        current_direc = os.getcwd()
        file_location = os.path.join(current_direc,file_name)
        if os.path.exists(file_location):
            pg.popup('The file with the given name \'' + file_name + '\' already exists.')
        else:
            with open(file_name,"x") as f:
                f.write(text)
            window['-FILE NAME-'].update(file_name)
    except TypeError:
        pass

def font_window():
    font_style = [
        'System','Terminal','Modern','Roman','Script','Courier','Arial','Calibri','Cambria','Candara','Consolas','Constantia','Georgia','Impact','Onyx','Forte'
    ]
    font_size = [
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40
    ]
    font_style_col = [
        [pg.Input(key = '-style-')],
        [pg.Listbox(font_style,enable_events=True, size = (40,15),key='-style_list-')],
    ]
    font_size_col = [
        [pg.Input(key = '-size-')],
        [pg.Listbox(font_size,enable_events=True, size = (40,15),key='-size_list-')],
    ]
    sample_font = [
        [pg.Text('Sample font look', font = ('Arial',12))],
        [pg.Text('AaByYyZz',font = ('Arial',22), key = '-sample-')]
    ]
    btn_col = [
        [pg.OK()],
        [pg.Cancel()]
    ]
    layout = [
        [
            pg.Column(font_style_col),
            pg.VSeperator(),
            pg.Column(font_size_col)
        ],
        [
            pg.Column(sample_font),
            pg.VSeperator(),
            pg.Column(btn_col)
        ]
    ]

    #pg.set_options(font = ('Arial',18))
    window = pg.Window("Font Settings", layout, modal = True, size = (650,400))

    while True:
        event,values = window.read()
        sample = 'AaByYyZz'
        if event == pg.WIN_CLOSED or event == 'Cancel':
            break

        elif event == '-style_list-':
            selected_style = values['-style_list-'][0]
            window['-style-'].update(selected_style)
            try:
                window['-sample-'].update(font = (selected_style,selected_size)) 
            except NameError:
                window['-sample-'].update(font = (selected_style,22))

        elif event == '-size_list-':
            selected_size = values['-size_list-'][0]
            window['-size-'].update(selected_size)
            try:
                window['-sample-'].update(font = (selected_style,selected_size))  
            except NameError:
                window['-sample-'].update(font = ('Default font',selected_size))

        elif event == 'OK':
            break
            
    window.close()
    return selected_style,selected_size

#STILL WORKING ON THE REFRESHING
def theme_select():
    theme_list = [
        'Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 'DarkPurple6', 'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10', 'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 'DarkTeal9', 'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan', 'HotDogStand', 'Kayak', 'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6', 'LightBlue7', 'LightBrown', 'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3', 'LightBrown4', 'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen', 'LightGreen1', 'LightGreen10', 'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8', 'LightGreen9', 'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6', 'LightPurple', 'LightTeal', 'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'PythonPlus', 'Reddit', 'Reds', 'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono', 'Topanga'
    ]
    theme_list.sort()
    layout = [
        [pg.Input(key = '-theme select-')],
        [pg.Listbox(theme_list, enable_events=True, size = (45,15),key='-themes-')],
        [pg.OK(),pg.Cancel()]
    ]

    window = pg.Window('Theme Selector',layout,size = (400,400))#, modal = True)

    while True:
        event, values = window.read()

        if event == pg.WIN_CLOSED or event == 'Cancel':
            break
        
        elif event == '-themes-':
            selected_theme = values['-themes-'][0]
            window['-theme select-'].update(selected_theme)
            if event == 'OK':
                break
    
    window.close()
    return selected_theme

menu_def = [
    ['File',['New','Open','Save','Exit']],
    ['Settings',['Font','Theme']]
]

layout = [
    [pg.Menu(menu_def)],
    [pg.Text("untitled.txt", size = (20,1), key = '-FILE NAME-')],
    [pg.Multiline(size = (100,30), key = '-TEXT-')]
]

window = pg.Window("Py Notepad",layout, size = (715,500))

while True:
    event, values = window.read()

    if event == pg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'New':
        newFile()

    elif event == 'Open':
        openFile()

    # IF FILE ALREADY SAVED THEN NO SAVE - work left
    elif event == 'Save':
        saveFile()
    
    elif event == 'Font':
        val = font_window()
        if val == None:
            pass
        else:
            window['-TEXT-'].update(font=val)
            #pg.set_options(font=val)
    
    elif event == 'Theme':
        selected_theme = theme_select()
        pg.theme(selected_theme)
        window.refresh()

window.close()
