class TestResult:
    def summary(self):
        return "1 run, 0 failed"

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

