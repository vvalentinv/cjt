class SignUpError(Exception):
    def __init__(self):
        super(SignUpError, self).__init__()
        self.messages = []

    def getMessages(self):
        return self.messages
