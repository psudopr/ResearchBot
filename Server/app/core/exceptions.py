class CrawlingError(Exception):
    def __init__(self, url: str, message: str):
        self.url = url
        self.message = message
        super().__init__(self.message)

class SummarizationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
