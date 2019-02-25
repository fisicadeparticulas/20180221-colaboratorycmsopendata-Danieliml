import matplotlib.pyplot as plt
import math

F = open("Sample6.csv","r")

M = []
auxW = 0
auxZ = 0
auxH = 0

L = F.readlines()

for i in range(1,20001):
	L[i] = L[i].split(",")

	M = M +[math.sqrt(2*float(L[i][7])*float(L[i][16])*(math.cosh(float(L[i][8])-float(L[i][17])) - math.cos(float(L[i][9])-float(L[i][18]))))]



for i in range(0,20000):
	if 80.360 < M[i] < 80.4:
		auxW = auxW + 1

	if 91.1855 < M[i] < 91.1897:
		auxZ = auxZ + 1

	if 124.85 < M[i] < 125.33:
		auxH = auxH + 1


print("Datos")

print("W = ", auxW)
print("Z = ", auxZ)
print("H = ", auxH)


print(max(M))
print(min(M))

plt.title('Masa')
plt.hist(M,200)
plt.grid(True)
plt.savefig("MASA.png")
plt.show()
plt.clf()




