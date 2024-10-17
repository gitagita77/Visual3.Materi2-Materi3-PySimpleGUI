import PySimpleGUI as sg
sg.theme("DarkGreen")
# sg.theme_background_color("#00FFFF")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("NPM       : 2210010187 ")],
                            [sg.Text("Nama      : Gita ")],
                            [sg.Text("Kelas     : 5E Regular Banjarmasin ")],
                            [sg.Text("Matkul    : Pemrograman Visual 3 ")],
                            ],
                    size=(400,200))
window()
window.close()