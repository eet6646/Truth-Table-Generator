
import string
alphabet = string.lowercase + string.uppercase


def toBin(x):
    return bin(x)[2:]


def addPad(x, varNum):
    pad = (varNum - len(x))*'0'
    return pad + x

varNum = int(raw_input("Enter Number of Variables: "))
decMax = 2**varNum

f = open('truthTable.txt', 'w')

f.write(' '.join(alphabet[0:varNum]))
f.write("\n")
f.write('=' * (varNum*2 - 1))
f.write("\n")
for i in xrange(decMax):
    f.write(' '.join(addPad(toBin(i), varNum)))
    f.write("\n")

f.close()
