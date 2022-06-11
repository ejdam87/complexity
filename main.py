from measure import measure_time
from analyse import add_plot, show_plot

# --- Sample config ---

# --- Assing function to test ---
from sample import maximum
SAMPLE_FUNCTION = maximum
# ---

# --- Assign input generator function ---
from ingen import generate_integers
SAMPLE_GENERATOR = generate_integers
# ---

# --- Assign function to compare sample function with ---
from compare_functions import linear, quadratic, cubic
COMPARE_FUNCTION = linear
# ---

# ---


data1 = measure_time(SAMPLE_FUNCTION, SAMPLE_GENERATOR)
data2 = measure_time(COMPARE_FUNCTION, SAMPLE_GENERATOR)

add_plot(data1, "Tested function")
add_plot(data2, "Compare function")
show_plot()
