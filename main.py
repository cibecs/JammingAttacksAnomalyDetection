
from TestCaseLauncher import TestCaseLauncher
from Constants import Constants

def main():
    tcl = TestCaseLauncher()
    tcl.basicNormalJammingConcatenatedTest(Constants.CONSTANT_JAMMING)
    tcl.increasingContaminationTest(Constants.CONSTANT_JAMMING, False)


if __name__ == '__main__':
    main()