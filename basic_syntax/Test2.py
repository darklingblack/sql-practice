import unittest
from io import StringIO
import pandas as pd
from Tests_1_file import get_gc_content, get_size_class, process_data, calculate_gc_content_by_size_class

class TestGrangerAnalysisCode(unittest.TestCase):

    def test_get_gc_content_upper_case(self):
        self.assertAlmostEqual(get_gc_content("AGCTATAG"), 37.5)

    def test_get_gc_content_lower_case(self):
        self.assertAlmostEqual(get_gc_content("agctatag"), 37.5)

    def test_get_gc_content_mixed_case(self):
        self.assertAlmostEqual(get_gc_content("AgCtATaG"), 37.5)

    def test_get_gc_content_multiline_string(self):
        self.assertAlmostEqual(get_gc_content("AGCT\nATAG"), 37.5)

    def test_get_gc_content_empty_string(self):
        self.assertEqual(get_gc_content(""), 0)

    def test_get_size_class_extralarge(self):
        self.assertEqual(get_size_class(15), 'extralarge')
        self.assertEqual(get_size_class(20), 'extralarge')

    def test_get_size_class_large(self):
        self.assertEqual(get_size_class(10), 'large')
        self.assertEqual(get_size_class(14.9), 'large')

    def test_get_size_class_medium(self):
        self.assertEqual(get_size_class(8), 'medium')
        self.assertEqual(get_size_class(9.9), 'medium')

    def test_get_size_class_small(self):
        self.assertEqual(get_size_class(7.9), 'small')
        self.assertEqual(get_size_class(0), 'small')

    def test_get_size_class_edgecases(self):
        self.assertEqual(get_size_class(8), 'medium')
        self.assertEqual(get_size_class(10), 'large')
        self.assertEqual(get_size_class(15), 'extralarge')

    def test_get_size_class_invalid_input(self):
        self.assertEqual(get_size_class("invalid"), 'invalid')
        self.assertEqual(get_size_class(None), 'invalid')
        self.assertEqual(get_size_class(""), 'invalid')

    def test_process_data(self):
        test_data = StringIO(
            "id,earlength,dnaseq\n"
            "1,10,AGCTATAG\n"
            "2,15,CGTAGCTA\n"
            "3,8,TTGACATG\n"
        )
        df = pd.read_csv(test_data)
        results_df = process_data(df)
        self.assertEqual(len(results_df), 3)
        self.assertEqual(results_df.iloc[0]['earlength_category'], 'large')
        self.assertAlmostEqual(results_df.iloc[0]['gc_content'], 37.5)

    def test_calculate_gc_content_by_size_class(self):
        test_data = StringIO(
            "id,earlength,dnaseq\n"
            "1,10,AGCTATAG\n"
            "2,15,CGTAGCTA\n"
            "3,8,TTGACATG\n"
        )
        df = pd.read_csv(test_data)
        results_df = process_data(df)
        avg_gc_content_df = calculate_gc_content_by_size_class(results_df)
        self.assertEqual(len(avg_gc_content_df), 3)
        self.assertAlmostEqual(avg_gc_content_df[avg_gc_content_df['earlength_category'] == 'large']['gc_content'].values[0], 37.5)

if __name__ == '__main__':
    unittest.main()
