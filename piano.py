import numpy as np
import simpleaudio as sa


def tocar_nota(frequencia, duracao=1, sample_rate=44100):
   t = np.linspace(0, duracao, int(duracao * sample_rate), False)
   nota = np.sin(frequencia * t * 2 * np.pi)
   audio = nota * (2**15 - 1) / np.max(np.abs(nota))
   audio = audio.astype(np.int16)
   sa.play_buffer(audio, 1, 2, sample_rate)
   

teclas = {
    'Z': 220.0,      # La
    'X': 493.88,     # Si
    'C': 261.63,     # Dó
    'V': 293.66,     # Ré
    'B': 329.63,     # Mi
    'N': 349.23,     # Fá
    'M': 392.0       # Sol
}
print("""Selecione alguma das teclas: 
Z para La
X para Si
C para Dó 
V para Ré
B para Mi
N para Fá
M para Sol
E para Sair
""")

rodando = True

while rodando==True: 
   tecla= input('Digite uma tecla: ').upper()

   if tecla == 'E':
      print('sair')
      rodando=False
   
   elif tecla in teclas: 
      frequencia= teclas[tecla]
      print(f'frequencia = {frequencia}Hz')
      tocar_nota(frequencia)
      rodando=True
   
   else:
       print('Tecla invalida. Tente novamente ')






