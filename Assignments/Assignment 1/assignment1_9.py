sPrincipal = input("Enter the Principal :")
sRate = input("Enter the Rate :")
sTime = input("Enter the Time :")

fPrincipal = float(sPrincipal)
fRate = float(sRate)
fTime = float(sTime)

SI = ((fPrincipal * fRate * fTime) / 100)
print("SI is :", SI)
