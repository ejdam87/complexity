from measure import measure_time
from analyse import add_plot, show_plot

# --- Sample config ---

# --- Assing function to test ---
from python.sample import maximum, is_palindrome, string_sum         # Python example
from c.c_wrapper import summation                                    # C example
SAMPLE_FUNCTION = is_palindrome
# ---

# --- Assign input generator functions ---
from ingen import generate_integers, generate_strings
SAMPLE_GENERATOR = generate_strings
COMPARE_GENERATOR = generate_integers
# ---

# --- Assign function to compare sample function with ---
from compare_functions import linear, quadratic, cubic, logaritmic
COMPARE_FUNCTION = quadratic
# ---

# ---


data1 = measure_time(SAMPLE_FUNCTION, SAMPLE_GENERATOR)
data2 = measure_time(COMPARE_FUNCTION, COMPARE_GENERATOR)

add_plot(data1, "Tested function")
add_plot(data2, "Compare function")
show_plot()
