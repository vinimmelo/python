m    from tkinter import *
from selenium import *

"""def decisionTree():
    
    resposta = str(res.get())
    if (resposta=='u' or resposta=='U'):
        urbana()
    elif (resposta=='r' or resposta=='R'):
        rural()
    else:
        lab4=Label(canvas, text="FIM EXE",font=("arial",12, "bold"),bg='light green')
        lab4.place(x=10, y=500)
        decisionTree()
"""



def urbana():
    metros=int(text_m.get())
    arvores=int(text_a.get())
    
    if metros <= 0 or arvores <= 0:
      lab4=Label(canvas, text="digite numeros positivos")
      lab4.place(x=10, y=500)
    else:
        
        ida = ((arvores*7/metros)*100)
        if ida <= 50:
           isa = ((50-ida))
           lab5=Label(canvas, text='Atualmente o indice de sombramento é {:.1f}%'.format(ida), font=("arial",12, "bold"),bg='light green')
           lab5.place(x=10, y=400)
           lab6=Label(canvas, text='O ideal na cidade de Ribeirão Preto é de mais {:.1f}%'.format(isa),font=("arial",12, "bold"),bg='light green')
           lab6.place(x=10, y=500)
           ideal=(arvores*isa)/ida
           lab7=Label(canvas, text="nº ideal é com + árvores {:.0f}".format(ideal),font=("arial",12, "bold"),bg='light green')
           lab7.place(x=10,y=450)
        else:
            lab4=Label(canvas, text="Parabéns Margem requerida acima de 50%",font=("arial",12, "bold"),bg='light green')
            lab4.place(x=10, y=500)
          #  decisionTree()
    return
"""metros = int(text_m.get())
     arvores = int(text_a())
     arv1 = 7.0
     atual = metros/arvores
     correto = ((metros*0.8)-(arvores*arv1))/arv1
     lab5=Label(canvas, text='Atualmente existem uma arvore a cada {0} metros quadrados nessa região...'.format(atual), font=("arial",12, "bold"),bg='light green')
     lab5.place(x=10, y=400)
     lab6=Label(canvas, text='Mas o ideal na cidade de Ribeirão Preto para que se tenha isenção total de tributos é de mais {:.0f} árvores'.format(correto),font=("arial",12, "bold"),bg='light green')
     lab6.place(x=10, y=500)
     ideal=(arvores*isa)/ida
     lab7=Label(canvas, text='http://www.centroeducacionalfsa.org.br/cefsa/calculadora_carbono/index.aspx',font=("arial",12, "bold"),bg='light green')
     lab7.place(x=10,y=450)
     decisionTree()   
"""


def limpar():
    
           #lab5=["text"]=input.get()
           #input.delete(0, END)
           #return
           
           lab5=Label(canvas, text="                                             ", bg='light green',fg='light green',font=("arial",25, "bold"))
           lab5.place(x=10, y=400)
           lab6=Label(canvas, text="                                             ",bg='light green',fg='light green',font=("arial",25, "bold"))
           lab6.place(x=10, y=500)
        
           lab7=Label(canvas, text="                                             ",bg='light green',fg='light green',font=("arial",25, "bold"))
           lab7.place(x=10,y=450)
           lab4=Label(canvas, text="                                             ",bg='light green',fg='light green',font=("arial",25, "bold"))
           lab4.place(x=10, y=500)
window =Tk()
window.title('Densidade arborea')

text_m=StringVar()
text_a=StringVar()
res=StringVar()
                         
canvas=Canvas(window, width=800, height=600)
canvas.configure(background="light green")
canvas.pack()


#bnt2=Button(text='iniciar',font=("arial",8,"bold"),width=5,height=1, command=decisionTree)
#bnt2.place(x=410,y=50)

lab1=Label(canvas, text="Bem vindo ao programa de apoio a decisão para reflorestamento !",font=("arial",12, "bold"),bg='light green')
lab1.place(x=150, y=0)
lab2=Label(canvas, text="Quantos metros quadrados quer verificar:",font=("arial",8,"bold"),bg='light green')
lab2.place(x=0,y=200)
lab3=Label(canvas, text="Quantas árvores existem nessa região?",font=("arial",8,"bold"),bg='light green')
lab3.place(x=0,y=220)


my_image = PhotoImage(file='C:\\ArvoresIDA.png')
canvas.create_image(450, 150, anchor = NW, image=my_image)

#labint=Label(canvas, text="Faça sua escolha entre rural e urbano",font=("arial",8,"bold"),bg='light green')
#resposta= Entry(canvas,font=('arial', 8,'bold'),textvariable=res)
#resposta.place(x=300,y=50)              
escolhaM= Entry(canvas,font=('arial', 8,'bold'),textvariable=text_m)
escolhaM.place(x=225, y=200)

escolhaA = Entry(canvas,font=('arial', 8,'bold'),textvariable=text_a)
escolhaA.place(x=225, y=220)

btn=Button(text='verificar',font=("arial",8,"bold"),width=6,height=2, command =urbana)
btn.place(x=350,y=200)

btn1=Button(text='limpar',font=("arial",8,"bold"), width=4,height=2,command=limpar)
btn1.place(x=405,y=200)

            


