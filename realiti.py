Clock.bpm = 125

p3 >> play("|=1|",amp=0.3, chop=2)

##d4 >> play('x-o-', sample=2, dur=1, rate=var([8,4,2],[16,1]), amp=0.8, 
  ##         hpf=linvar([100, 1000], 16),
    ##       hpr=linvar([0.1, 0.5], 8)).every(5, 'stutter', 3)
           

p1 >> play("|X2| ")

d1 >> dirt(dur=PSum(var(8,4),2), amp=0.9, oct=5, root=var([0,1]), hpf=var([0,200]))

b1 >> sawbass(dur=PDur(var(2,10),3).offadd(1,2), root=var([0,1]), hpf=var([400,0]), lpr=4, amp=1, oct=var([7,8]))

p2 >> play(" |n2|")

p4 >> play("-V-o", dur=PDur(var(3,5),4), sample=0, amp=1)


           
p5 >> play(" [v][-][v][-][v]", dur=1/2, amp=1)







print(SynthDefs)
