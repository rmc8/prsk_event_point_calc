import json
from typing import List, Dict

import polars as pl

from lib.bp import BASIC_POINTS


def generate_point_data(df: pl.DataFrame, use_cols: List[str]) -> Dict[str, List[List]]:
    point_data: dict = {}
    for ep in df["eventPoint"].unique():
        cdf = df.filter(pl.col("eventPoint") == ep).select(use_cols)
        table: list = [
            [
                f"{row['eventBonus']}%",
                row["liveBonus"],
                f"{row['scoreLowerLimit']:,}",
                f"{row['scoreUpperLimit']:,}",
            ]
            for row in cdf.iter_rows(named=True)
        ]
        point_data[str(ep)] = table
    return point_data


use_cols: List[str] = [
    "eventBonus", "liveBonus", "scoreLowerLimit", "scoreUpperLimit"
]

for bp in BASIC_POINTS:
    df = pl.read_csv(f"table/event_point_table_bp{bp}.tsv", separator="\t")
    point_data = generate_point_data(df, use_cols)
    with open(f"api/point_data_bp{bp}.json", "w", encoding="utf-8") as file:
        json.dump(point_data, file, ensure_ascii=False)
