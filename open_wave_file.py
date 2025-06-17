import simpleaudio as sa

# this is to test if simple audio library is working or not
wave_obj = sa.WaveObject.from_wave_file("cicadas.wav")
play_obj = wave_obj.play()
print("teste - iniciando")
play_obj.wait_done()
print("teste - acabou")   # since this never runs, it means that there is a bug on simpleaudio library