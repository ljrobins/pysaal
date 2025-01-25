"""
Basic Time Operations
=====================
"""

from pysaal.time import Epoch

# %%
# Let's initialize and Epoch object

epoch = Epoch(0.0).from_components(2024, 10, 10, 10, 10, 10.0)

print(epoch)