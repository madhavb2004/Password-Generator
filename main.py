'''
Creating an interactive GUI
Creates a random password
Decrypting the password using hashing algorithm
File operations for storing passwords
Password duplication check
'''
import tkinter as tk
import random
import hashlib
from tkinter import messagebox

TEXTBOX_BACKGROUND_COLOUR='light cyan'
TITLE_ROOT='Passsword Generator'
DIMENSIONS_ROOT="600x400"
SHOW_ERROR="Error"
ERROR_MESSAGE="Invalid input\nPlease enter a valid number"
TEXTBOX_1='Password'
TEXTBOX_2='Hashed password'
TEXT_FONTSTYLE='ariel'
BOLD='bold'
PASSW_LABEL_TEXT='Enter number of characters:'
PASSW_LABEL_FONT='calibre'
NORMAL='normal'
BOTTON_1_TEXT='Submit'
BOTTON_2_TEXT="Reset"

password_list = []

def Dictionary(range1,range2):
	another_random = random.randint(range1,range2)
	ch=chr(another_random)
	return ch

def password_generator2(no_char):
	corresponding_set = {1 : Dictionary(33,43), 2:Dictionary(48,57), 3:Dictionary(58,64), 4:Dictionary(65,90), 5:Dictionary(91,96), 6:Dictionary(97,122), 7:Dictionary(123,126)}
	no_of_char = no_char
	psswd = ['None'] * no_of_char
	count = 0
	while count < no_of_char:
		random_number = random.randint(1,7)
		psswd[count] = corresponding_set[random_number]
		count += 1
	password = "".join(psswd)
	
	if(password in password_list):
		messagebox.showerror(SHOW_ERROR,"Password already exists. Regenerate your password")
		return None
	else:
		password_list.append(password)
		write_to_file()
	return password

def hash_pswd(password):
	hash_obj = hashlib.sha256(password.encode())
	hash_digest = hash_obj.hexdigest()
	return hash_digest

def read_generated_passwords_from_file():
	with open(r"File Path", "r") as file:
		data = file.readline()
		# print(data)
		read_passwords = data.split(',')
	for p in read_passwords:
		password_list.append(p)
	
def write_to_file():
	print(password_list)
	print(','.join(password_list))
	with open(r"File Path", "w") as file:
		new_data = ','.join(password_list)
		file.write(new_data)

def res_command():
	passw_entry.delete(0, 'end')
	result.delete(1.0,'end')
	hash_result.delete(1.0,'end')

def response():
	result.delete("1.0","end")
	try:
		value = int(name_var.get())
	except ValueError:
		messagebox.showerror(SHOW_ERROR,ERROR_MESSAGE)
		return
	print(value)
	psw = password_generator2(value)
	if(psw):
		hpsw=hash_pswd(psw)
		result.insert(tk.END,psw)
		hash_result.insert(tk.END,hpsw)
		result.grid(row=5,column=1)
		hash_result.grid(row=7,column=1)
		text_label=tk.Label(root,text=TEXTBOX_1,font=(TEXT_FONTSTYLE,10,BOLD))
		text_label.grid(row=4,column=0)
		text2_label=tk.Label(root,text=TEXTBOX_2,font=(TEXT_FONTSTYLE,10,BOLD))
		text2_label.grid(row=6,column=0)

read_generated_passwords_from_file()

root = tk.Tk()
root.geometry(DIMENSIONS_ROOT)
root.title(TITLE_ROOT)

name_var=tk.StringVar()
psw=''
hpsw=''

result=tk.Text(root,
			   height=8,
			   width=40,
			   bg= TEXTBOX_BACKGROUND_COLOUR
)
hash_result=tk.Text(root,
					height=8,
					width=40,
					bg=TEXTBOX_BACKGROUND_COLOUR
)

name_var=tk.StringVar()

passw_label = tk.Label(root, text = PASSW_LABEL_TEXT, font = (PASSW_LABEL_FONT,10,BOLD))
passw_entry=tk.Entry(root, textvariable = name_var, font = (PASSW_LABEL_FONT,10,NORMAL))

sub_btn=tk.Button(root,text = BOTTON_1_TEXT, command = response)
sub_btn.grid(row=2,column=1)

passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)

reset_btn=tk.Button(root,text=BOTTON_2_TEXT,command=res_command)
reset_btn.grid(row=8,column=1)

root.mainloop()