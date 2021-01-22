inputfile1 = open('in1.txt')
inputfile2 = open('in2.txt')

outputfile = open('out.txt', 'w')

line1 = inputfile1.readline()
line2 = inputfile2.readline()

while line1 != "" and line2 != "":
    if int(line1) <= int(line2):
        if line1[len(line1)-1] != '\n':
            line1 += '\n'
        outputfile.write(line1)
        line1 = inputfile1.readline()
    else:
        if line2[len(line2)-1] != '\n':
            line2 += '\n'
        outputfile.write(line2)
        line2 = inputfile2.readline()

while line1 != "":
    outputfile.write(line1)
    line1 = inputfile1.readline()
while line2 != "":
    outputfile.write(line2)
    line2 = inputfile2.readline()

inputfile1.close()
inputfile2.close()
outputfile.close()


# Римские числа
inputfile = open('out.txt')
outputfile = open('out1.txt', 'w')

max = 0

for line in inputfile:
    line = line.strip('\n')
    number = int(line)
    res = ''

    count1000 = number // 1000
    res = res + 'M' * count1000
    number = number - 1000 * count1000

    count500 = number // 500
    res = res + 'D' * count500
    number = number - 500 * count500

    count100 = number // 100
    if count100 == 4:
        res = res + 'CD'
    else:
        res = res + 'C' * count100
    number = number - 100 * count100

    count50 = number // 50
    res = res + 'L' * count50
    number = number - 50 * count50

    if number == 19:
        res += 'XIX'
    else:
        count10 = number // 10
        if count10 == 4:
            res = res + 'XL'
        else:
            res = res + 'X' * count10
        number = number - 10 * count10

        count5 = number // 5
        res = res + 'V' * count5
        number = number - 5 * count5

        count1 = number
        if count1 == 4:
            res = res + 'IV'
        else:
            res = res + 'I' * count1
        number = number - 10 * count1

    if len(res) > max:
        max = len(res)
        
inputfile.close()


inputfile = open('out.txt')
for line in inputfile:
    line = line.strip('\n')
    number = int(line)
    res = ''

    count1000 = number // 1000
    res = res + 'M' * count1000
    number = number - 1000 * count1000

    count500 = number // 500
    res = res + 'D' * count500
    number = number - 500 * count500

    count100 = number // 100
    if count100 == 4:
        res = res + 'CD'
    else:
        res = res + 'C' * count100
    number = number - 100 * count100

    count50 = number // 50
    res = res + 'L' * count50
    number = number - 50 * count50

    if number == 19:
        res += 'XIX'
    else:
        count10 = number // 10
        if count10 == 4:
            res = res + 'XL'
        else:
            res = res + 'X' * count10
        number = number - 10 * count10

        count5 = number // 5
        res = res + 'V' * count5
        number = number - 5 * count5

        count1 = number
        if count1 == 4:
            res = res + 'IV'
        else:
            res = res + 'I' * count1
        number = number - 10 * count1

    blank = max - len(res)
    outputfile.write( (blank//2)*" " + res + (blank - (blank//2)) * " " + '\n')

inputfile.close()
outputfile.close()

