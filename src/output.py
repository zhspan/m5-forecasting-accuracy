"""
Write submissions
"""

import pandas as pd

class SubmissionWriter:
    
    def __init__(self, submission_directory, reader):
        """
        :param submission_directory: Directory
        :type submission_directory: string
        """
        self.submission_directory

    def write_submission(self, submission, model):
        time_string = self.get_time_string()
        file_name = "{}_{}".format(model.get_pre_string(), time_string);
        submission = self.format_submission(submission)
        submission.to_csv(self.submission_directory+file_name, index=False)

    def format_submission(self, submission):
        sample_submission = self.reader.get_sample_submission()
        sample_submission.iloc[:submission.shape(0), 1:29] = submission.iloc[:, 6:34]
        return sample_submission

    def get_time_string(self):
        current_time = pd.Timestamp.now()
        time_string = "{}{}{}{}{}{}".format(current_time.year, current_time.month,
                current_time.day, current_time.hour, current_time.minute,
                current_time.second)
        return time_string
