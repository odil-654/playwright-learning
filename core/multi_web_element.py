class MultiWebElement:
    def __init__(self, locator, description):
        self.locator = locator
        self.description = description

    def count(self):
        return self.locator.count()

    def nth(self, index):
        return WebElement(
            self.locator.nth(index),
            f"{self.description} -> element #{index}",
        )

    def first(self):
        return self.locator.nth(0)

    def last(self):
        return self.locator.nth(self.count() - 1)

    def all(self):
        results = []
        max_number = self.count()
        for i in range(max_number):
            results.append(self.nth(i))
        return results
