import os
from pdf2image import convert_from_path
import PySimpleGUI as sg

# All the stuff inside your window.
layout = [  [sg.Text('Input file'), sg.InputText(key='-INPUT-FOLDER-'), 
             #sg.Button('select_file', image_filename=r"C:\Users\shlomof\Documents\code\pdf2image_gui\icons\add-file-8.png", image_size=(24, 24), key='-SELECT_FILE-'), 
             sg.Listbox(values=['PNG', 'JPG'], default_values='PNG' , size=(6, 2), key='-FILETYPE-', no_scrollbar=True)],
            [sg.Text('Output folder path'), sg.InputText(key='-OUTPUT-FOLDER-')],
            [sg.ProgressBar(max_value=(10), key='-PROGRESS_BAR-')],
            [sg.Button('Convert'), sg.Button('Quit')] ]
count = 0
# Create the Window
window = sg.Window(title='PDF to IMG', 
                   layout=layout,
                   background_color='#BAD0E8',
                   button_color='#83A9D1')    


#run script
def convert_on_press (window, event, values):
    
    print(values['-INPUT-FOLDER-'])
    if str(values['-INPUT-FOLDER-']) == '':
        sg.popup('Please input a file or folder!', any_key_closes=True)
        print("no inputfile")
        pass
    elif str(values['-OUTPUT-FOLDER-']) == '':
        sg.popup('Please select an output folder!', any_key_closes=True)
        print("no output path")
        pass
    else:
        print("working")
        
        try:
            user_input_folder = str(values['-INPUT-FOLDER-'].replace("\\", "/").strip('""'))
            user_output_folder = str(values['-OUTPUT-FOLDER-'].replace("\\", "/").strip('""'))
            print(user_input_folder, user_output_folder)
            filelist = []
            try: 
                for user_input_file in os.listdir(user_input_folder):
                    if '.' not in user_input_file:
                        f = user_input_folder + '/' + user_input_file
                        filelist.append(f)
                    else:
                        f = user_input_folder + '/' + user_input_file
                        sg.popup(f"{f} is not a supported filetype.")
                        pass
            except:
                filelist.append(user_input_folder)

            try:
                for x in range(len(filelist)):
                    print("did you get here1")
                    filename = filelist[x].rsplit('/')
                    filename = filename[-1].rsplit('.')
                    filename = filename[0]#.replace(".", "_").strip(']').strip("'")
                    images = convert_from_path(filelist[x], dpi=800, poppler_path=r"C:\Program Files\poppler-23.11.0\Library\bin")
                    for i in range(len(images)):
                        
                        # Save pages as images in the pdf
                        print("did you get here2")
                        print(values['-FILETYPE-'])
                        if values['-FILETYPE-'] == ['JPG']:
                            print(values['-FILETYPE-'])
                            images[i].save(user_output_folder + '\\' + str(filename) + '_' + str(i) +'.jpg', 'JPEG')
                            pass

                        elif values['-FILETYPE-'] == ['PNG']:
                            print(values['-FILETYPE-'])
                            images[i].save(user_output_folder + '\\' + str(filename) + '_' + str(i) +'.png', 'PNG')
                            pass

                        else:
                            images[i].save(user_output_folder + '\\' + str(filename) + '_' + str(i) +'.png', 'PNG')
                            pass

                    sg.popup(f"{filename} is done!")

            except:
                err = ''
                sg.popup(f"Error! Check your files. \n{err}")
                pass                 
                    

        except WindowsError as err:
            sg.popup(f"Error! {err}")
            pass



           

while True:
    event, values = window.read()    
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    if event == 'Convert':
        convert_on_press(window, event, values)
    #if event == 'select_file':
      #  sg.popup_get_file()