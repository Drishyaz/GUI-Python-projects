# TWO COLUMNS
# COLUMN 1 - ROW 1 - INPUT BOX AND BROWSE BUTTON
# COLUMN 1 - ROW 2 - LISTBOX - IT WILL DISPLAY ALL THE .PY FILES IN THE SELECTED FOLDER

# COLUMN 2 - ROW 1 - INSTRUCTION TO SELECT A FILE FROM THE LIST ON THE LEFT
# COLUMN 2 - ROW 2 - SELECTED FILE.PY NAME
# COLUMN 2 - ROW 3 - A MULTILINE THAT DISPLAYS THE CONTENTS OF THE SELECTED FILE

# WE IMPORT PySimpleGUI FOR ALL GUI HELP, OS FOR GETTING ACCESS TO SYSTEM'S FILE PATHS, RE FOR FINDING THE CORRECT MATCHING FILE
import PySimpleGUI as pg
import os.path
import re

# THIS IS THE FIRST COLUMN WHICH WILL HAVE 2 ROWS - ONE FOLDER BROWSE OPTION WITH LABEL, INPUT, BUTTO - TWO LISTBOX THAT WILL DISPLAY FILES
file_list_column = [
    [
        pg.Text("Project Folder: "),
        pg.In(size = (25,1), enable_events=True, key='-FOLDER-'),
        pg.FolderBrowse(),
    ],
    [
        pg.Listbox(values=[], enable_events=True, size = (40,30), key = "-FILE LIST-")
    ]
]

# THIS IS THE SECOND COLUMN THAT WILL DISPLAY THE SELECTED FILE.PY NAME - AND ITS CONTENTS IN THE MULTILINE IN ROW 2
proj_viewer = [
    [pg.Text("Choose a file.py from the list on the left: ")],
    [pg.Text(size = (25,1), key = '-TOUT-')],
    [pg.Multiline(size = (40,30), key = '-TEXT-')],
]

# THIS IS THE MAIN LAYOUT OF THE WINDOW - IT HAS 1ST COLUMN - A VERTICAL SEPERATOR - AND THE 2ND COLUMN
layout = [
    [
        pg.Column(file_list_column),
        pg.VSeperator(),
        pg.Column(proj_viewer),
    ]
]

# WE CREATE AN OBJECT FOR THE Window CLASS SO WE CAN READILY ACCES IT - PARAMETERS - WINDOW TITLE - AND THE MAIN LAYOUT OF THE WINDOW
win = pg.Window("Project Viewer",layout)

# INFINITE LOOP MEANS THE WINDOW KEEPS RUNNING UNTIL WE EXIT
while True:
    # THE EVENTS AND INPUT VALUES BY THE USER ARE READ INTO EVENT, VALUES[] RESPECTIVELY.
    event, values = win.read()

    # IF WINDOW IS CLOSED THEN LOOP BREAKS AND PROGRAM ENDS
    if event == pg.WIN_CLOSED:
        break

    # IF USER SELECTS A FOLDER with 'BROWSE'
    if event == '-FOLDER-':
        folder = values['-FOLDER-']
        try:
            # WE GET ALL THE FOLDERS OR DIRECTORIES LISTED INSIDE THE SELECTED FOLDER IN THE file_list
            file_list = os.listdir(folder)
        except:
            # IF BY CHANCE THERE IS AN EXCEPTION THEN file_list STAYS EMPTY
            file_list = []
        
        # WE CREATE A REGEX THAT WILL MATCH ANY FILES WITH THE EXTENSION .PY - IT HAS TO HAVE A NAME OF ATLEAST 1 LETTER - NO EMPTY NAMES
        regex = r'\b.+(.py)\b'
        # NEXT CHECK - IF EVERY FILE IN file_list MATCHES THE GIVEN REGEX EXPRESSION - THAT IS ONLY PYTHON FILES
        fnames = [
            f 
            for f in file_list
            #os.path.isfile(os.path.join(folder,f)) and
            if re.search(regex,f)
        ]

        # ONLY PYTHON FILES ARE DISPLAYED IN THE LISTBOX
        # MEANS IF THERE ARE OTHER FILES TOO, STILL DISPLAY ONLY .PY FILES
        win['-FILE LIST-'].update(fnames)
    
    # NOW IF YOU SELECT A FILE FROM THE LISTBOX
    elif event == '-FILE LIST-':
        try:
            # GET THE FILE NAME
            selected_file = values['-FILE LIST-'][0]
            # GET THE FOLDER NAME
            folder_location = values['-FOLDER-']

            # GET THE SELECTED FILE'S LOCATION OR PATH
            with open(os.path.join(folder_location,selected_file)) as fl:
                # READ THE CONTENTS OF THE FILES AND STORE IN lines
                lines = fl.read()

            # NOW DISPALY THE SELECTED FILE'S NAME
            win['-TOUT-'].update(os.path.join(selected_file))
            # DISPLAY THE CONTENT OF SELECTED FILE IN MULTILINE
            win['-TEXT-'].update(lines)

        except:
            pass

# CLOSE THE WINDOW AFTER USER CLICKS 'EXIT'
win.close()