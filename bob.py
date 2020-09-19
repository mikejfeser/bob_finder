'''
s = string of letters
prints "Number of times bob occurs is:" and numBobs
'''

numBobs = 0
iteration = 0

for i in s:
    while iteration < len(s) - 2:
        if s[iteration] == 'b' and s[iteration + 1] == 'o' and s[iteration + 2] == 'b':
            numBobs += 1
        iteration += 1
        
print("Number of times bob occurs is: ", numBobs)
