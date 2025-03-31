import xunit

class TestCaseTest(xunit.TestCase):
    def setUp(self):
        self.wasRunTest = xunit.WasRun("testMethod")
    def testRunning(self):
        assert self.wasRunTest.log == ""
        self.wasRunTest.run()
        assert self.wasRunTest.log == "setUp testMethod tearDown "
    def testWasSetUp(self):
        assert self.wasRunTest.log == ""
        self.wasRunTest.run()
        assert self.wasRunTest.log == "setUp testMethod tearDown "
    def testWasTearedDown(self):
        assert self.wasRunTest.log == ""
        self.wasRunTest.run()
        assert self.wasRunTest.log == "setUp testMethod tearDown "

TestCaseTest("testRunning").run()
TestCaseTest("testWasSetUp").run()
TestCaseTest("testWasTearedDown").run()