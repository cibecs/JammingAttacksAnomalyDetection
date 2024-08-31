
from TestCaseLauncher import TestCaseLauncher
from Constants import Constants

def main():
    tcl = TestCaseLauncher()
    tcl.basicNormalJammingConcatenatedTest(Constants.PERIODIC_JAMMING)


if __name__ == '__main__':
    main()