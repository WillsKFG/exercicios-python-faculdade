import turtle # 4 - um quadrado dentro do outro

# Cria a janela e a tartaruga 
janela = turtle.Screen() 
tartaruga = turtle.Turtle() 



tartaruga.forward(150)
tartaruga.left(90)
tartaruga.forward(150)
tartaruga.left(90)
tartaruga.forward(150)
tartaruga.left(90)
tartaruga.forward(150)
tartaruga.left(90)

tartaruga.penup()
tartaruga.left(45)
tartaruga.forward(50)
tartaruga.right(45)
tartaruga.pendown()

tartaruga.forward(75)
tartaruga.left(90)
tartaruga.forward(75)
tartaruga.left(90)
tartaruga.forward(75)
tartaruga.left(90)
tartaruga.forward(75)
tartaruga.left(90)



# Mantém a janela aberta até ser fechada.
janela.mainloop()
