import math


def getAnalogVoltageFromDigitalADC(inDigital):
    return float(inDigital / 32767 * 4.096)

def getPhosphateFromVoltage(inVoltage):
    if True:
        return float( max(0, (inVoltage - 1.65447100313479622535) / -0.00899216300940438272) )

    if True:
        # iter1 -- most accurate
        return float( (1.65447100313479 - inVoltage) / 0.00899216300940438 )
    else:
        if False:
            # iter2
            return float( -111.225051717125991931 * inVoltage + 184.00000000000005640000 )
        else:
            # iter3 -- least accurate
            return float( -93.102452281766200000 * inVoltage + 154.44398907103800000)



def main():
    # phosphate conversion test...
    if False:
        testVals = [1.656, 1.646, 1.629, 1.61, 1.565]

        i = 0

        for i in range(len(testVals)):
            ret = getPhosphateFromVoltage(testVals[i])

            print(f'testVal {testVals[i]} --> phosphate {ret}\n')

    # digital to analog conversion test...
    else:
        testVals = [24009, 26380, 13202, 4823, 4817]

        i = 0

        for i in range(len(testVals)):
            ret = getAnalogVoltageFromDigitalADC(testVals[i])

            print(f'testVal {testVals[i]} --> analog voltage {ret}\n')

    return 0

if __name__ == "__main__":
    main()