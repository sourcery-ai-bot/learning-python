# Graphical User Interface (GUI) atur cara untuk mengira Body Mass Index (BMI)
# Kumpulan Syabil & Amir
# Dibuat oleh Amir

# Python 3.x Sahaja
# Import module Tkinter
import tkinter as tk
from tkinter import ttk


# ===============================================FUNCTIONS=======================================================

# Mengira bmi dan mengetahui kategori sesuatu bmi
def kira_bmi(event=None):
	# Dapatkan input daripada entry input_ketinggian
	tinggi = input_ketinggian.get()
	# Dapatkan input daripada entry input_berat
	berat = input_berat.get()

	# Tukar string kepada nombor
	berat = float(berat)
	tinggi = float(tinggi)
	# Pengiraan BMI
	bmi = berat / (tinggi * tinggi)
	# Bundarkan bmi kepada 2 tempat perpuluhan
	bmi = round(bmi, 2)

	# Jika bmi kurang daripada 18.5
	if bmi < 18.5:
		kategori = "Kurang Berat Badan"

	# Jika bmi lebih atau sama dengan 18.5 dan kurang daripada 24.9
	elif bmi >= 18.5 and bmi < 24.9:
		kategori = "Berat Badan Normal"

	# Jika bmi lebih atau sama dengan 25.0 dan kurang daripada 29.9
	elif bmi >= 25.0 and bmi < 29.9:
		kategori = "Lebih Berat Badan"

	# Jika bmi lebih atau sama dengan 30.0
	elif bmi >= 30.0:
		kategori = "Obesiti"

	# Tukarkan bmi *float* menjadi string
	bmi = str(bmi)

	# Output
	# Configure/Edit Label output_bmi
	output_bmi.config(text="BMI Anda: " + bmi + "\nDan Anda: " + kategori,  fg='black')

# ==============================================================================================================
# ============================================CLASS=============================================================

# Placeholder effect ## copied
class PlaceholderEntry(ttk.Entry):
	def __init__(self, container, placeholder, *args, **kwargs):
		super().__init__(container, *args, **kwargs)
		self.placeholder = placeholder

		self.field_style = kwargs.pop("style", "TEntry")
		self.placeholder_style = kwargs.pop("placeholder_style", self.field_style)
		self["style"] = self.placeholder_style

		self.insert("0", self.placeholder)
		self.bind("<FocusIn>", self._clear_placeholder)
		self.bind("<FocusOut>", self._add_placeholder)

	def _clear_placeholder(self, e):
		if self["style"] == self.placeholder_style:
			self.delete("0", "end")
			self["style"] = self.field_style

	def _add_placeholder(self, e):
		if not self.get():
			self.insert("0", self.placeholder)
			self["style"] = self.placeholder_style

# =============================================================================================================
# ===========================================TKINTER/WINDOWS===================================================

# Window
window = tk.Tk() # buat window kosong
window.title('Atur Cara Untuk Mengira BMI Anda') # set tajuk window
window.configure(bg='#1a75ff') # tukar backgroud color window
w, h = window.winfo_screenwidth(), window.winfo_screenheight() # mendapatkan ketinggian dan lebar screen
window.geometry("%dx%d+0+0" % (w, h)) # tukar ketinggian dan lebar window sama dengan ketinggian dan lebar screen

# Tajuk
# Frame
frame_tajuk = tk.Frame(window, bg='#99b3ff', bd=5)
frame_tajuk.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# Label
label_tajuk = tk.Label(frame_tajuk, text='KALKULATOR BMI', font=('roboto', 30, 'bold'), bg='white', justify='center')
label_tajuk.place(relwidth=1, relheight=1)

# Oleh
# Frame
frame_oleh = tk.Frame(window, bg='#99b3ff', bd=5)
frame_oleh.place(relx=0.5, rely=0.23, relwidth=0.20, relheight=0.08, anchor='n')
# Label
label_oleh = tk.Label(frame_oleh, text='Oleh: Syabil & Amir', font=('roboto', 14), bg='white', justify='center')
label_oleh.place(relwidth=1, relheight=1)

# Input/Entry User
# Frame
frame_input = tk.Frame(window, bg='#99b3ff', bd=5)
frame_input.place(relx=0.5, rely=0.37, relwidth=0.75, relheight=0.1, anchor='n')
# Ketinggian
input_ketinggian = PlaceholderEntry(frame_input, 'Masukkan Ketinggian Anda (Meter)', font=('roboto', 15), justify='center')
input_ketinggian.place(relwidth=0.4, relheight=1)
# Berat
input_berat = PlaceholderEntry(frame_input, 'Masukkan Berat Anda (KG)', font=('roboto', 15), justify='center')
input_berat.place(relx=0.4, relwidth=0.4, relheight=1)
# Button 'KIRA' untuk mengira input yang diberi
button = tk.Button(frame_input, text="KIRA", font=('roboto', 15, 'bold'), bg='#e6e6e6', command=kira_bmi)
button.place(relx=0.8, relheight=1, relwidth=0.2)
window.bind('<Return>', kira_bmi) # call function kira_bmi apabila menekan enter key

# Output
# Frame
frame_output = tk.Frame(window, bg='#99b3ff', bd=5)
frame_output.place(relx=0.5, rely=0.50, relwidth=0.75, relheight=0.4, anchor='n')
# Label
output_bmi = tk.Label(frame_output, text='OUTPUT', font=('roboto', 28, 'bold'), bg='white', fg='black', justify='center')
output_bmi.place(relwidth=1, relheight=1)

# Jalankan program
window.mainloop()

# ==============================================================================================================