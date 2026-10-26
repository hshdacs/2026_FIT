f = 1 / 16
sum = 0.0
for i in range(0, 10_000_000):
    # i hat hierin den Wert 0 bis 9_999_999
    #sum = sum + f # oder als Faulänzer
    sum += f
print(sum)
#print(type(sum))
