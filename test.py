import xunit

class WasRun(xunit.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""
    def setUp(self):
        self.log += "setUp "
    def testMethod(self):
        self.log += "testMethod "
    def tearDown(self):
        self.log += "tearDown "

class HaveResult(xunit.TestCase):
    def __init__(self, name):
        super().__init__(name)
    def testMethod(self):
        pass
    def testBrokenMethod(self):
        raise Exception("Broken Method")

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        wasRunTest = WasRun("testMethod")
        assert wasRunTest.log == ""
        wasRunTest.run()
        assert wasRunTest.log == "setUp testMethod tearDown "
    def testResult(test):
        resultTest = HaveResult("testMethod")
        result = resultTest.run()
        assert result.summary() == "1 run, 0 failed"
    def testFailedResult(test):
        resultTest = HaveResult("testBrokenMethod")
        result = resultTest.run()
        assert result.summary() == "1 run, 1 failed"

TestCaseTest("testRunning").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResult").run()