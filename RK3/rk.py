infile = open('in.txt', 'r')
outfile = open('out.txt', 'w')


maxSentence = 0
minSentence = 1000
indexRowBeginningMax = indexInTheRowBeginningMax = 0
indexRowEndMax = indexInTheRowEndMax = 0
indexRowBeginningMin = indexInTheRowBeginningMin = 0
indexRowEndMin = indexInTheRowEndMin = 0
indexRowBeginningCurrent = indexInTheRowBeginningCurrent = 0
indexRowEndCurrent = indexInTheRowEndCurrent = 0
count = i = 0
for line in infile:
    for j in range(len(line)):
        if line[j] == '.':
            if count > maxSentence:
                maxSentence = count
                indexRowBeginningMax = indexRowBeginningCurrent
                indexInTheRowBeginningMax = indexInTheRowBeginningCurrent
                indexRowEndMax = i
                indexInTheRowEndMax = j
            if count < minSentence:
                minSentence = count
                indexRowBeginningMin = indexRowBeginningCurrent
                indexInTheRowBeginningMin = indexInTheRowBeginningCurrent
                indexRowEndMin = i
                indexInTheRowEndMin = j
            if j == len(line)-1:
                indexRowBeginningCurrent = i + 1
                indexInTheRowBeginningCurrent = 0
            else:
                indexRowBeginningCurrent = i
                indexInTheRowBeginningCurrent = j + 1
            count = 0
        elif (line[j] == " " or line[j] == "\n") and line[j-1] != ",":
            count += 1
    i += 1
        
infile.close()

with open('in.txt', 'r') as file:
    i = 0
    stringMax = stringMin = ""
    for line in file:
        if i == indexRowBeginningMax:
            stringMax = stringMax + line[(indexInTheRowBeginningMax+1):].strip('\n')
        if i == indexRowEndMax:
            stringMax = stringMax + line[:(indexInTheRowEndMax+1)]
        if i == indexRowBeginningMin:
            stringMin = stringMin + line[(indexInTheRowBeginningMin+1):].strip('\n')
        if i == indexRowEndMin:
            stringMin = stringMin + line[:(indexInTheRowEndMin+1)]
        i += 1
    outfile.write(stringMin + "\n")
    outfile.write(stringMax + "\n")

with open('in.txt', 'r') as file:
    count = 0
    for line in file:
        j = 0
        while j < len(line):
            if line[j] == '.':
                line = line[:(j+1)] + "(" + str(count) + ")" + line[(j+1):]
                j = j + 2 + len(str(count))
                count = 0
            elif (line[j] == " " or line[j] == "\n") and (line[j-1] != "," or line[j-1] != "-"):
                count += 1
            j += 1
        outfile.write(line)

outfile.close()


