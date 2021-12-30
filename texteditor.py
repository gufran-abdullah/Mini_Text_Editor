#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Python Text Editor @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os


root = tk.Tk()
root.geometry('1200x800')
root.title('Python Text Editor')


#============================ Main Menu ========================
main_menu = tk.Menu()

# File Icons
new_icon = tk.PhotoImage(file='imgs/new.png')
open_icon = tk.PhotoImage(file='imgs/open.png')
save_icon = tk.PhotoImage(file='imgs/save.png')
save_as_icon = tk.PhotoImage(file='imgs/save_as.png')
exit_icon = tk.PhotoImage(file='imgs/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# Edit Icons
copy_icon = tk.PhotoImage(file='imgs/copy.png')
paste_icon = tk.PhotoImage(file='imgs/paste.png')
cut_icon = tk.PhotoImage(file='imgs/cut.png')
clear_all_icon = tk.PhotoImage(file='imgs/clear_all.png')
find_icon = tk.PhotoImage(file='imgs/find.png')

edit = tk.Menu(main_menu, tearoff=False)

#View Icons
tool_bar_icon = tk.PhotoImage(file='imgs/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='imgs/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)

#Color Theme Icon
light_default_icon = tk.PhotoImage(file='imgs/light_default.png')
light_plus_icon = tk.PhotoImage(file='imgs/light_plus.png')
dark_icon = tk.PhotoImage(file='imgs/dark.png')
red_icon = tk.PhotoImage(file='imgs/red.png')
monokai_icon = tk.PhotoImage(file='imgs/monokai.png')
night_blue_icon = tk.PhotoImage(file='imgs/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' : ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#474747','#ffd596'),
    'Night Blue' : ('#ededed','#6b9dc2')
}

#Cascading
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
#---------------------------- End Main Menu --------------------

#============================ Toolbar ========================
tool_bar = ttk.Label(root)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# Font Box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

# Size Box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(8)
font_size.grid(row=0,column=1,padx=5)

# Bold Button
bold_icon = tk.PhotoImage(file='imgs/bold.png')
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

# Italic Button
italic_icon = tk.PhotoImage(file='imgs/italic.png')
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

# Underline Button
underline_icon = tk.PhotoImage(file='imgs/underline.png')
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# Font Color Button
font_color_icon = tk.PhotoImage(file='imgs/color_picker.png')
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

# Left Align Button
left_icon = tk.PhotoImage(file='imgs/align_left.png')
left_btn = ttk.Button(tool_bar,image=left_icon)
left_btn.grid(row=0,column=6,padx=5)

# Center Align Button
center_icon = tk.PhotoImage(file='imgs/align_center.png')
center_btn = ttk.Button(tool_bar,image=center_icon)
center_btn.grid(row=0,column=7,padx=5)

# Right Align Button
right_icon = tk.PhotoImage(file='imgs/align_right.png')
right_btn = ttk.Button(tool_bar,image=right_icon)
right_btn.grid(row=0,column=8,padx=5)
#---------------------------- End Toolbar --------------------

#============================ Text Editor ========================
text_editor = tk.Text(root)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(root)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# Font Family and Font Size Functionallity
current_font_family = 'Arial'
current_font_size = 16

# Change Font Functions
def change_font_family(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font_family)
font_size.bind("<<ComboboxSelected>>",change_font_size)

## Buttons Functionallity
# Bold Button
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

# Italic Button
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

# Italic Button
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

# Font Color Button
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
    
font_color_btn.configure(command=change_font_color)

# Left Allignment Button
def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

left_btn.configure(command=align_left)

# Center Allignment Button
def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

center_btn.configure(command=align_center)

# Right Allignment Button
def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

right_btn.configure(command=align_right)

text_editor.configure(font=('Arial',16))

#---------------------------- End Text Editor --------------------

#============================ Status Bar ========================
status_bar = ttk.Label(root,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

# Status Bar  Functionality
text_changed = False
def change_status(event=None):
    global text_changed
    if text_editor.edit_modified:
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        #chars = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        chars = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters : {chars} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',change_status)
    
#---------------------------- End Status Bar --------------------

#============================ Main Menu Functionality ========================
# New File Functionality
url = ''
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)
#########File Commands
# New File    
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+n',command=new_file)

# Open File Functionallity
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as file_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,file_read.read())
    except FileNotFoundError:
        return
    except:
        return
    root.title(os.path.basename(url))
# Open File
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+o',command=open_file)

# Save File Functionallity
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as file_writer:
                file_writer.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0,tk.GET)
            url.write(content2)
            url.close()
    except:
        return
# Save File
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+s',command=save_file)

#Save as Functionallity
def saveas_file(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return
# Save as File    
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+s',command=saveas_file)

# Exit Fromm Editor Functionallity
def exit_from_editor(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do You want to save this file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        root.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    root.destroy()
            elif mbox is False:
               root.destroy()
        else:
            root.destroy()
    except:
         return       
# Exit From Editor
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+q',command=exit_from_editor)

########Edit Commands
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+c',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+v',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+x',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,command=lambda:text_editor.delete(1.0,tk.END))

#Find Functionallity
def find_function(event=None):
    find_dialog = tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)

    #Find Function
    def find():
        word = find_entry.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    #Replace Function
    def replace():
        word = find_entry.get()
        replace_text = replace_entry.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    #Find Frame
    find_frame = ttk.LabelFrame(find_dialog,text='Find/Replace')
    find_frame.pack(pady=20)

    #Find Labels
    text_find_label = ttk.Label(find_frame,text='Find : ')
    text_replace_label = ttk.Label(find_frame,text='Replace : ')

    #Find Entry
    find_entry = ttk.Entry(find_frame,width=30)
    replace_entry = ttk.Entry(find_frame,width=30)

    #Find Buttons
    find_btn = ttk.Button(find_frame,text='Find',command=find)
    replace_btn = ttk.Button(find_frame,text='Replace',command=replace)

    #Label Grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    #Entry Grid
    find_entry.grid(row=0,column=1,padx=4,pady=4)
    replace_entry.grid(row=1,column=1,padx=4,pady=4)

    #Buttons Grid
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=2,padx=8,pady=4)

    find_dialog.mainloop()
    
# Find From File
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+f',command=find_function)

#######View Check Button
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

#Toolbar Function
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True

#Statusbar Function
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True
    
view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

#######Color theme

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
                                    


count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count += 1

#---------------------------- End Main Menu Functionality --------------------


root.config(menu=main_menu)

#Bind Shoetcut Keys
root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-Alt-s>",saveas_file)
root.bind("<Control-q>",exit_from_editor)
root.bind("<Control-f>",find_function)

root.mainloop()
