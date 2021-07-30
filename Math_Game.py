#game start
gs=""
while gs.lower() != "start":
    gs=input("Type \"START\" to start the math game: ")
    if gs.lower() != "start":
        print(gs)
#questions maker and printer
ot=1
tt=1
for loua in range(1,101):
    q="# question "+str(loua)
    print(q)
    tot=ot*tt
    qfu=input(str(ot)+" x "+str(tt)+" = ")
    print(qfu)
    if qfu == str(tot):
        print("user you are correct")
    else:
        print("user you are wrong, good luck in the next time")
    if ot < 10 :
        ot=ot+1
    else:
        ot=1
        tt=tt+1
print("Thanks for playing this game but the same ended, bye bye")
#trick
while True:
    pass

