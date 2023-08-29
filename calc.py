from typing import List, Tuple
from itertools import product
from lib import event_point as ep

BASIC_POINTS: List[int] = [
    100, 103, 104, 105, 106, 107,
    108, 109, 110, 111, 112, 113,
    114, 115, 117, 117, 118, 119,
    120, 121, 122, 123, 124, 125,
    126, 127, 128, 130
]


def get_score_ranges() -> List[Tuple[int, int]]:
    return [(score, score + 19_999) for score in range(0, 2_500_001, 20_000)]


def main():
    import pandas as pd
    df = pd.read_csv(r"test\data\test_data_bp100.tsv", sep="\t")
    for bp in BASIC_POINTS:
        prod = product(range(11), range(386), get_score_ranges())
        for lb, eb, (lower_limit, upper_limit) in prod:
            pt = ep.calc(
                score=lower_limit,
                event_bonus=eb,
                basic_point=bp,
                live_bonus=lb,
            )
            if lb == 0 and bp == 100:
                c = df[(df["LiveBonus"]==0)&(df["EventBonus"]==ep)&(df["ScoreLowerLimit"]==lower_limit)&(df["EventPoint"]==pt)]
                if not c.empty:
                    raise Exception("Err")
        break


if __name__ == "__main__":
    main()
