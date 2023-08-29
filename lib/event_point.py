from typing import Dict


BONUS_DICT: Dict[int, int] = {
    0: 1,
    1: 5,
    2: 10,
    3: 15,
    4: 19,
    5: 23,
    6: 26,
    7: 29,
    8: 31,
    9: 33,
    10: 35,
}


def score_bonus(score: int) -> int:
    """
    Calculate and return the score-based bonus.

    Args:
        score (int): Player's score.

    Returns:
        int: Score-based bonus value.
    """
    return score // 20000


def truncate_to_two_decimal_places(num: float) -> float:
    """
    Truncate a floating-point number to retain only two decimal places.

    Args:
        num (float): Input number.

    Returns:
        float: Number truncated to two decimal places.
    """
    return round(num * 100) / 100.0


def _calculate_event_points(scaled_score: float, basic_point: float, live_bonus_multiplier: int) -> int:
    """
    Compute event points using the scaled score, basic point, and a live bonus multiplier.

    Args:
        scaled_score (float): Score scaled with event bonus.
        basic_point (float): Basic point value for the event.
        live_bonus_multiplier (int): Multiplier based on the live bonus.

    Returns:
        int: Total event points.
    """
    truncated_score: float = truncate_to_two_decimal_places(scaled_score)
    scaled_basic_point: int = int(basic_point / 100)
    val: int = int(truncated_score * scaled_basic_point)
    return val * live_bonus_multiplier


def calc(score: int, event_bonus: int, basic_point: int, live_bonus: int) -> int:
    """
    Calculate total event points based on score, event bonus, basic points, and live bonus.

    Args:
        score (int): Player's score.
        event_bonus (int): Additional bonus percentage for the event.
        basic_point (int): Basic point value for the event.
        live_bonus (int): Live bonus value which acts as a key to fetch the multiplier from BONUS_DICT.

    Returns:
        int: Total event points.
    """
    # print((100 + score_bonus(score)) * ((100 + event_bonus) / 100))
    scaled_score: float = truncate_to_two_decimal_places(
        (100 + score_bonus(score)) * ((100 + event_bonus) / 100)
    )
    # print(scaled_score)

    return _calculate_event_points(
        scaled_score=scaled_score,
        basic_point=basic_point,
        live_bonus_multiplier=BONUS_DICT[live_bonus],
    )
