from tkinter import *
from tkinter import messagebox
from math import pi, e, sin, cos, tan, log, log2, log10, factorial

window = Tk()
screenSize = "290x800"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("Calculator")


# function
def about():
    messagebox.showinfo(
        "About",
        "Калькулятор 1.0"
        "\n"
        "© Правая палочка Твикс (ФГБОУ ВО «МАГУ»), 2023."
    )


def clickButton(item):
    global expression
    inputText.set(inputText.get() + (str(item)))


def evalute(item):
    clickButton(item)
    equalButton()


def apply_func(name_func):
    inputText.set(eval(f"{name_func}({inputText.get()})")[2:])


def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])


def clearAll():
    inputText.set("")


def expand():
    if screenSize == "279x500":
        window.geometry("279x555")
    else:
        window.geometry("279x555")


def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "ERROR..."
        inputText.set(result)


# menubar
menubar = Menu(window, bg="black", fg="white")
filemenu = Menu(menubar, tearoff=0, bg="black", fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0, bg="black", fg="white")
helpmenu.add_command(label="About", command=about)
mode_menu = Menu(menubar, tearoff=0, bg="black", fg="white")
mode_menu.add_command(label="Простой", command=lambda: simple())
mode_menu.add_command(label="Расширенный", command=lambda: extend())
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_cascade(label="Режим", menu=mode_menu)

expression = ""
inputText = StringVar()

inputFrame = Frame(
    window,
    width=312,
    height=50,
    bd=0,
    highlightbackground="black",
    highlightcolor="gray",
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
    bg="black",
    bd=0,
    justify=RIGHT,
)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack()

ac = PhotoImage(file=r"images\ac.png")
acimage = ac.subsample(4, 4)
ac = Button(
    mainFrame,
    text="AC",
    fg="black",
    image=acimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clearAll(),
).grid(row=0, column=0, padx=1, pady=1)

clear = PhotoImage(file=r"images\clear.png")
clearimage = clear.subsample(4, 4)
clear = Button(
    mainFrame,
    text="AC",
    fg="black",
    image=clearimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clearButton(),
).grid(row=0, column=1, padx=1, pady=1)

expan_btn = PhotoImage(file=r"images\expan_btn.png")
expan_btnimage = expan_btn.subsample(4, 4)
percentage = Button(
    mainFrame,
    fg="black",
    image=expan_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: expand(),
).grid(row=0, column=2, padx=1, pady=1)

divide = PhotoImage(file=r"images\divide.png")
divideimage = divide.subsample(4, 4)
divide = Button(
    mainFrame,
    text="/",
    fg="white",
    image=divideimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("/"),
).grid(row=0, column=3, padx=1, pady=1)


seven = PhotoImage(file=r"images\seven.png")
sevenimage = seven.subsample(4, 4)
seven = Button(
    mainFrame,
    text="7",
    fg="black",
    image=sevenimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(7),
).grid(row=1, column=0, padx=1, pady=1)

eight = PhotoImage(file=r"images\eight.png")
eightimage = eight.subsample(4, 4)
eight = Button(
    mainFrame,
    text="8",
    fg="black",
    image=eightimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(8),
).grid(row=1, column=1, padx=1, pady=1)

nine = PhotoImage(file=r"images\nine.png")
nineimage = nine.subsample(4, 4)
nine = Button(
    mainFrame,
    text="9",
    fg="black",
    image=nineimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(9),
).grid(row=1, column=2, padx=1, pady=1)

multi = PhotoImage(file=r"images\multi.png")
multiimage = multi.subsample(4, 4)
multiply = Button(
    mainFrame,
    text="*",
    fg="white",
    image=multiimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("*"),
).grid(row=1, column=3, padx=1, pady=1)

four = PhotoImage(file=r"images\four.png")
fourimage = four.subsample(4, 4)
four = Button(
    mainFrame,
    text="4",
    fg="black",
    image=fourimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(4),
).grid(row=2, column=0, padx=1, pady=1)

five = PhotoImage(file=r"images\five.png")
fiveimage = five.subsample(4, 4)
five = Button(
    mainFrame,
    text="5",
    fg="black",
    image=fiveimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(5),
).grid(row=2, column=1, padx=1, pady=1)

six = PhotoImage(file=r"images\six.png")
siximage = six.subsample(4, 4)
six = Button(
    mainFrame,
    text="6",
    fg="black",
    image=siximage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(6),
).grid(row=2, column=2, padx=1, pady=1)

minus = PhotoImage(file=r"images\minus.png")
minusimage = minus.subsample(4, 4)
minus = Button(
    mainFrame,
    text="-",
    fg="white",
    image=minusimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("-"),
).grid(row=2, column=3, padx=1, pady=1)

one = PhotoImage(file=r"images\one.png")
oneimage = one.subsample(4, 4)
one = Button(
    mainFrame,
    text="1",
    fg="black",
    image=oneimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(1),
).grid(row=3, column=0, padx=1, pady=1)

two = PhotoImage(file=r"images\two.png")
twoimage = two.subsample(4, 4)
two = Button(
    mainFrame,
    text="2",
    fg="black",
    image=twoimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(2),
).grid(row=3, column=1, padx=1, pady=1)

three = PhotoImage(file=r"images\three.png")
threeimage = three.subsample(4, 4)
three = Button(
    mainFrame,
    text="3",
    fg="black",
    image=threeimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(3),
).grid(row=3, column=2, padx=1, pady=1)

plus = PhotoImage(file=r"images\plus.png")
plusimage = plus.subsample(4, 4)
plus = Button(
    mainFrame,
    text="+",
    fg="white",
    image=plusimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("+"),
).grid(row=3, column=3, padx=1, pady=1)


zero = PhotoImage(file=r"images\0.png")
zeroimage = zero.subsample(4, 4)
zero = Button(
    mainFrame,
    text="0",
    fg="black",
    image=zeroimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(0),
).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = PhotoImage(file=r"images\point.png")
pointimage = point.subsample(4, 4)
point = Button(
    mainFrame,
    text=".",
    fg="black",
    image=pointimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("."),
).grid(row=4, column=2, padx=1, pady=1)


equal = PhotoImage(file=r"images\equal.png")
equalimage = equal.subsample(4, 4)
equals = Button(
    mainFrame,
    text="=",
    image=equalimage,
    fg="white",
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: equalButton(),
).grid(row=4, column=3, padx=1, pady=1)


sqr_btn = PhotoImage(file = r"images\pow_2_btn.png")
sqr_btnimage = sqr_btn.subsample(4,4)
sqr_btn = Button(
    mainFrame,
    text="X²",
    fg="white",
    image=sqr_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: evalute("**2"),
).grid(row=5, column=0, padx=1, pady=1)

sqrt_btn = PhotoImage(file=r"images\sqrt_btn.png")
sqrt_btnimage = sqrt_btn.subsample(4, 4)
sqrt_btn = Button(
    mainFrame,
    text="√",
    fg="white",
    image=sqrt_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: evalute("**.5"),
).grid(row=5, column=1, padx=1, pady=1)

change_sign = PhotoImage(file=r"images\plus_minus_btn.png")
change_sign_btnimage = change_sign.subsample(4, 4)
change_sign = Button(
    mainFrame,
    text="*-1",
    fg="white",
    image=change_sign_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: evalute("*-1"),
).grid(row=5, column=2, padx=1, pady=1)


sin_btn = PhotoImage(file=r"images\sin_btn.png")
sin_btnimage = sin_btn.subsample(4, 4)
sin_btn = Button(
    mainFrame,
    text="sin",
    fg="black",
    image=sin_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("sin("),
)
sin_btn.grid(row=7, column=0, padx=1, pady=1)

cos_btn = PhotoImage(file=r"images\cos_btn.png")
cos_btnimage = cos_btn.subsample(4, 4)
cos_btn = Button(
    mainFrame,
    text="cos",
    fg="black",
    image=cos_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("cos("),
)
cos_btn.grid(row=7, column=1, padx=1, pady=1)

tan_btn = PhotoImage(file=r"images\tan_btn.png")
tan_btnimage = tan_btn.subsample(4, 4)
tan_btn = Button(
    mainFrame,
    text="tan",
    fg="black",
    image=tan_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("tan("),
)
tan_btn.grid(row=7, column=2, padx=1, pady=1)

log_btn = PhotoImage(file=r"images\log_btn.png")
log_btnimage = log_btn.subsample(4, 4)
log_btn = Button(
    mainFrame,
    text="log",
    fg="black",
    image=log_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("log("),
)
log_btn.grid(row=7, column=3, padx=1, pady=1)


pow_y = PhotoImage(file=r"images\pow_y_btn.png")
pow_y_btnimage = pow_y.subsample(4, 4)
pow_y = Button(
    mainFrame,
    text="x^y",
    fg="white",
    image=pow_y_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("**"),
)
pow_y.grid(row=8, column=0, padx=1, pady=1)

log_btn2 = PhotoImage(file=r"images\log2_btn.png")
log2_btnimage = log_btn2.subsample(4, 4)
btn_log2_ = Button(
    mainFrame,
    text="log2",
    fg="white",
    image=log2_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("log2("),
)
btn_log2_.grid(row=8, column=1, padx=1, pady=1)

log_btn10 = PhotoImage(file=r"images\log10_btn.png")
log10_btnimage = log_btn10.subsample(4, 4)
btn_log10_ = Button(
    mainFrame,
    text="log10",
    fg="white",
    image=log10_btnimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("log10("),
)
btn_log10_.grid(row=8, column=2, padx=1, pady=1)

abs_ = PhotoImage(file=r"images\abs_btn.png")
absimage = abs_.subsample(4, 4)
btn_abs = Button(
    mainFrame,
    text="abs",
    fg="white",
    image=absimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("abs("),
)
btn_abs.grid(row=8, column=3, padx=1, pady=1)

fact_ = PhotoImage(file=r"images\factorial_btn.png")
factimage = fact_.subsample(4, 4)
bnt_fact = Button(
    mainFrame,
    text="X!",
    fg="white",
    image=factimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("factorial("),
)
bnt_fact.grid(row=9, column=0, padx=1, pady=1)

bin_ = PhotoImage(file=r"images\bin_btn.png")
binimage = bin_.subsample(4, 4)
btn_bin = Button(
    mainFrame,
    text="bin",
    fg="white",
    image=binimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: apply_func("bin"),
)
btn_bin.grid(row=9, column=1, padx=1, pady=1)

oct_ = PhotoImage(file=r"images\oct_btn.png")
octimage = oct_.subsample(4, 4)
btn_oct = Button(
    mainFrame,
    text="oct",
    fg="white",
    image=octimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: apply_func("oct"),
)
btn_oct.grid(row=9, column=2, padx=1, pady=1)

hex_ = PhotoImage(file=r"images\hex_btn.png")
heximage = hex_.subsample(4, 4)
btn_hex = Button(
    mainFrame,
    text="hex",
    fg="white",
    image=heximage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: apply_func("hex"),
)
btn_hex.grid(row=9, column=3, padx=1, pady=1)

expan = PhotoImage(file=r"images\expand.png")
expanimage = expan.subsample(4, 4)
expan = Label(window, text="pi", fg="black", image=expanimage, bg="black").pack(
    side=BOTTOM
)
pie = 3.1415
pi = PhotoImage(file=r"images\pi.png")
piimage = pi.subsample(4, 4)
pi = Button(
    mainFrame,
    text="pi",
    fg="black",
    image=piimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(pie),
)
pi.grid(row=10, column=0, padx=1, pady=1)

eie = 2.7182
ee = PhotoImage(file=r"images\eie.png")
eeimage = ee.subsample(4, 4)
ee = Button(
    mainFrame,
    text="у",
    fg="black",
    image=eeimage,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton(eie),
)
ee.grid(row=10, column=1, padx=1, pady=1)

bracket1 = PhotoImage(file=r"images\bracket1.png")
bracket1_image = bracket1.subsample(4, 4)
bracket1 = Button(
    mainFrame,
    text="(",
    fg="black",
    image=bracket1_image,
    bd=0,
    bg="black",
    cursor="hand2",
    command=lambda: clickButton("("),
)
bracket1.grid(row=10, column=2, padx=1, pady=1)

bracket2 = PhotoImage(file=r"images\bracket2.png")
bracket2_image = bracket2.subsample(4, 4)
bracket2 = Button(
    mainFrame,
    text=")",
    fg="black",
    image=bracket2_image,
    bd=0,
    bg="black",
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
    log_btn.grid_forget()
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
    log_btn.grid(row=7, column=3, padx=1, pady=1)
    btn_oct.grid(row=9, column=2, padx=1, pady=1)
    btn_hex.grid(row=9, column=3, padx=1, pady=1)
    pi.grid(row=10, column=0, padx=1, pady=1)
    ee.grid(row=10, column=1, padx=1, pady=1)
    bracket1.grid(row=10, column=2, padx=1, pady=1)
    bracket2.grid(row=10, column=3, padx=1, pady=1)


window.iconbitmap("images\icon.ico")
window.config(bg="black", menu=menubar)
window.mainloop()
