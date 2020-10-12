# GUI atur cara untuk mengira BMI (Body Mass Index)
# Kumpulan Syabil & Amir

# Python 3.x Only
# Impory module Tkinter
import tkinter as tk
from tkinter import ttk


# FUNCTIONS
# Function untuk mengira bmi dan mengetahui status sesuatu bmi
def keadaan_bmi():
	# Dapatkan input daripada entry input_ketinggian
	tinggi = input_ketinggian.get()
	# Dapatkan input daripada entry input_berat
	berat = input_berat.get()

	def kira_bmi():
		global tinggi, berat
		# Note - != bermaksud tidak sama dengan
		# Jika input tinggi tidak sama dengan "" dan berat tidak sama dengan ""
		if tinggi != "" and berat != "":
	    	# Proses
			# Tukar string kepada nombor
			berat = float(berat)
			tinggi = float(tinggi)
			# Pengiraan BMI
			bmi = berat / (tinggi * tinggi)
			# Bundarkan bmi kepada 2 tempat perpuluhan
			bmi = round(bmi, 2)

			# Jika bmi kurang daripada 18.5
			if bmi < 18.5:
				status = "Kurang Berat Badan"

			# Jika bmi lebih atau sama dengan 18.5 dan kurang daripada 24.9
			elif bmi >= 18.5 and bmi < 24.9:
				status = "Berat Badan Normal"

			# Jika bmi lebih atau sama dengan 25.0 dan kurang daripada 29.9
			elif bmi >= 25.0 and bmi < 29.9:
				status = "Lebih Berat Badan"

			# Jika bmi lebih atau sama dengan 30.0
			elif bmi >= 30.0:
				status = "Obesiti"

			# Tukarkan bmi *float* menjadi string
			bmi = str(bmi)

			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="BMI Anda: " + bmi + "\nDan Anda: " + status, fg='black')

		# Jika input tinggi tidak sama dengan "" dan berat sama dengan ""
		elif tinggi != "" and berat == "":
			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="ERROR:\nMasukkan Berat Badan Anda!", fg='red')

		# Jika input tinggi sama dengan "" dan berat tidak sama dengan ""
		elif tinggi == "" and berat != "":
			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="ERROR:\nMasukkan Ketinggian Anda!", fg='red')

		# Jika input tinggi sama dengan "" dan berat sama dengan ""
		else:
			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="ERROR:\nMasukkan Ketinggian Dan Berat Badan Anda!", fg='red')

	# Jika tinggi dan berat tidak sama dengan ""
	if tinggi != "" and berat != "":
		# Test input tinggi & berat jika boleh ditukarkan menjadi float 
		try:
			test_tinggi = float(tinggi)
			test_berat = float(berat)

		# Jika try == error
		except:
			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="ERROR:\nMasukkan Ketinggian Dan Berat Badan Anda Dengan Betul (Nombor)!", fg='red')

		# Jika try != error
		else:
			kira_bmi()

	# Jika tinggi tidak sama dengan ""
	elif tinggi != "":
		# Test input tinggi jika boleh ditukarkan menjadi float 
		try:
			test_tinggi = float(tinggi)

		# Jika try == error
		except:
			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="ERROR:\nMasukkan Ketinggian Anda Dengan Betul!", fg='red')

		# Jika try != error
		else:
			kira_bmi()

	# Jika berat tidak sama dengan ""
	elif berat != "":
		# Test input berat jika boleh ditukarkan menjadi float 
		try:
			test_berat = float(berat)

		# Jika try == error
		except:
			# Output
			# Configure/Edit Label output_bmi
			output_bmi.config(text="ERROR:\nMasukkan Berat Badan Anda Dengan Betul!", fg='red')

		# Jika try != error
		else:
			kira_bmi()


# Class
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


# Window
window = tk.Tk() # create empty window
window.title('Atur Cara Untuk Mengira BMI Anda') # create the window title
window.configure(bg='#0040ff') # configure window background color
w, h = window.winfo_screenwidth(), window.winfo_screenheight() # get screen width & height info
window.geometry("%dx%d+0+0" % (w, h)) # set window width & height the same as screen's

# Tajuk
# Frame
frame_tajuk = tk.Frame(window, bg='#99b3ff', bd=5)
frame_tajuk.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# Label
label_tajuk = tk.Label(frame_tajuk, text='KALKULATOR BMI', font=('Arial Bold', 30), bg='white', justify='center')
label_tajuk.place(relwidth=1, relheight=1)

# Input/Entry User
# Frame
frame_input = tk.Frame(window, bg='#99b3ff', bd=5)
frame_input.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')
# Ketinggian
input_ketinggian = PlaceholderEntry(frame_input, 'Masukkan Ketinggian Anda (Meter)', font=40, justify='center')
input_ketinggian.place(relwidth=0.4, relheight=1)
# Berat
input_berat = PlaceholderEntry(frame_input, 'Masukkan Berat Anda (KG)', font=40, justify='center')
input_berat.place(relx=0.4, relwidth=0.4, relheight=1)
# Button 'OK' untuk calculate input yang diberi
button = tk.Button(frame_input, text="OK", font=10, bg='#e6e6e6', command=keadaan_bmi)
button.place(relx=0.8, relheight=1, relwidth=0.2)

# Output
# Frame
frame_output = tk.Frame(window, bg='#99b3ff', bd=5)
frame_output.place(relx=0.5, rely=0.50, relwidth=0.75, relheight=0.4, anchor='n')
# Label
output_bmi = tk.Label(frame_output, text='OUTPUT', font=('Bold', 18), bg='white', fg='black', justify='center')
output_bmi.place(relwidth=1, relheight=1)

# Jalankan program
window.mainloop()