from tkinter import *
from tkinter import filedialog
##Janela
root=Tk("Text Editor")
root.title("Editor de Texto")
text=Text(root)
text.grid()
text.grid()
##BOTÃO DE SALVAR
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()
button=Button(root, text="Salvar", command=saveas)
button.grid() 
root.mainloop()

