import xunit

class TestCaseSample(xunit.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""
    def setUp(self):
        self.log += "setUp "
    def testMethod(self):
        self.log += "testMethod "
    def tearDown(self):
        self.log += "tearDown "
    def testBrokenMethod(self):
        raise Exception("Broken Method")

class TestCaseTest(xunit.TestCase):
    def testRunning(self):
        wasRunTest = TestCaseSample("testMethod")
        assert wasRunTest.log == ""
        wasRunTest.run()
        assert wasRunTest.log == "setUp testMethod tearDown "
    def testResult(test):
        resultTest = TestCaseSample("testMethod")
        result = resultTest.run()
        assert result.summary() == "1 run, 0 failed"
    def testFailedResult(test):
        resultTest = TestCaseSample("testBrokenMethod")
        result = resultTest.run()
        assert result.summary() == "1 run, 1 failed"

class TestResultTest(xunit.TestCase):
    def testSummary(self):
        result = xunit.TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == "1 run, 1 failed"

class TestSuiteTest(xunit.TestCase):
    def testRunning(self):
        suite = TestSuiteSample()
        assert suite.log == ""
        suite.run()
        assert suite.log == "setUp runTests tearDown "
    def testHoldsTests(self):
        suite = xunit.TestSuite()
        testcase1 = TestCaseSample("testMethod")
        testcase2 = TestCaseSample("testMethod")
        suite.add(testcase1)
        suite.add(testcase2)
        assert suite.tests == [testcase1, testcase2]
    def testRunsTests(self):
        suite = xunit.TestSuite()
        testcase1 = TestCaseSample("testMethod")
        testcase2 = TestCaseSample("testBrokenMethod")
        suite.add(testcase1)
        suite.add(testcase2)
        result = suite.run()
        assert result.summary() == "2 run, 1 failed"

tests = [
    TestCaseTest("testRunning").run(),
    TestCaseTest("testResult").run(),
    TestResultTest("testSummary").run(),
    TestCaseTest("testFailedResult").run(),
    TestSuiteTest("testHoldsTests").run(),
    TestSuiteTest("testRunsTests").run(),
    TestSuiteTest("testRunning").run(),
]

for test in tests:
    print(test.summary())