class TestResult:
    def __init__(self):
        self.runCount = 1
        self.failureCount = 0
    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"

class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        targetMethod = getattr(self, self.name)
        self.setUp()
        targetMethod()
        self.tearDown()
        return TestResult()
    def tearDown(self):
        pass

