from winsound import Beep as make_sound

freq = 400 # Hz
duration = 100 # ms
for _ in range(4):
    make_sound(freq, duration)
