import unittest

import polars as pl

from lib.event_point import calc


class TestEventPointCalculation(unittest.TestCase):

    def _load_test_data(self, filename):
        normalized_filename = filename.replace("\\", "/")
        df = pl.read_csv(normalized_filename, separator="\t")
        df = df.filter(pl.col("liveBonus") == 0)
        return df.iter_rows(named=True)

    def test_calc_from_file(self):
        test_data = self._load_test_data(r"test\data\test_data_bp100.tsv")
        for data in test_data:
            event_bonus = data["eventBonus"]
            live_bonus = data["liveBonus"]
            score_lower = data["scoreLowerLimit"]
            score_upper = data["scoreUpperLimit"]
            expected_event_point = int(data["eventPoint"])
            avg_score = (score_upper + score_lower) // 2

            # Test using an average score within the range.
            calculated_event_point = calc(
                avg_score, event_bonus, 100, live_bonus)
            self.assertEqual(calculated_event_point, expected_event_point)


if __name__ == "__main__":
    unittest.main()
