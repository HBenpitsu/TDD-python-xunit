import xunit

class TestCaseTest(xunit.TestCase):
    def setUp(self):
        self.wasRunTest = xunit.WasRun("testMethod")
    def testRunning(self):
        assert self.wasRunTest.wasRun == False
        self.wasRunTest.run()
        assert self.wasRunTest.wasRun == True
    def testWasSetUp(self):
        assert self.wasRunTest.wasSetUp == False
        self.wasRunTest.run()
        assert self.wasRunTest.wasSetUp == True

TestCaseTest("testRunning").run()
TestCaseTest("testWasSetUp").run()