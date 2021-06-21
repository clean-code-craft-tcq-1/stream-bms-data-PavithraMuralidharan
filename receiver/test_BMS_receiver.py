import unittest
import bms_stream_formatter
import bms_stream_reporter


class test_bms_receiver(unittest.TestCase):

    def test_bms_param_min_calculator(self):
        bms_param_min = bms_stream_reporter.bms_param_min([10,12,14,15,18])
        self.assertTrue(bms_param_min is not None)
        self.assertTrue(bms_param_min == 10)
        bms_param_min = bms_stream_reporter.bms_param_min([])
        self.assertTrue(bms_param_min == 'Data not available')
        self.assertFalse(bms_param_min == 0.58)

    def test_bms_param_max_calculator(self):
        bms_param_max = bms_stream_reporter.bms_param_max([10,12,14,15,18])
        self.assertTrue(bms_param_max is not None)
        self.assertTrue(bms_param_max == 18)
        bms_param_max = bms_stream_reporter.bms_param_max([])
        self.assertTrue(bms_param_max == 'Data not available')
        self.assertFalse(bms_param_max == 0.15)

    def test_bms_param_moving_avg_calculator(self):
        bms_moving_average = bms_stream_reporter.moving_average_last_5([5,6.5,2,3])
        self.assertTrue(bms_moving_average == 'Data Insufficent')
        self.assertFalse(bms_moving_average == 7.5)
        bms_moving_average = bms_stream_reporter.moving_average_last_5([5, 6.5, 2, 3,8,9.5])
        self.assertTrue(bms_moving_average == 5.8)
        
    def test_bms_statistics_reporting(self):
        self.assertTrue(bms_stream_reporter.displayOutput(bms_stream_formatter.bms_stream_formatting()) == 'Success')


if __name__ == '__main__':
    unittest.main()
