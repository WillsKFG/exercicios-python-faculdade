import turtle # 2 - Desenho de um Hexágono.

# Cria a janela e a tartaruga 
janela = turtle.Screen() 
tartaruga = turtle.Turtle() 


tartaruga.forward(50)
tartaruga.left(60)

tartaruga.undo() #Desfaz o último comando.

tartaruga.forward(50)
tartaruga.left(60)
tartaruga.forward(100)
tartaruga.left(60)
tartaruga.forward(100)
tartaruga.left(60)
tartaruga.forward(100)
tartaruga.left(60)
tartaruga.forward(100)
tartaruga.left(60)
tartaruga.forward(100)
tartaruga.left(60)
tartaruga.forward(50)

# Mantém a janela aberta até ser fechada.
janela.mainloop() 
