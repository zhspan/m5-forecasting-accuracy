import data_input
import evaluator

class Framework:
    
    def __init__(self, model):
        self.model = model
        self.reader = data_input.DataInput()
        self.split = split.Split(self.reader)
        self.evaluator = evaluator.Evaluator()
        self.writer = output.Output()

        self.model.setup(self.reader)

    def train(self, train_start_day=1; train_end_day=1885):
        train_data = self.split.get_range(train_start_day, train_end_day)
        self.model.train(train_data)

    def test(self, test_start_day=1886, test_end_day=1913):
        actual = self.split.get_range_empty(test_start_day, test_end_day)
        predicted = self.split.get_range_empty(test_start_day, test_end_day)
        predicted = model.predict(predicted)
        self.evaluator.evaluate(actual, predicted) 

    def predict(self, predict_start_day=1914, predict_end_day=1941):
        prediction = self.split.get_range_empty(train_start_day, train_end_day)
        self.writer.write_submission(prediction, self.model)
