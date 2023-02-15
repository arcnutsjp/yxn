import pyperclip as c

g = input("増やしたい文字 >> ")
x = input("増やす数 >> ")
xa = int(x)

c.copy(g * xa)
