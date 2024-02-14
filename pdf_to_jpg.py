import os
from pdf2image import convert_from_path
import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Input file'), sg.InputText()],
            [sg.Text('Output folder path'), sg.InputText()],
            [sg.Listbox(values=['PNG', 'JPG'], size=(5))],
            [sg.Button('Convert'), sg.Button('Quit')] ]

# Create the Window
window = sg.Window(title='PDF to IMG', 
                   layout=layout,
                   background_color='#BAD0E8',
                   button_color='#83A9D1')


def input_folder_OR_file(user_input_folder='', user_input_file='', filelist=[], f='', 
                         error_message_list=[]):
    while True:
        try: 
            filelist = []
            try: 
                for user_input_file in os.listdir(user_input_folder):
                    if '.' not in user_input_file:
                        f = user_input_folder + '/' + user_input_file
                        filelist.append(f)
                    else:
                        f = user_input_folder + '/' + user_input_file
                        sg.popup(f"{f} is not a supported filetype.")
            except:
                filelist.append(user_input_folder)

            #sg.popup(filelist)
            convert_to_img(filelist)

        except WindowsError as err:
            print(f"Error! {err}")
            input_folder_OR_file()
        


def convert_to_img(filelist, user_output_folder='', filename='', x=[], i='', images=''):

    user_output_folder = input("Select an output folder:\n>> ").replace("\\", "/").strip('""')
    
    for x in range(len(filelist)):
        filename = filelist[x].rsplit('/')
        filename = filename[-1].rsplit('.')
        filename = filename[0]#.replace(".", "_").strip(']').strip("'")
        images = convert_from_path(filelist[x], poppler_path=r"C:\Program Files\poppler-23.11.0\Library\bin")
        for i in range(len(images)):
            
            # Save pages as images in the pdf
            images[i].save(user_output_folder + '\\' + str(filename) + '_' + str(i) +'.jpg', 'JPEG')


#run script
while True:
    event, values = window.read()
    user_input_folder = values[0].replace("\\", "/").strip('""')
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    if event == 'Convert':
        if user_input_folder == '' or user_input_folder != '/':
            sg.popup('Please input a file or folder!', any_key_closes=True)
        
        #input_folder_OR_file()