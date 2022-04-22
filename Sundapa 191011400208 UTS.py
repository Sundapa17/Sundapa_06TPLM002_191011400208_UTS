lapar = 1
makan = 0
status = "Kelaparan"

makan = float (input())

if (makan==1):
    lapar = 0
    status ="Kenyang"
else :
    lapar = lapar - makan
    status = Lapar + " Kenyang"
print (lapar)