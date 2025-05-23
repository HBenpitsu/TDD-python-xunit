import xunit

class BareSampleClass:
    pass

class TestCaseSample(xunit.TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.log = ""
    def setUp(self):
        self.log += "setUp "
    def testMethod(self):
        self.log += "testMethod "
    def testBrokenMethod(self):
        raise Exception("Broken Method")
    def tearDown(self):
        self.log += "tearDown "

class TestSuiteSample(xunit.TestSuite):
    def __init__(self):
        super().__init__()
        self.log = ""
    def setUp(self):
        self.log += "setUp "
    def tearDown(self):
        self.log += "tearDown "

class SetUpFailureTestCaseSample(xunit.TestCase):
    def setUp(self):
        raise Exception("setUp Failure")
    def testMethod(self):
        pass

class SetUpFailureTestSuiteSample(xunit.TestSuite):
    def setUp(self):
        raise Exception("setUp Failure")

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
    def testSetUpFailure(test):
        setUpFailureTest = SetUpFailureTestCaseSample("testMethod")
        try:
            setUpFailureTest.run()
            raise AssertionError("setUpFailureTest did not raise exception")
        except Exception:
            pass

class TestResultTest(xunit.TestCase):
    def testSummary(self):
        result = xunit.TestResult()
        result.testStarted()
        result.testFailed(Exception("Exception"))
        assert result.summary() == "1 run, 1 failed"
    def testDetailReportsException(self):
        suite = xunit.TestSuite()
        suite.addAllOf(TestCaseSample)
        result = suite.run()
        assert result.summary() in result.detail()
        assert "Traceback" in result.detail()
        assert "Exception: Broken Method" in result.detail() 
    def testDetailReportsNoException(self):
        suite = xunit.TestSuite()
        suite.add(TestCaseSample("testMethod"))
        result = suite.run()
        assert result.summary() in result.detail()
        assert "Traceback" not in result.detail()
        assert "Exception" not in result.detail()
class TestSuiteTest(xunit.TestCase):
    def testRunning(self):
        suite = TestSuiteSample()
        assert suite.log == ""
        suite.run()
        assert suite.log == "setUp tearDown "
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
    def testAddAllTestOfTestCase(self):
        suite = xunit.TestSuite()
        suite.addAllOf(TestCaseSample)
        assert len(suite.tests) == 2
    def testNotTestCaseClassExeption(self):
        try:
            suite.addAllOf(BareSampleClass)
            raise AssertionError("TypeCheck did not work")
        except TypeError:
            pass
    def testNotTestCaseExeption(self):
        try:
            suite.add(BareSampleClass())
            raise AssertionError("TypeCheck did not work")
        except TypeError:
            pass
    def testSetUpFailure(self):
        suite = SetUpFailureTestSuiteSample()
        try:
            suite.run()
            raise AssertionError("setUpFailureTest did not raise exception")
        except Exception:
            pass
    def testAddTestSuite(self):
        child = xunit.TestSuite()
        parent = xunit.TestSuite()
        parent.add(child)
        assert child in parent.tests
    def testRecursiveRun(self):
        testcase = TestCaseSample("testMethod")
        child = xunit.TestSuite()
        child.add(testcase)
        parent = xunit.TestSuite()
        parent.add(child)
        parent.add(testcase)
        result = parent.run()
        assert result.summary() == "2 run, 0 failed"
class PythonSpecificationTest(xunit.TestCase):
    pass

suite = xunit.TestSuite()
suite.addAllOf(TestCaseTest)
suite.addAllOf(TestResultTest)
suite.addAllOf(TestSuiteTest)
suite.addAllOf(PythonSpecificationTest)
result = suite.run()
print(result.detail())