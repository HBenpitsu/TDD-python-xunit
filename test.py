import xunit

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        test = xunit.WasRun("testMethod")
        assert test.wasRun == False
        test.run()
        assert test.wasRun == True

TestCaseTest().run()