import sys
sys.path.insert(0, 'D:/My Own Work/PYTHON Codes/Casual Coding/Music')
import Music_Notes as music
from winsound import Beep
from time import sleep

Octave0 = music.notes(0)
Octave1 = music.notes(1)

# Notes Frequency, Octave 0
C0  = Octave0[0]
Cs0 = Octave0[1]
D0  = Octave0[2]
Ds0 = Octave0[3]
E0  = Octave0[4]
F0  = Octave0[5]
Fs0 = Octave0[6]
G0  = Octave0[7]
Gs0 = Octave0[8]
A0  = Octave0[9]
As0 = Octave0[10]
B0  = Octave0[11]

# Notes Frequency, Octave 1
C1  = Octave1[0]
Cs1 = Octave1[1]
D1  = Octave1[2]
Ds1 = Octave1[3]
E1  = Octave1[4]
F1  = Octave1[5]
Fs1 = Octave1[6]
G1  = Octave1[7]
Gs1 = Octave1[8]
A1  = Octave1[9]
As1 = Octave1[10]
B1  = Octave1[11]

def part1():
    Beep(A1, 300)
    Beep(G1, 300)
    Beep(Fs1, 700)

    sleep(0.05)

    Beep(Fs1, 300)
    Beep(Fs1, 300)
    Beep(G1, 300)
    Beep(Fs1, 300)
    Beep(E1, 300)
    Beep(D1, 300)
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

def part2():
    
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

def part3():
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

def part4():
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

def part5():
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

def part6():
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

def part7():
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

def part8():
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

def play_song():
    for _ in range(2):
        part1()
    for _ in range(2):
        part2()
    part3()
    for _ in range(2):
        part4()
    part5()
    for _ in range(2):
        part6()
    for _ in range(2):
        part7()
    part8()
    part3()
    part4()
    part5()

def run():
    print("|---------------------------|")
    print("|Album: Jab Harry Met Sejal |")
    print("|Singer: Arijit Singh       |")
    print("|Song: Hawayein             |")
    print("|---------------------------|")
    
    play_song()

if __name__ == '__main__':
    run()
