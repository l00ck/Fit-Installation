from tkinter import *
from shutil import copyfile
import copysc


root = Tk()
root.resizable(width=False, height=False)
root.wm_title("Fit Installer")
root.iconbitmap("fit.ico")

copysccm = copysc.Copy()


print("wtf")

###############
def test(x, y):
    print(x + y)


##wtf
#################



AutoLoginGroup = LabelFrame(root, text="Autologin", padx=5, pady=5)
groupAll = LabelFrame(root, text="Options", padx=5, pady=5)

buttoncpysccm = Button(groupAll, text="Copy Sccm", command= copysccm.copyfile)
buttonsccm = Button(groupAll, text="Install Sccm")
buttonuninstall = Button(groupAll, text="Uninstall Filezilla")
buttonAutostart = Button(groupAll, text="Fit 2 Autostart")

buttonAutologin = Button(AutoLoginGroup, text="Create Autologin",
                         command=lambda: test(entryUsername.get(), entryPassword.get()))

labelUsername = Label(AutoLoginGroup, text="Username: ")
labelPassword = Label(AutoLoginGroup, text="Password: ")
entryUsername = Entry(AutoLoginGroup)
entryPassword = Entry(AutoLoginGroup)

entryPassword.insert(0, "Dss12345")
entryUsername.insert(0, "grpdemanfit0")

AutoLoginGroup.grid(row=0, column=1)
groupAll.grid(row=0, column=0)
buttoncpysccm.grid(row=0, column=0, sticky=N + S + E + W)
buttonsccm.grid(row=1, column=0, sticky=N + S + E + W)
buttonuninstall.grid(row=2, column=0, sticky=N + S + E + W)
buttonAutostart.grid(row=3, column=0, sticky=N + S + E + W)

labelUsername.grid(row=0, column=2)
labelPassword.grid(row=1, column=2)
buttonAutologin.grid(row=2, column=3)
entryUsername.grid(row=0, column=3)
entryPassword.grid(row=1, column=3)

root.mainloop()
