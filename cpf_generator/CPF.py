import re
import random
import deprecation
from packaging import version

global CPF_LENGHT
global BLACKLIST

CPF_LENGHT = 11
BLACKLIST = [
  '00000000000',
  '11111111111',
  '22222222222',
  '33333333333',
  '44444444444',
  '55555555555',
  '66666666666',
  '77777777777',
  '88888888888',
  '99999999999',
]

def __numberToWeightArray(weight, length):
    array = []
    for i in range(length):
        array.append(weight - i)

    return array

def __createChecksum(base, weights):
    aggregator = 0
    for index, digit in enumerate(base):
        aggregator += int(digit) * weights[index]
    
    return aggregator

def __generateChecksum(base, weights):
    numericBase = re.sub("[^0-9]", "", str(base))

    if isinstance(weights, int):
        weightsArray = __numberToWeightArray(weights, len(numericBase))
        return __createChecksum(numericBase, weightsArray)
    elif isinstance(weights, list):
        return __createChecksum(numericBase, weights)
    else:
        raise Exception('Invalid weight type. Should be an Array like or a Number')

def validate(cpf):
    stringCpf = unformat(cpf)

    if (len(stringCpf) < CPF_LENGHT) or (len(stringCpf) > CPF_LENGHT):
        return False
    elif stringCpf in BLACKLIST:
        return False
    else:
        cpfRoot = stringCpf[:(CPF_LENGHT-2)]
        check1 = stringCpf[-2]
        check2 = stringCpf[-1]

        expectedCheck1 = __generateChecksum(cpfRoot, 10) % 11
        if expectedCheck1 < 2:
            expectedCheck1 = 0
        else:
            expectedCheck1 = 11 - expectedCheck1
        expectedCheck2 = __generateChecksum(cpfRoot + str(expectedCheck1), 11) % 11
        if expectedCheck2 < 2:
            expectedCheck2 = 0
        else:
            expectedCheck2 = 11 - expectedCheck2

        if (int(check1) == expectedCheck1) and (int(check2) == expectedCheck2):
            return True
        else:
            return False

def generate():
    baseCpf = ''
    for i in range(CPF_LENGHT - 2):
        baseCpf +=  str(random.randint(0, 9))

    mod1 = __generateChecksum(baseCpf, 10) % 11
    if mod1 < 2:
        check1 = 0
    else:
        check1 = 11 - mod1

    mod2 = __generateChecksum(baseCpf + str(check1), 11) % 11
    if mod2 < 2:
        check2 = 0
    else:
        check2 = 11 - mod2

    return baseCpf + str(check1) + str(check2)

@deprecation.deprecated(deprecated_in="2.1.0", removed_in="3.0.0", details="Use the 'format' function instead")
def formater(cpf):
    return format(cpf)

def format(cpf):
    cpf = str(cpf)

    return '{0}.{1}.{2}-{3}'.format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

def unformat(cpf):
    return re.sub("[^0-9]", "", str(cpf))
