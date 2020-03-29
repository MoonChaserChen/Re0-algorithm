from typing import Dict, List, Tuple

names: List[str] = ["Guido", "Jukka", "Ivan"]
version: Tuple[int, int, int] = (3, 7, 1)
options: Dict[str, bool] = {"centered": False, "capitalize": True}


def get_length(arr: List[str]):
    return len(arr)
