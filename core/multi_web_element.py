class MultiWebElement:
    def __init__(self, locator, description):
        self.locator = locator
        self.description = description

    def count(self):
        return self.locator.count()

    def nth(self, index):
        return self.locator[index]

    def first(self):
        return self.locator[0]

    def last(self):
        return self.locator[self.locator.count()-1]

    def all(self):
        results = []
        max_number = self.count()
        for i in range(max_number):
            results.append(self.nth(i))
        return results