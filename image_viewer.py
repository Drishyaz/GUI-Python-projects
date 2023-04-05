import PySimpleGUI as sg
import os.path

#window layout of two column
file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=[],enable_events=True,size=(40,20),key="-FILE LIST-")
    ]
]   

#for now will only show the name of the chosen file
img_viewer = [
    [sg.Text("Choose an image from the list on left:")],
    [sg.Text(size=(40,1),key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

#------------ full layout -------------
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(img_viewer),
    ]   
]

window = sg.Window("Image Viewer",layout)

while True:
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    #folder name was filled in, so we make a list of files
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            #get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png",".gif"))
        ]

        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":
    # a file was chosen from the listbox
        try:
            filename = os.path.join(values["-FOLDER-"],values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

window.close()