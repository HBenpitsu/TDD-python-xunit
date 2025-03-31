class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        targetMethod = getattr(self, self.name)
        self.setUp()
        targetMethod()

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = False
        self.wasSetUp = False
    def setUp(self):
        self.wasSetUp = True
    def testMethod(self):
        self.wasRun = True
