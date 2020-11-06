import unittest #https://docs.python.org/3/library/unittest.html
from UnitTest_Example import GoogleTestCase

# get test cases
tc1 = unittest.TestLoader().loadTestsFromTestCase(GoogleTestCase)
tc2 = unittest.TestLoader().loadTestsFromTestCase(GoogleTestCase)

# create test suit combining tc1 and tc2
smoke_test = unittest.TestSuite([tc1, tc2])

# trigger test
unittest.TextTestRunner(verbosity=2).run(smoke_test)