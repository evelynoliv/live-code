Clock.bpm = 130

chords = [(0, 4, 7), (3, 7, 10), (5, 9, 0), (7, 11, 2)]

s1 >> bell(chords, dur=4,lpf=1000, amp=0.5)

s2 >> pads(dur=4, lpf=2000, room=0.5, mix=0.5)

s3 >> pads(chords, dur=4, lpf=2000, room=0.5, mix=0.5)

s4 >> bass(chords, dur=4, lpf=2000, amp=0.5, room=0.6)

d2 >> play("VSVSVS", dur=1/2, amp=0.5)

d3 >> pluck([0,4,7,3,7,10], dur=1/2, slide=linvar([0, 2], 1), slidedelay=0)

melody = [0,4,7,3,7,10,5,9,0,7,11,2]
def sinos():
    global melody
    random.shuffle(melody)
    b3 >> bell(melody, amp=0.5, dur=PDur(1,2), oct=5, slide=linvar([0, 2], 1))
sinos()
