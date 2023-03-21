from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log, log2, log10, factorial
import configparser
from translate import Trans

theme_map = {"yagami light": "theme_1", "L": "images", "Ryuk": "theme_2"}
state = ''

def main():
    global screenSize
    global state
    smoll = "290x508"
    window = Tk()

    screenSize = smoll
    window.geometry(screenSize)
    window.resizable(0, 0)
    window.title("Calculator")

    config = configparser.ConfigParser()
    config.read("settings.ini")

    theme = config["settings"]["theme"]

    lang = config["settings"]["lang"]

    t = Trans(lang)
    bg_color = {"yagami light": "grey", "L":"black", "Ryuk": "#66C8FF"}[theme]
    folder_theme = theme_map[theme]

    def change_theme(theme_name):
        global state
        state = inputText.get()
        window.destroy()
        config.set("settings", "theme", theme_name)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)


    def change_lang(lang):
        window.destroy()
        config.set("settings", "lang", lang)
        with open("settings.ini", "w") as configfile:
            config.write(configfile)
    # function
    def about():
        messagebox.showinfo(
            t.about,
            "Калькулятор 1.0"
            "\n"
            "© Правая палочка Твикс (ФГБОУ ВО «МАГУ»), 2023."
        )

    def help_syn():
        messagebox.showinfo(
            t.help_s,
            "Режимы работы.\n\n"
            "Простой: базовые арифметические операции, смена знака, проценты, возведение в квадрат, квадратный корень;\n"
            "Расширенный: функции простого калькулятора, тригонометрические функции, возведение в произвольную степень, логарифмы (натуральный и десятичный), модуль числа, факториал числа, перевод в системы счисления (2, 3, 4, 5, 6, 7, 8)."
        )


    def clickButton(item):
        global expression
        inputText.set(inputText.get() + (str(item)))

    def powuwu():
        inputText.set('(' + inputText.get() + ')' + '**2')
        equalButton()

    def evalute(item):
        clickButton(item)
        equalButton()


    def apply_func(name_func):
        inputText.set(eval(f"{name_func}({inputText.get()})")[2:])


    def apply_percent():
        txt = inputText.get()

        if "+" in txt:
            a, b = txt.split("+")
        if "-" in txt:
            a, b = txt.split("-")
        a, b = float(a), float(b)
        if "+" in txt:
           inputText.set(str(a+ (a*b/100)))
        if "-" in txt:
            inputText.set(str(a- (a*b/100)))


        equalButton()

    def clearButton():
        global expression
        expression = ""
        inputText.set(inputText.get()[0:-1])


    def clearAll():
        inputText.set("")


    def expand():
        global screenSize
        if screenSize == "290x508":
            screenSize = "290x800"
            window.geometry("290x800")
        else:
            screenSize = "290x508"
            window.geometry("290x490")


    def equalButton():
        result = ""
        try:
            result = eval(inputText.get())
            inputText.set(result)
        except:
            result = "ERROR..."
            inputText.set(result)

    def copy(*args):
        global sel
        sel = inputText.get()
        window.clipboard = sel

    def paste(*args):
        global sel
        inputText.set(inputText.get() + sel)

    # menubar
    menubar = Menu(window, bg="white", fg="white")
    filemenu = Menu(menubar, tearoff=0, bg=bg_color, fg="white")
    filemenu.add_command(label=t.copy, command=copy)
    filemenu.add_command(label=t.paste, command=paste)
    filemenu.add_separator()
    filemenu.add_command(label=t.exit, command=window.quit)
    menubar.add_cascade(label=t.calc, menu=filemenu)
    helpmenu = Menu(menubar, tearoff=0, bg=bg_color, fg="white")
    helpmenu.add_command(label=t.about, command=about)
    helpmenu.add_command(label=t.help_s, command=help_syn)
    mode_menu = Menu(menubar, tearoff=0, bg=bg_color, fg="white")
    mode_menu.add_command(label=t.simple, command=lambda: expand())
    mode_menu.add_command(label=t.extend, command=lambda: expand())
    menubar.add_cascade(label=t.help_s, menu=helpmenu)
    menubar.add_cascade(label=t.mode, menu=mode_menu)


    theme_menu = Menu(menubar, tearoff=0, bg=bg_color, fg="white")
    theme_menu.add_command(label=t.light, command=lambda: change_theme("yagami light"))
    theme_menu.add_command(label=t.dark, command=lambda: change_theme("L"))
    theme_menu.add_command(label=t.children, command=lambda: change_theme("Ryuk"))
    menubar.add_cascade(label=t.theme, menu=theme_menu)


    lang_menu = Menu(menubar, tearoff=0, bg=bg_color, fg="white")
    lang_menu.add_command(label="Русский", command=lambda: change_lang("ru"))
    lang_menu.add_command(label="English", command=lambda:  change_lang("eng"))
    menubar.add_cascade(label=t.langauge, menu=lang_menu)

    expression = ""
    inputText = StringVar()
    inputText.set(state)

    inputFrame = Frame(
        window,
        width=312,
        height=50,
        bd=0,
        highlightbackground="black",
        highlightcolor="grey",
        highlightthickness=2,
    )
    inputFrame.pack(side=TOP)
    inputField = Entry(
        inputFrame,
        font=(
            "arial",
            25,
        ),
        textvariable=inputText,
        width=50,
        fg="white",
        bg=bg_color,
        bd=0,
        justify=RIGHT,
    )
    inputField.grid(row=0, column=0)
    inputField.pack(ipady=13)

    mainFrame = Frame(window, width=312, height=272.5, bg=bg_color)
    mainFrame.configure(background=bg_color)
    mainFrame.pack()


    ac = PhotoImage(file=f"{folder_theme}\\ac.png")
    acimage = ac.subsample(4, 4)
    ac = Button(
        mainFrame,
        text="AC",
        fg="black",
        image=acimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clearAll(),
    ).grid(row=0, column=0, padx=1, pady=1)

    clear = PhotoImage(file=f"{folder_theme}\\clear.png")
    clearimage = clear.subsample(4, 4)
    clear = Button(
        mainFrame,
        text="AC",
        fg="black",
        image=clearimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clearButton(),
    ).grid(row=0, column=1, padx=1, pady=1)

    expan_btn = PhotoImage(file=f"{folder_theme}\\expan_btn.png")
    expan_btnimage = expan_btn.subsample(4, 4)
    percentage = Button(
        mainFrame,
        fg="black",
        image=expan_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: expand(),
    ).grid(row=0, column=2, padx=1, pady=1)

    divide = PhotoImage(file=f"{folder_theme}\\divide.png")
    divideimage = divide.subsample(4, 4)
    divide = Button(
        mainFrame,
        text="/",
        fg="white",
        image=divideimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("/"),
    ).grid(row=0, column=3, padx=1, pady=1)


    seven = PhotoImage(file=f"{folder_theme}\\seven.png")
    sevenimage = seven.subsample(4, 4)
    seven = Button(
        mainFrame,
        text="7",
        fg="black",
        image=sevenimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(7),
    ).grid(row=1, column=0, padx=1, pady=1)

    eight = PhotoImage(file=f"{folder_theme}\\eight.png")
    eightimage = eight.subsample(4, 4)
    eight = Button(
        mainFrame,
        text="8",
        fg="black",
        image=eightimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(8),
    ).grid(row=1, column=1, padx=1, pady=1)

    nine = PhotoImage(file=f"{folder_theme}\\nine.png")
    nineimage = nine.subsample(4, 4)
    nine = Button(
        mainFrame,
        text="9",
        fg="black",
        image=nineimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(9),
    ).grid(row=1, column=2, padx=1, pady=1)

    multi = PhotoImage(file=f"{folder_theme}\\multi.png")
    multiimage = multi.subsample(4, 4)
    multiply = Button(
        mainFrame,
        text="*",
        fg="white",
        image=multiimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("*"),
    ).grid(row=1, column=3, padx=1, pady=1)

    four = PhotoImage(file=f"{folder_theme}\\four.png")
    fourimage = four.subsample(4, 4)
    four = Button(
        mainFrame,
        text="4",
        fg="black",
        image=fourimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(4),
    ).grid(row=2, column=0, padx=1, pady=1)

    five = PhotoImage(file=f"{folder_theme}\\five.png")
    fiveimage = five.subsample(4, 4)
    five = Button(
        mainFrame,
        text="5",
        fg="black",
        image=fiveimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(5),
    ).grid(row=2, column=1, padx=1, pady=1)

    six = PhotoImage(file=f"{folder_theme}\\six.png")
    siximage = six.subsample(4, 4)
    six = Button(
        mainFrame,
        text="6",
        fg="black",
        image=siximage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(6),
    ).grid(row=2, column=2, padx=1, pady=1)

    minus = PhotoImage(file=f"{folder_theme}\\minus.png")
    minusimage = minus.subsample(4, 4)
    minus = Button(
        mainFrame,
        text="-",
        fg="white",
        image=minusimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("-"),
    ).grid(row=2, column=3, padx=1, pady=1)

    one = PhotoImage(file=f"{folder_theme}\\one.png")
    oneimage = one.subsample(4, 4)
    one = Button(
        mainFrame,
        text="1",
        fg="black",
        image=oneimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(1),
    ).grid(row=3, column=0, padx=1, pady=1)

    two = PhotoImage(file=f"{folder_theme}\\two.png")
    twoimage = two.subsample(4, 4)
    two = Button(
        mainFrame,
        text="2",
        fg="black",
        image=twoimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(2),
    ).grid(row=3, column=1, padx=1, pady=1)

    three = PhotoImage(file=f"{folder_theme}\\three.png")
    threeimage = three.subsample(4, 4)
    three = Button(
        mainFrame,
        text="3",
        fg="black",
        image=threeimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(3),
    ).grid(row=3, column=2, padx=1, pady=1)

    plus = PhotoImage(file=f"{folder_theme}\\plus.png")
    plusimage = plus.subsample(4, 4)
    plus = Button(
        mainFrame,
        text="+",
        fg="white",
        image=plusimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("+"),
    ).grid(row=3, column=3, padx=1, pady=1)


    zero = PhotoImage(file=f"{folder_theme}\\0.png")
    zeroimage = zero.subsample(4, 4)
    zero = Button(
        mainFrame,
        text="0",
        fg="black",
        image=zeroimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(0),
    ).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

    point = PhotoImage(file=f"{folder_theme}\\point.png")
    pointimage = point.subsample(4, 4)
    point = Button(
        mainFrame,
        text=".",
        fg="black",
        image=pointimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("."),
    ).grid(row=4, column=2, padx=1, pady=1)


    equal = PhotoImage(file=f"{folder_theme}\\equal.png")
    equalimage = equal.subsample(4, 4)
    equals = Button(
        mainFrame,
        text="=",
        image=equalimage,
        fg="white",
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: equalButton(),
    ).grid(row=4, column=3, padx=1, pady=1)


    sqr_btn = PhotoImage(file = f"{folder_theme}\\pow_2_btn.png")
    sqr_btnimage = sqr_btn.subsample(4,4)
    sqr_btn = Button(
        mainFrame,
        text="X²",
        fg="white",
        image=sqr_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: powuwu(),
    ).grid(row=5, column=0, padx=1, pady=1)

    sqrt_btn = PhotoImage(file=f"{folder_theme}\\root_btn.png")
    sqrt_btnimage = sqrt_btn.subsample(4, 4)
    sqrt_btn = Button(
        mainFrame,
        text="√",
        fg="white",
        image=sqrt_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: evalute("**.5"),
    ).grid(row=5, column=1, padx=1, pady=1)

    change_sign = PhotoImage(file=f"{folder_theme}\\plus_minus_btn.png")
    change_sign_btnimage = change_sign.subsample(4, 4)
    change_sign = Button(
        mainFrame,
        text="*-1",
        fg="white",
        image=change_sign_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: evalute("*-1"),
    ).grid(row=5, column=2, padx=1, pady=1)


    # TODO

    per_img = PhotoImage(file=f"{folder_theme}\\procent_btn.png")
    per = per_img.subsample(4, 4)
    change_sign = Button(
        mainFrame,
        text="*%",
        fg="white",
        image=per,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: apply_percent(),
    ).grid(row=5, column=3, padx=1, pady=1)

    sin_btn = PhotoImage(file=f"{folder_theme}\\sin_btn.png")
    sin_btnimage = sin_btn.subsample(4, 4)
    sin_btn = Button(
        mainFrame,
        text="sin",
        fg="black",
        image=sin_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("sin("),
    )
    sin_btn.grid(row=7, column=0, padx=1, pady=1)

    cos_btn = PhotoImage(file=f"{folder_theme}\\cos_btn.png")
    cos_btnimage = cos_btn.subsample(4, 4)
    cos_btn = Button(
        mainFrame,
        text="cos",
        fg="black",
        image=cos_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("cos("),
    )
    cos_btn.grid(row=7, column=1, padx=1, pady=1)

    tan_btn = PhotoImage(file=f"{folder_theme}\\tan_btn.png")
    tan_btnimage = tan_btn.subsample(4, 4)
    tan_btn = Button(
        mainFrame,
        text="tan",
        fg="black",
        image=tan_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("tan("),
    )
    tan_btn.grid(row=7, column=2, padx=1, pady=1)

    # log_btn = PhotoImage(file=f"{folder_theme}\\log_btn.png")
    # log_btnimage = log_btn.subsample(4, 4)
    # log_btn = Button(
    #     mainFrame,
    #     text="log",
    #     fg="black",
    #     image=log_btnimage,
    #     bd=0,
    #     bg=bg_color,
    #     cursor="hand2",
    #     command=lambda: clickButton("log("),
    # )
    # log_btn.grid(row=7, column=3, padx=1, pady=1)


    pow_y = PhotoImage(file=f"{folder_theme}\\pow_y_btn.png")
    pow_y_btnimage = pow_y.subsample(4, 4)
    pow_y = Button(
        mainFrame,
        text="x^y",
        fg="white",
        image=pow_y_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("**"),
    )
    pow_y.grid(row=8, column=0, padx=1, pady=1)

    log_btn2 = PhotoImage(file=f"{folder_theme}\\log2_btn.png")
    log2_btnimage = log_btn2.subsample(4, 4)
    btn_log2_ = Button(
        mainFrame,
        text="log2",
        fg="white",
        image=log2_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("log2("),
    )
    btn_log2_.grid(row=8, column=1, padx=1, pady=1)

    log_btn10 = PhotoImage(file=f"{folder_theme}\\log10_btn.png")
    log10_btnimage = log_btn10.subsample(4, 4)
    btn_log10_ = Button(
        mainFrame,
        text="log10",
        fg="white",
        image=log10_btnimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("log10("),
    )
    btn_log10_.grid(row=8, column=2, padx=1, pady=1)

    abs_ = PhotoImage(file=f"{folder_theme}\\abs_btn.png")
    absimage = abs_.subsample(4, 4)
    btn_abs = Button(
        mainFrame,
        text="abs",
        fg="white",
        image=absimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("abs("),
    )
    btn_abs.grid(row=8, column=3, padx=1, pady=1)

    fact_ = PhotoImage(file=f"{folder_theme}\\factorial_btn.png")
    factimage = fact_.subsample(4, 4)
    bnt_fact = Button(
        mainFrame,
        text="X!",
        fg="white",
        image=factimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("factorial("),
    )
    bnt_fact.grid(row=9, column=0, padx=1, pady=1)

    bin_ = PhotoImage(file=f"{folder_theme}\\bin_btn.png")
    binimage = bin_.subsample(4, 4)
    btn_bin = Button(
        mainFrame,
        text="bin",
        fg="white",
        image=binimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: apply_func("bin"),
    )
    btn_bin.grid(row=9, column=1, padx=1, pady=1)

    oct_ = PhotoImage(file=f"{folder_theme}\\oct_btn.png")
    octimage = oct_.subsample(4, 4)
    btn_oct = Button(
        mainFrame,
        text="oct",
        fg="white",
        image=octimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: apply_func("oct"),
    )
    btn_oct.grid(row=9, column=2, padx=1, pady=1)

    hex_ = PhotoImage(file=f"{folder_theme}\\hex_btn.png")
    heximage = hex_.subsample(4, 4)
    btn_hex = Button(
        mainFrame,
        text="hex",
        fg="white",
        image=heximage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: apply_func("hex"),
    )
    btn_hex.grid(row=9, column=3, padx=1, pady=1)

    # expan = PhotoImage(file=f"{folder_theme}\\expand.png")
    # expanimage = expan.subsample(4, 4)
    # expan = Label(window, text="pi", fg="black", image=expanimage, bg=bg_color).pack(
    #     side=BOTTOM
    # )
    pie = 3.1415
    pi = PhotoImage(file=f"{folder_theme}\\pi.png")
    piimage = pi.subsample(4, 4)
    pi = Button(
        mainFrame,
        text="pi",
        fg="black",
        image=piimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(pie),
    )
    pi.grid(row=10, column=0, padx=1, pady=1)

    eie = 2.7182
    ee = PhotoImage(file=f"{folder_theme}\\eie.png")
    eeimage = ee.subsample(4, 4)
    ee = Button(
        mainFrame,
        text="у",
        fg="black",
        image=eeimage,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(eie),
    )
    ee.grid(row=10, column=1, padx=1, pady=1)

    bracket1 = PhotoImage(file=f"{folder_theme}\\bracket1.png")
    bracket1_image = bracket1.subsample(4, 4)
    bracket1 = Button(
        mainFrame,
        text="(",
        fg="black",
        image=bracket1_image,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton("("),
    )
    bracket1.grid(row=10, column=2, padx=1, pady=1)

    bracket2 = PhotoImage(file=f"{folder_theme}\\bracket2.png")
    bracket2_image = bracket2.subsample(4, 4)
    bracket2 = Button(
        mainFrame,
        text=")",
        fg="black",
        image=bracket2_image,
        bd=0,
        bg=bg_color,
        cursor="hand2",
        command=lambda: clickButton(")"),
    )
    bracket2.grid(row=10, column=3, padx=1, pady=1)


    def simple():
        sin_btn.grid_forget()
        cos_btn.grid_forget()
        tan_btn.grid_forget()
        btn_log10_.grid_forget()
        btn_log2_.grid_forget()
        pow_y.grid_forget()
        bnt_fact.grid_forget()
        btn_bin.grid_forget()
        btn_abs.grid_forget()
        # log_btn.grid_forget()
        btn_oct.grid_forget()
        btn_hex.grid_forget()
        pi.grid_forget()
        ee.grid_forget()
        bracket1.grid_forget()
        bracket2.grid_forget()


    def extend():
        sin_btn.grid(row=7, column=0, padx=1, pady=1)
        cos_btn.grid(row=7, column=1, padx=1, pady=1)
        tan_btn.grid(row=7, column=2, padx=1, pady=1)
        btn_log10_.grid(row=8, column=2, padx=1, pady=1)
        btn_log2_.grid(row=8, column=1, padx=1, pady=1)
        pow_y.grid(row=8, column=0, padx=1, pady=1)
        bnt_fact.grid(row=9, column=0, padx=1, pady=1)
        btn_bin.grid(row=9, column=1, padx=1, pady=1)
        btn_abs.grid(row=8, column=3, padx=1, pady=1)
        # log_btn.grid(row=7, column=3, padx=1, pady=1)
        btn_oct.grid(row=9, column=2, padx=1, pady=1)
        btn_hex.grid(row=9, column=3, padx=1, pady=1)
        pi.grid(row=10, column=0, padx=1, pady=1)
        ee.grid(row=10, column=1, padx=1, pady=1)
        bracket1.grid(row=10, column=2, padx=1, pady=1)
        bracket2.grid(row=10, column=3, padx=1, pady=1)


    window.iconbitmap(f"images\\icon.ico")
    window.config(bg=bg_color, menu=menubar)
    import sys
    window.protocol("WM_DELETE_WINDOW", lambda: sys.exit(1))
    window.mainloop()



while True:
    main()