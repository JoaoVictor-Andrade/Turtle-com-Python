# Funções utilizada pela biblioteca turtle no projeto.

# turtle.speed  – um número inteiro no intervalo 0..10 ou uma string de velocidade que aumenta a velocidade do desenho.
#  turtle.forward( distância )  distância – um número (inteiro ou flutuante) Move a caneta para frente pela distância especificada , na direção em que a tartaruga está indo.
# turtle.goto( x , y = Nenhum ) Move a caneta para uma posição absoluta.
# turtle.circle( raio , extensão = Nenhum , passos = Nenhum ) Desenhar um círculo com determinado raio.
#turtle.stamp( ) Carimba uma cópia da forma da caneta na tela na posição atual da tartaruga.
# turtle.penup( ) Puxa a caneta para cima – sem desenho ao se mover.
# turtle.pendown( ) Puxe a caneta para baixo – desenhando ao se mover.
# turtle.pensize( largura = Nenhum ) define a espessura da linha para largura ou retorne-a.
# turtle.color( * argumentos ) altera a cor de peenchimento
#turtle.begin_fill( ) Para ser chamado antes de desenhar uma forma a ser preenchida.
#turtle.end_fill( ) Preenche a forma desenhada após a última chamada para begin_fill().
#turtle.hideturtle( ) fazer a caneta invisivel
# turtle.getshapes( ) Retorna uma lista de nomes de todas as formas de tartaruga disponíveis no momento.
# turtle.turtles( ) Retorna a lista de tartarugas na tela.
#turtle.exitonclick( ) método aos cliques do mouse na Tela.
# turtle.setheading( to_ângulo ) Define a orientação da tartaruga para o ângulo.
# turtle.setposition( x , y = Nenhum ) muda a posição x, e y.
# turtle.left( ângulo ) vira a caneta à esquerda por unidades de ângulo.
# turtle.right( ângulo ) Vira a caneta para a direita por unidades de ângulo.
# turtle.backward( distância ) Mover a caneta para trás pela distância.
# turtle.fillcolor( * argumentos ) Retorna ou define a cor de preenchimento.



# Importação da biblioteca


from turtle import *
from random import *




#Criando a nuvem

def nuvem(x, y, r):
    caneta = Turtle()
    caneta.speed(0)

    caneta.penup()
    caneta.goto(x, y)
    caneta.pendown()
    caneta.color("white")
    caneta.begin_fill()
    caneta.circle(r)
    caneta.end_fill()

    caneta.penup()
    caneta.goto(x + 20, y)
    caneta.pendown()
    caneta.begin_fill()
    caneta.circle(r + 2.5)
    caneta.end_fill()

    caneta.penup()
    caneta.goto(x + 40, y)
    caneta.pendown()
    caneta.begin_fill()
    caneta.circle(r)
    caneta.end_fill()
    caneta.penup()

    caneta.hideturtle()
    chuva(caneta, x, y, 10)


# Criando a chuva

def chuva(caneta, x, y, num):
    caneta.up()
    caneta.color("blue")
    caneta.setpos(x + (num * 3), y + (num / 3))
    caneta.down()
    caneta.pensize(2)
    caneta.setheading(0)
    caneta.right(90)
    caneta.forward(30)
    if num > 0:
        chuva(caneta, x, y, num - 1)



#céu

# seta velocidade do desenho
speed(0)

# seta posicao do cursor
penup()
goto(-750, -100)
pendown()

# desenha um retangulo de B = 1500 e L = 800 (Céu)
color("deepskyblue")
begin_fill()
for i in range(2):
    forward(1500)
    left(90)
    forward(800)
    left(90)
end_fill()

# sol
penup()
goto(-600, 225)
pendown()
color("yellow")
begin_fill()
circle(35)
end_fill()
hideturtle()

# Desenha 2 nuvens
nuvem(0, 210, 25)
nuvem(100, 230, 25)
nuvem(350, 200, 25)
nuvem(550, 180, 25)

x = -200

# grama
bgcolor("DarkGreen")
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
t6 = Turtle()
turtles = [t1, t2, t3, t4, t5,t6]


# Folhas
for t in turtles:
    t.speed(0)
    t.left(90)
    t.color('brown')
    t.pu()
    x += randint(80, 160)
    t.goto(x - 220, randint(-300, -200))
    t.pd()

#Arvores
def branch(turt, branch_len):
    angle = randint(22, 30)
    sf = uniform(0.6, 0.8)
    size = int(branch_len / 10)
    turt.pensize(size)
    if branch_len < 20:
        turt.color('#458B00')
        turt.stamp()
        turt.color('brown')
        turt.hideturtle()

    if branch_len > 10:
        turt.forward(branch_len)
        turt.left(angle)
        branch(turt, branch_len * sf)
        turt.right(angle * 2)
        branch(turt, branch_len * sf)
        turt.left(angle)
        turt.backward(branch_len)


for t in turtles:
    branch(t, 80)



hideturtle()
exitonclick()




