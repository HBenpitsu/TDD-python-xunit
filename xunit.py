class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
    def testStarted(self):
        self.runCount += 1
    def testFailed(self):
        self.failureCount += 1
    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"

class TestSuite:
    def __init__(self):
        self.tests: list[TestSuite] = []
    def add(self, test):
        self.tests.append(test)
    def run(self, result=None):
        testsResult = TestResult() if result is None else result
        for test in self.tests:
            test.run(testsResult)
        return testsResult
            
class TestCase(TestSuite):
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self, result=None):
        targetMethod = getattr(self, self.name)
        result = TestResult() if result is None else result
        self.setUp()
        result.testStarted()
        try:
            targetMethod()
        except:
            result.testFailed()
        self.tearDown()
        return result
    def tearDown(self):
        pass
