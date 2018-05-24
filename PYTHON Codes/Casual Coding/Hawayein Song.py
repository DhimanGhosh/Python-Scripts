from winsound import Beep
from time import sleep

# Notes Frequency, Octave 0
C0  = 262
Cs0 = 277
D0  = 294
Ds0 = 311
E0  = 330
F0  = 349
Fs0 = 370
G0  = 392
Gs0 = 415
A0  = 440
As0 = 466
B0  = 494

# Notes Frequency, Octave 1
C1  = 523
Cs1 = 554
D1  = 587
Ds1 = 622
E1  = 659
F1  = 699
Fs1 = 740
G1  = 784
Gs1 = 831
A1  = 880
As1 = 932
B1  = 988

print("|---------------------------|")
print("|Album: Jab Harry Met Sejal |")
print("|Singer: Arijit Singh       |")
print("|Song: Hawayein             |")
print("|---------------------------|")


# PART 1
for _ in range(2):
    Beep(A1, 300)
    Beep(G1, 300)
    Beep(Fs1, 700)

    sleep(0.05)

    Beep(Fs1, 300)
    Beep(Fs1, 300)
    Beep(G1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(B0, 700)

    sleep(0.05)

    Beep(B0, 300)
    Beep(B0, 300)
    Beep(D1, 300)
    Beep(E1, 300)
    Beep(Fs1, 300)
    Beep(E1, 700)

    sleep(0.05)

    Beep(Cs1, 300)
    Beep(Cs1, 300)
    Beep(D1, 300)
    Beep(Cs1, 300)
    Beep(B0, 300)
    Beep(A0, 700)

    sleep(0.1)

# PART 2
for _ in range(2):
    Beep(D1, 300)
    Beep(D1, 300)
    Beep(Cs1, 300)
    Beep(B0, 300)
    Beep(A0, 300)
    Beep(B0, 300)
    Beep(B0, 600)
    Beep(D1, 300)
    Beep(B0, 300)
    Beep(B0, 600)
    Beep(D1, 300)
    Beep(B0, 300)
    Beep(B0, 600)
    
    sleep(0.05)
    
    Beep(D1, 300)
    Beep(D1, 300)
    Beep(Cs1, 300)
    Beep(B0, 300)
    Beep(G0, 300)
    Beep(A0, 300)
    Beep(A0, 600)
    Beep(B0, 300)
    Beep(A0, 300)
    Beep(A0, 600)
    Beep(B0, 300)
    Beep(A0, 300)
    Beep(A0, 600)

    sleep(0.1)

# PART 3
Beep(A0, 300)
Beep(A0, 300)
Beep(Cs1, 300)
Beep(E1, 300)
Beep(Fs1, 300)
Beep(E1, 400)
Beep(G1, 400)
Beep(G1, 300)
Beep(Fs1, 300)
Beep(E1, 300)
Beep(D1, 300)
Beep(E1, 300)
Beep(G1, 600)

sleep(0.2)

Beep(Cs1, 200)
Beep(Cs1, 600)
Beep(Cs1, 600)
sleep(0.1)
Beep(D1, 600)
sleep(0.1)
Beep(Cs1, 200)
Beep(B0, 600)
sleep(0.1)
Beep(B0, 200)
Beep(A0, 600)

sleep(0.5)


# PART 4
for _ in range(2):
    Beep(A0, 300)
    sleep(0.1)
    Beep(A1, 400)
    sleep(0.1)
    Beep(G1, 700)
    sleep(0.4)
    Beep(A0, 300)
    sleep(0.1)
    Beep(G1, 400)
    sleep(0.1)
    Beep(Fs1, 700)
    sleep(0.4)
Beep(E1, 200)
sleep(0.1)
Beep(D1, 300)
sleep(0.1)
Beep(E1, 700)
sleep(0.1)
Beep(D1, 200)
sleep(0.1)
Beep(Cs1, 300)
sleep(0.1)
Beep(D1, 700)

sleep(0.7)


# PART 5
for _ in range(2):
    Beep(A0, 300)
    Beep(B0, 300)
    Beep(A0, 300)
    Beep(Gs0, 300)
    Beep(A0, 300)
    Beep(Fs1, 700)

    Beep(Fs1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(G1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(D1, 300)
    Beep(D1, 300)
    Beep(Cs1, 300)
    Beep(Cs1, 300)
    sleep(0.2)
    Beep(D1, 300)
    sleep(0.2)
    Beep(Cs1, 300)
    sleep(0.1)
    Beep(B0, 700)

    Beep(B0, 300)
    Beep(Cs1, 300)
    Beep(B0, 300)
    Beep(As0, 300)
    Beep(B0, 300)
    Beep(G1, 700)

    Beep(G1, 300)
    Beep(G1, 300)
    Beep(Fs1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(E1, 300)
    Beep(D1, 300)
    Beep(D1, 300)
    sleep(0.1)
    Beep(Cs1, 300)
    sleep(0.1)
    Beep(D1, 300)
    sleep(0.1)
    Beep(G1, 300)
    sleep(0.1)
    Beep(Fs1, 700)
    
    sleep(0.4)


# PART 6
for _ in range(2):
    Beep(Fs1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(Fs1, 300)
    Beep(G1, 700)
    sleep(0.1)
    Beep(G1, 300)
    Beep(G1, 300)
    Beep(Fs1, 300)
    Beep(G1, 300)
    Beep(A1, 300)
    Beep(G1, 300)
    Beep(Fs1, 700)
    sleep(0.1)

Beep(Fs1, 300)
Beep(Fs1, 300)
Beep(E1, 300)
Beep(Fs1, 300)
Beep(A1, 300)
Beep(A1, 300)
Beep(G1, 700)

sleep(0.1)

Beep(G1, 300)
Beep(G1, 300)
Beep(Fs1, 300)
Beep(G1, 300)
Beep(A1, 300)
Beep(G1, 300)
Beep(Fs1, 700)

sleep(0.1)

# PART 3 (Repeat)
Beep(A0, 300)
Beep(A0, 300)
Beep(Cs1, 300)
Beep(E1, 300)
Beep(Fs1, 300)
Beep(E1, 400)
Beep(G1, 400)
Beep(G1, 300)
Beep(Fs1, 300)
Beep(E1, 300)
Beep(D1, 300)
Beep(E1, 300)
Beep(G1, 600)

sleep(0.2)

Beep(Cs1, 200)
Beep(Cs1, 600)
Beep(Cs1, 600)
sleep(0.1)
Beep(D1, 600)
sleep(0.1)
Beep(Cs1, 200)
Beep(B0, 600)
sleep(0.1)
Beep(B0, 200)
Beep(A0, 600)

sleep(0.5)

# PART 4 (Repeat)
for _ in range(2):
    Beep(A0, 300)
    sleep(0.1)
    Beep(A1, 400)
    sleep(0.1)
    Beep(G1, 700)
    sleep(0.4)
    Beep(A0, 300)
    sleep(0.1)
    Beep(G1, 400)
    sleep(0.1)
    Beep(Fs1, 700)
    sleep(0.4)
Beep(E1, 200)
sleep(0.1)
Beep(D1, 300)
sleep(0.1)
Beep(E1, 700)
sleep(0.1)
Beep(D1, 200)
sleep(0.1)
Beep(Cs1, 300)
sleep(0.1)
Beep(D1, 700)

sleep(0.7)

