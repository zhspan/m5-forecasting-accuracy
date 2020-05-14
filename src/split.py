

class Split:

    STV_COLS = ["id", "item_id", "dept_id", "cat_id", "store_id", "state_id"]

    def __init__(self, data_input):
        self.data_input = data_input

    def get_range(self, start_day, end_day):
        days = self.get_days_in_range(start_day, end_day)
        return data_input.get_sales_train_validation().loc[:, STV_COLS+days]

    def get_range_empty(self, start_day, end_day):
        days = self.get_days_in_range(start_day, end_day)
        filled = data_input.get_sales_train_validation().loc[:, STV_COLS+days]
        filled[days] = 0
        return filled
        
    def get_days_in_range(self, start_day, end_day):
        days = ["d_{}".format(day) for day in range(start_day, end_day+1)]
        return days
        
