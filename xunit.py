class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
    def testStarted(self):
        self.runCount += 1
    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"

class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        targetMethod = getattr(self, self.name)
        result = TestResult()
        self.setUp()
        result.testStarted()
        targetMethod()
        self.tearDown()
        return result
    def tearDown(self):
        pass

