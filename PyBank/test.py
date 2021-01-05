
# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
#print(marks)

#for item in marks.items():
#    print(item)

# Output: ['English', 'Math', 'Science']
#print(list(sorted(marks.keys())))


a = [[],[],[]]
#print(len(a))
#print(a[0])
 
i = 0
n = 3
while i <= n:
    if a[0] == []:
        a[0].append("KEN")
        a[1].append(0)
        a[2].append(10)
    if i == 1:
        a[0].append("JJ")
        a[1].append(50)
        a[2].append(100)
    i = i + 1

#print(len(a[0]))
for j in range(len(a[0])):
    if a[0][j] == "KEN":
        a[1][j] = int(a[1][j]) + 10
        print(a[1][j])
        a[2][j] = int(a[2][j]) + 10
        print(a[2][j])
#        if a[0][j] == "KEN":
#           a[1][j] = int(a[1][j]) + 10
#           a[2][j] = int(a[2][j]) + 10
   
print(a)
 