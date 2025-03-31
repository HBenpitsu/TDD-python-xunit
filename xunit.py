class TestCase:
    pass

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = False
        self.name = name
    def run(self):
        targetMethod = getattr(self, self.name)
        targetMethod()
    def testMethod(self):
        self.wasRun = True

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
