import subprocess
from sys import argv
import tkinter
from tkinter.constants import BOTTOM

from requests.auth import parse_dict_header

def shell(command):
    subprocess.run(command,shell=True)

def run(path):
    try:
        shell(f"python3 {path}")            
    except:
        try:
            shell(f"python {path}")
        except:
            try:
                shell(f"py {path}")
            except:
                pass
            
def debug(path):
    try:
        shell(f"python3 {path} -v")          
    except:
        try:
            shell(f"python {path} -v")
        except:
            try:
                shell(f"py {path} -v") #aggiungere altri setting del run (for ex. -v or -V or --version)
            except:
                pass
        
        
def main(path):
    root=tkinter.Tk()
    root.title("instantPythonRunner")
    root.attributes("-topmost", True)
    root.geometry("200x200+70+100")
    root.configure(background="white")
    
    RunButton=tkinter.Button(root, command=run(path),background="white", text="RUN", highlightbackground="white", fg="black", height=3, width=18, font="helvetica").grid(pady=5, padx=5)
    
    RunWithDebugButton=tkinter.Button(root,command=debug(path), background="white", text="DEBUG", highlightbackground="white", fg="black", height=3, width=18, font="helvetica").grid(pady=5, padx=5)
    root.mainloop()
    
def askForPath():
   
    root=tkinter.Tk()
    root.title("instantPythonRunner - pathSelector")
    root.attributes("-topmost", True)
    root.geometry("200x200+70+100")
    root.configure(background="white")
    
    PathEntry=tkinter.Entry(root,background="white", highlightbackground="white", fg="black", font="helvetica")
    PathEntry.grid(pady=5, padx=5)
    
    ClickButton=tkinter.Button(root,command=main(PathEntry.get()), background="white", text="GO", highlightbackground="white", fg="black", height=3, width=18, font="helvetica").grid(pady=5, padx=5)
    
    root.mainloop()
    
    
if __name__=="__main__":
    try:
        path=argv[1]
        main(path)
    except:
        print(f"usage: python3 {argv[0]} <the path of the your program>")
        path=askForPath()