import tkinter as tk


def login_bem_sucedido():
	janela_bem_sucedido = tk.Tk()
	janela_bem_sucedido.title("Login :)")
	janela_bem_sucedido.geometry("200x30")
	janela_bem_sucedido.resizable(0,0)

	txt_bem_sucedido = tk.Label(janela_bem_sucedido, text="Login realizado com sucesso! \n:)")
	txt_bem_sucedido.pack()

def login_mal_sucedido():
	janela_mal_sucedido = tk.Tk()
	janela_mal_sucedido.title("Login :(")
	janela_mal_sucedido.geometry("200x30")
	janela_mal_sucedido.resizable(0,0)

	txt_mal_sucedido = tk.Label(janela_mal_sucedido, text="Login não realizado! \n:(")
	txt_mal_sucedido.pack()

def executa_login():
	user = inp_user.get()
	password = inp_password.get()

	if user == "na18k" and password == "123":
		login_bem_sucedido()
	else:
		login_mal_sucedido()



janela = tk.Tk()
janela.title('Login')
janela.geometry("248x180")
janela.resizable(0, 0)

frm_login = tk.LabelFrame(text="Login")
frm_login.grid(column=0, row=0,padx=10, pady=10)

# --------------------------------------------
txt_user = tk.Label(frm_login, text="User:")
txt_user.grid(column=0, row=0,padx=10, pady=10)

inp_user = tk.Entry(frm_login)
inp_user.grid(column=1, row=0,padx=10, pady=10)

# ---------------------------------------------
txt_password = tk.Label(frm_login, text="Password:")
txt_password.grid(column=0, row=1,padx=10, pady=10)

inp_password = tk.Entry(frm_login)
inp_password.grid(column=1, row=1,padx=10, pady=10)

# ------------------------------------
btn_login = tk.Button(frm_login, text="Login", command=executa_login)
btn_login.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)

# ---------------------------------------------

txt_credit = tk.Label(text="Na18k")
txt_credit.grid(column=0, row=1)

# ______________________________________
janela.mainloop()
