from typing import List, Tuple
from itertools import product

import pandas as pd

from lib import event_point as ep
from lib.bp import BASIC_POINTS


def get_score_ranges() -> List[Tuple[int, int]]:
    return [(score, score + 19_999) for score in range(0, 2_820_001, 20_000)]


def main():
    for bp in BASIC_POINTS:
        prod = product(range(11), range(431), get_score_ranges())
        table: list = []
        for lb, eb, (lower_limit, upper_limit) in prod:
            pt = ep.calc(
                score=lower_limit,
                event_bonus=eb,
                basic_point=bp,
                live_bonus=lb,
            )
            rec = {
                "eventBonus": eb,
                "liveBonus": lb,
                "scoreLowerLimit": lower_limit,
                "scoreUpperLimit": upper_limit,
                "eventPoint": pt,
            }
            table.append(rec)
        df = pd.DataFrame(table)
        path = f"table/event_point_table_bp{bp}.tsv"
        df.to_csv(path, sep="\t", index=False)


if __name__ == "__main__":
    main()
