
class Model:

    def __init__(self):
        pass

    def setup(self, reader):
        self.reader = reader

    def get_pre_string(self):
        return "empty_model"

    def predict(self, prediction):
        return None

    def train(self, train_data):
        pass
