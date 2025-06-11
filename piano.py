print("""selecione alguma das teclas: 
Z para la
X para si
C para do 
V para re
B para mi
N para fa
M para sol""")
 
rodando = True

while rodando:
    QQ = input("digite uma tecla: ")
    print (QQ)
    if QQ[0] == 'E':
        print("Sair")
        exit ()
    elif QQ [0]=='Z':
      print ('Frequencia = 220.0 Hz')
    elif QQ [0]=='X':
       print ('Frequencia = 493.88 Hz')
    elif QQ [0]=='C':
       print ('Frequencia = 261.63 Hz')
    elif QQ [0]=='V':
       print ('Frequencia = 293.66 Hz')
    elif QQ [0]=='B':
       print ('Frequencia = 329.63 Hz')
    elif QQ [0]=='N':
       print ('Frequencia = 349,228 Hz')
    elif QQ [0]=='M':
       print ('Frequencia = 392 Hz')
    else:
       print('tente novamente')
       







