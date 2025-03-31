import xunit

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        test = xunit.WasRun("testMethod")
        assert test.wasRun == False
        test.run()
        assert test.wasRun == True
    def testWasSetUp(self):
        test = xunit.WasRun("testMethod")
        test.run()
        assert test.wasSetUp == True

TestCaseTest("testRunning").run()
TestCaseTest("testWasSetUp").run()