from tkinter import *
import re

#AMITY CONVERT STRING TO SQL SERVER FORMAT

def Main():
    global root

    root = Tk()
    ##title
    root.title("Convert Frame")

    width = 500
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    inputSc = InputScreen(root)
    inputSc.pack(side=LEFT,fill=X)

    outputSc = OutputScreen(root)
    outputSc.pack(side=RIGHT,fill=X)

    Title = Label(inputSc, text="Input Data", font=(18))
    Title.pack(side=TOP)

    T = Text(inputSc,height=10, width=20)
    T.config(state='normal')
    T.pack(side=LEFT)

    Submit = Button(inputSc, text='Submit', width=6,
                    height=2, command=lambda: inputSc.submit(T, T1))
    Submit.pack(side=BOTTOM)

    Title1 = Label(outputSc, text="Output Data", font=(18))
    Title1.pack(side=TOP)

    T1 = Text(outputSc, height=10, width=20)
    T1.pack(side=RIGHT)

    Clear = Button(outputSc, text='Clear', width=6, height=2,
                  command=lambda: outputSc.clear(T, T1))
    Clear.pack(side=BOTTOM)

    root.mainloop()


class InputScreen(Frame):
    
    def RegexOper(self,T):
        output_text = T.get('1.0', 'end-1c')
        a = (output_text).strip()
        a = re.sub('\s+', '\',\'', a)
        a = re.sub(r'^\A', '(\'', a)
        a = re.sub(r'\Z', '\')', a)
        return a
        
    def submit(self, T, T1):
        T.config(state='disabled')
        T1.config(state='normal')
        T1.insert(END,self.RegexOper(T))
        T1.config(state='disabled')
        
class OutputScreen(Frame):

    def clear(self,T,T1):
        T.config(state='normal')
        T1.config(state='normal')
        T.delete('1.0',END)
        T1.delete('1.0',END)
        T1.config(state='disabled')

if __name__ == '__main__':
    Main()

## AMITY 
'''
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

TextString=StringVar() # Value saved here

def submit():
  print(TextString.get())
  return ''

ttk.Entry(mainframe, width=40,textvariable=TextString,justify = CENTER,font = ('courier', 15, 'bold')).grid(column=2, row=1)
ttk.Label(mainframe, text="Text Input").grid(column=1, row=1)

ttk.Button(mainframe, text="Submit", command=lambda : submit()).grid(column=2, row=3)

root.mainloop()

'''
##################################################
'''
TextString = StringVar() 
  
# This class is used to add styling 
# to any widget which are available 
def submit():
  print(TextString.get())
  return ''

TextIn =ttk.Entry(root,textvariable = TextString, justify = CENTER,font = ('courier', 15, 'bold'))  
TextIn.pack(side = TOP) 

Submit = ttk.Button(root, text = 'Submit', command = lambda : submit()) 
Submit.pack(side = TOP, pady = 10) 

root.mainloop() 


'''


# f= open("C:\\Users\\52038474\\Documents\\LEARNING\\PYTHON 3\\Python\\MINI PROJECTS\\SQL_Format\\A.txt",'r')

# a=(f.read()).strip()

# a=re.sub('\s+','\',\'',a)

# a=re.sub(r'^\A','(\'',a)

# a=re.sub(r'\Z','\')',a)

'''
################################################################

raw_data='   Amit Yadav python is     t    '

raw_data=raw_data.strip()

raw_data=re.sub('\s+','\',\'',raw_data)

raw_data=re.sub(r'^\A','(\'', raw_data)

raw_data=re.sub(r'\Z','\')',raw_data)

print(raw_data)
'''







'''
################################################################

raw_data='   Amit Yadav python is     t    '

raw_data=raw_data.strip()

raw_data=re.sub('\s+','\',\'',raw_data)

raw_data=re.sub(r'^\A','(\'', raw_data)

raw_data=re.sub(r'\Z','\')',raw_data)

print(raw_data)
'''
