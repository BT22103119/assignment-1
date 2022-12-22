income=int(input("enter your gross income = "))
dependent=int(input("enter number of dependent = "))
#deduction=(income)-(10000)
#dependent deduction = 3000*dependent
taxableincome=int((income)-(10000)-(dependent*3000))
incometax=(0.2)*(taxableincome) 
print("incometax = ",end='')
print(incometax)


