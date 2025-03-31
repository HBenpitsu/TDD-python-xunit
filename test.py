import xunit

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        wasRunTest = xunit.WasRun("testMethod")
        assert wasRunTest.log == ""
        wasRunTest.run()
        assert wasRunTest.log == "setUp testMethod tearDown "

TestCaseTest("testRunning").run()