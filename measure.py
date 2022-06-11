import time
from typing import Any, Callable, List, Dict

REPEAT_COUNT = 50   # How many times to repeat measurement


def normalize_measuremenent(data: Dict[int, List[int]]) -> Dict[int, float]:
    """
    Function to average elapsed times of given size
    """
    res = {}

    for size, measured in data.items():

        res[size] = sum(measured) / len(measured)

    return res


def measure_sample(testing_funtion: Callable[[Any], Any],
                 generator: Callable[[None], List[Dict[int, Any]]],
                 sample: Any) -> int:
        """
        Function to measure time taken by single sample input
        """
        elapsed = -time.perf_counter_ns()

        for run in range(REPEAT_COUNT):
            testing_funtion(sample)

        elapsed += time.perf_counter_ns()

        return elapsed


def measure_time(testing_funtion: Callable[[Any], Any],
                 generator: Callable[[None], List[Dict[int, Any]]]) -> Dict[int, float]:
    """
    Function to measure time taken by testing_funtion on given inputs by generator
    """
    results = {}

    for _ in range(REPEAT_COUNT):

        for size, sample in generator():

            elapsed = measure_sample(testing_funtion, generator, sample)

            if size not in results:
                results[size] = [elapsed // REPEAT_COUNT]
            else:
                results[size] += [elapsed // REPEAT_COUNT]

    # At this point results contains map {size: [array of elapsed times]}
    return normalize_measuremenent(results)
