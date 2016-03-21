#############################################################################
###                                                                       ###
### A Registry Editor and CMD unblocker in Python.                        ###
### Copyright (C) 2016  lenku                                             ###
###                                                                       ###
### This program is free software: you can redistribute it and/or modify  ###
### it under the terms of the GNU General Public License as published by  ###
### the Free Software Foundation, either version 3 of the License, or     ###
### (at your option) any later version.                                   ###
###                                                                       ###
### This program is distributed in the hope that it will be useful,       ###
### but WITHOUT ANY WARRANTY; without even the implied warranty of        ###
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ###
### GNU General Public License for more details.                          ###
###                                                                       ###
### You should have received a copy of the GNU General Public License     ###
### along with this program.  If not, see <http://www.gnu.org/licenses/>. ###
###                                                                       ###
#############################################################################

### First check to see if program is elevated
import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'
if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb = 'runas',
                         lpFile = sys.executable,
                         lpParameters = params)
    sys.exit(0)

### IMPORTS
import tkinter
import winreg

### VARIABLES
# button width
button_width = 25

## Registry-related
# registry key read type
key_all = winreg.KEY_ALL_ACCESS
# assign HKCU hive to var
hkcu = winreg.HKEY_CURRENT_USER
# key path for regedit
reg_path = 'Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System'
# key name for regedit
reg_name = 'DisableRegistryTools'
# key path for CMD
cmd_path = 'Software\\Policies\\Microsoft\\Windows\\System'
# key name for CMD
cmd_name = 'DisableCMD'

## Assign key values to variables
# locate and open regedit key location
key = winreg.OpenKeyEx(hkcu, reg_path, 0, key_all)
# assign regedit value from key
reg_val = int(str(winreg.QueryValueEx(key, reg_name))[1])
# close key
key.Close()

# locate and open CMD key location
key = key = winreg.OpenKeyEx(hkcu, cmd_path, 0, key_all)
# assign CMD value from key
cmd_val = int(str(winreg.QueryValueEx(key, cmd_name))[1])
# close key
key.Close()

class InCommand(tkinter.Frame):
    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)
        # set title
        master.title('InCommand')
        # set window icon
        master.iconbitmap('InCommand.ico')
        # set to non-resizable
        master.resizable(width = False, height = False)
        # pack the frame
        self.pack()
        # create window widgets
        self.create_widgets()

    def create_widgets(self):
        # create regedit button
        self.reg_button = tkinter.Button(self)
        # if regedit is enabled
        if reg_val == 0:
            # set button text
            self.reg_button['text'] = 'Disable regedit'
            # set button text colour
            self.reg_button['fg'] = 'red'
            # seet onclick command
            self.reg_button['command'] = self.disable_reg
        # if regedit is disabled
        else:
            # set button text
            self.reg_button['text'] = 'Enable regedit'
            # set button text colour
            self.reg_button['fg'] = 'green'
            # set onclick command
            self.reg_button['command'] = self.enable_reg
        # seet button width
        self.reg_button['width'] = button_width
        # set button location on grid + padding
        self.reg_button.grid(row = 0, column = 0,
                             padx = (10, 10), pady = (10, 5))

        # create CMD button
        self.cmd_button = tkinter.Button(self)
        # if CMD is enabled
        if cmd_val == 0:
            # set button text
            self.cmd_button['text'] = 'Disable CMD'
            # set button text colour
            self.cmd_button['fg'] = 'red'
            # seet onclick command
            self.cmd_button['command'] = self.disable_cmd
        else:
            # set button text
            self.cmd_button['text'] = 'Enable CMD'
            # set button text colour
            self.cmd_button['fg'] = 'green'
            # seet onclick command
            self.cmd_button['command'] = self.enable_cmd
        # seet button width
        self.cmd_button['width'] = button_width
        # set button location on grid + padding
        self.cmd_button.grid(row = 1, column = 0,
                             padx = (10, 10), pady = (5, 10))

    def enable_reg(self):
        # locate and open regedit key location
        key = winreg.OpenKeyEx(hkcu, reg_path, 0, key_all)
        # assign key from regedit value
        winreg.SetValueEx(key, reg_name, 0, winreg.REG_DWORD, 0)
        # close key
        key.Close()

        # set button text
        self.reg_button['text'] = 'Disable regedit'
        # set button text colour
        self.reg_button['fg'] = 'red'
        # seet onclick command
        self.reg_button['command'] = self.disable_reg

    def disable_reg(self):
        # locate and open regedit key location
        key = winreg.OpenKeyEx(hkcu, reg_path, 0, key_all)
        # assign key from regedit value
        winreg.SetValueEx(key, reg_name, 0, winreg.REG_DWORD, 1)
        # close key
        key.Close()

        # set button text
        self.reg_button['text'] = 'Enable regedit'
        # set button text colour
        self.reg_button['fg'] = 'green'
        # seet onclick command
        self.reg_button['command'] = self.enable_reg

    def enable_cmd(self):
        # locate and open CMD key location
        key = winreg.OpenKeyEx(hkcu, cmd_path, 0, key_all)
        # assign key from CMD value
        winreg.SetValueEx(key, cmd_name, 0, winreg.REG_DWORD, 0)
        # close key
        key.Close()

        # set button text
        self.cmd_button['text'] = 'Disable CMD'
        # set button text colour
        self.cmd_button['fg'] = 'red'
        # seet onclick command
        self.cmd_button['command'] = self.disable_cmd

    def disable_cmd(self):
        # locate and open CMD key location
        key = winreg.OpenKeyEx(hkcu, cmd_path, 0, key_all)
        # assign key from CMD value
        winreg.SetValueEx(key, cmd_name, 0, winreg.REG_DWORD, 2)
        # close key
        key.Close()

        # set button text
        self.cmd_button['text'] = 'Enable CMD'
        # set button text colour
        self.cmd_button['fg'] = 'green'
        # seet onclick command
        self.cmd_button['command'] = self.enable_cmd

# create root widget/window
root = tkinter.Tk()
# create main application
app = InCommand(master = root)
# initiate tkinter loop
app.mainloop()
