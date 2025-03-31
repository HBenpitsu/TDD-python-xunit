class TestCase:
    def __init__(self, name):
        self.name = name

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = False
    def run(self):
        targetMethod = getattr(self, self.name)
        targetMethod()
    def testMethod(self):
        self.wasRun = True

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
