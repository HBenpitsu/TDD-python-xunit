class WasRun:
    def __init__(self, name):
        self.wasRun = False
    def run(self):
        self.testMethod()
    def testMethod(self):
        self.wasRun = True

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
