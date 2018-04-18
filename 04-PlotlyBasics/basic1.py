#######
# This script creates a static matplotlib plot
######
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create fake data:
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.plot()
plt.show()
#######
# At the terminal run:  python basic1.py
# Close the plot window to close the script
######
