import matplotlib.pyplot as plt
from typing import Dict, List, Tuple


def add_plot(measured_data: Dict[int, float], label: str) -> None:
    """
    Function to present measured data and give it it's label
    """
    size = list(measured_data.keys())
    time_taken = list(measured_data.values())

    plt.ylabel("Taken time (ns)")
    plt.xlabel("Size of input (units)")

    plt.plot(size, time_taken, label=label)
    plt.legend()

def show_plot() -> None:
    """
    Function to show all figures
    """
    plt.show()
