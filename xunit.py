class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        targetMethod = getattr(self, self.name)
        targetMethod()

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = False
    def setUp(self):
        self.wasSetUp = True
    def testMethod(self):
        self.setUp()
        self.wasRun = True
