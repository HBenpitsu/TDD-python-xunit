class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        targetMethod = getattr(self, self.name)
        targetMethod()
    def testMethod(self):
        self.wasSetUp = True

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = False
    def testMethod(self):
        self.wasRun = True
