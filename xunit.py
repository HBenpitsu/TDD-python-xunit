from abc import abstractmethod
import traceback

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0
        self.exceptionBuffer = ""
    def testStarted(self):
        self.runCount += 1
    def testFailed(self, e: Exception):
        self.failureCount += 1
        self.exceptionBuffer += "\n".join(traceback.format_exception(e)) + "\n"
    def summary(self):
        return f"{self.runCount} run, {self.failureCount} failed"
    def detail(self):
        return (
            f"{self.runCount} run, {self.failureCount} failed\n {self.exceptionBuffer}"
        )

class TestCase:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def setUp(self):
        pass
    def run(self, result=None):
        targetMethod = getattr(self, self.name)
        result = TestResult() if result is None else result
        self.setUp()
        result.testStarted()
        try:
            targetMethod()
        except Exception as e:
            result.testFailed(e)
        self.tearDown()
        return result
    @abstractmethod
    def tearDown(self):
        pass

class TestSuite(TestCase):
    def __init__(self):
        self.tests: list[TestSuite] = []
    def add(self, test: TestCase):
        if not isinstance(test, TestCase):
            raise TypeError("test must be an instance of TestCase")
        self.tests.append(test)
    def addAllOf(self, testCaseClass: type[TestCase]):
        if not issubclass(testCaseClass, TestCase):
            raise TypeError("testCaseClass must be a subclass of TestCase")
        methodNames = testCaseClass.__dict__.keys()
        for methodName in methodNames:
            if methodName.startswith("test"):
                self.add(testCaseClass(methodName))
    @abstractmethod
    def setUp(self):
        pass
    def run(self, result: None | TestResult =None):
        self.setUp()
        testsResult = TestResult() if result is None else result
        for test in self.tests:
            test.run(testsResult)
        self.tearDown()
        return testsResult
    @abstractmethod
    def tearDown(self):
        pass