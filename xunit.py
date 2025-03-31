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
    def tearDown(self):
        pass

