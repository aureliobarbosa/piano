import numpy as np
import pyaudio


def tocar_nota(frequencia: float, duracao: float = 1.0, sample_rate: int=44100):
    """
    Toca uma nota musical com uma dada frequência e duração usando PyAudio.

    Args:
        frequencia (float): A frequência da nota em Hertz (Hz).
        duracao (float): A duração da nota em segundos.
        sample_rate (int): A taxa de amostragem em samples por segundo (padrão: 44100).
    """
    p = pyaudio.PyAudio()

    sample_number = int(duracao * sample_rate)
    t = np.linspace(0, duracao, sample_number)

    # Gera a onda senoidal (a forma básica de uma nota musical)
    # A amplitude é normalizada para o máximo de um int16 para evitar clipping e garantir volume.
    amplitude = (2**15 - 1)
    nota = amplitude * np.sin(frequencia * t * 2 * np.pi)

    # Converte para 16-bit inteiros (formato necessário para PyAudio)
    audio_data = nota.astype(np.int16).tobytes()

    # Abre um stream de áudio
    stream = p.open(format=pyaudio.paInt16,  # Formato de 16-bit inteiros
                    channels=1,             # Mono
                    rate=sample_rate,       # Taxa de amostragem
                    output=True)            # Modo de saída

    # Escreve os dados de áudio no stream
    stream.write(audio_data)

    # Para e fecha o stream
    stream.stop_stream()
    stream.close()

    # Termina a instância do PyAudio
    p.terminate()


if __name__ == "__main__":
    
    teclas = {
        'Z': 220.0,      # La
        'X': 233.08,     # Si
        'C': 261.63,     # Dó
        'V': 293.66,     # Ré
        'B': 329.63,     # Mi
        'N': 349.23,     # Fá
        'M': 392.0,      # Sol
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

    while rodando:
        tecla = input('Digite uma tecla: ').upper()

        if tecla == 'E':
            print('Saindo do programa...')
            rodando=False
        
        elif tecla in teclas:
            frequencia = teclas[tecla]
            print(f'frequencia = {frequencia}Hz')
            tocar_nota(frequencia)
        else:
            print('Tecla invalida. Tente novamente ')
