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

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        wasRunTest = WasRun("testMethod")
        assert wasRunTest.log == ""
        wasRunTest.run()
        assert wasRunTest.log == "setUp testMethod tearDown "

TestCaseTest("testRunning").run()