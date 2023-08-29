import json
from typing import List, Dict

import pandas as pd

from lib.bp import BASIC_POINTS


def generate_point_data(df: pd.DataFrame, use_cols: List[str]) -> Dict[str, List[List]]:
    point_data: dict = {}
    for ep in df.eventPoint.unique():
        cdf = df[df["eventPoint"] == ep][use_cols]
        table: list = [
            [
                f"{rec['eventBonus']}%",
                rec["liveBonus"],
                f"{rec['scoreLowerLimit']:,}",
                f"{rec['scoreUpperLimit']:,}",
            ]
            for rec in cdf.to_dict("records")
        ]
        point_data[str(ep)] = table
    return point_data


use_cols: List[str] = [
    "eventBonus", "liveBonus", "scoreLowerLimit", "scoreUpperLimit"
]

for bp in BASIC_POINTS:
    df = pd.read_csv(f"table/event_point_table_bp{bp}.tsv", sep="\t")
    point_data = generate_point_data(df, use_cols)
    with open(f"api/point_data_bp{bp}.json", "w", encoding="utf-8") as file:
        json.dump(point_data, file, ensure_ascii=False)
