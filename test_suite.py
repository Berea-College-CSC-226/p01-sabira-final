from main import *
import sys

from inspect import getframeinfo, stack


def unittest(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():

    # Test correctness of barcode validation and binary conversion
    b1 = Barcode("UPC-A", "Coke")
    b1.barcode_number = "056820720246"
    b1.barcode_length = len(b1.barcode_number)
    unittest(b1.validate() == True)
    unittest(b1.convert2binary() == "10100011010110001010111101101110010011000110101010100010011011001110010110110010111001010000101")

    # Test correctness of barcode generation
    b2 = Barcode("UPC-A", "Apple")
    bg = BarcodeGenerator(b2)
    bg.generate()
    unittest(b2.validate() == True)


if __name__ == "__main__":
    test_suite()