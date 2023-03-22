Clock.bpm = 250
Scale.default = "harmonicMinor"

a = var([0,1,0,2],8)

b1 >> dbass(P[:3]+a, dur=1/2, amp=0.6)

d1 >> play("--- --- ---")

d2 >> play("X - ")

bass_notes = [P[0], P[1], P[0], P[2], P[0], P[1], P[0], P[2]]
b2 >> bass(bass_notes, dur=1/2,sus=1/2, amp=0.8, oct=6)

g1 >> gong([0,1,2,2,1,3], dur=1/2, amp=1)

k1 >> crunch([4,5,8,2], amp=1.5, dur=1/2)

s1 >> razz ([2,2,2,2], amp=1, oct=5)

melody = [0,1,2,2,1,3]

def muda():
    global melody
    random.shuffle(melody)
    b3 >> star(melody, amp=1, dur=PDur(2,4), oct=6)
muda()

