import turtle # 3 - Desenhe uma estrela de 5 pontas.

# Cria a janela e a tartaruga 
janela = turtle.Screen() 
tartaruga = turtle.Turtle() 




#posicionando começo da estrela
tartaruga.penup()
tartaruga.forward(200)
tartaruga.right(90)
tartaruga.forward(200)
tartaruga.right(75)

tartaruga.right(45)


tartaruga.forward(150)
tartaruga.left(90)
tartaruga.pendown()
tartaruga.forward(150)
tartaruga.right(144)
tartaruga.forward(150)

tartaruga.left(72)
tartaruga.forward(150)

tartaruga.right(144)
tartaruga.forward(150)
tartaruga.left(72)
tartaruga.forward(150)
tartaruga.right(144)
tartaruga.forward(150)
tartaruga.left(72)
tartaruga.forward(150)
tartaruga.right(144)
tartaruga.forward(150)
tartaruga.left(72)
tartaruga.forward(150)
tartaruga.right(144)
tartaruga.forward(150)

# Mantém a janela aberta até ser fechada.
janela.mainloop() 
