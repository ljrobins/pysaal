"""
SGP4-XP Basic Usage
===================
"""

from pysaal.elements import TLE
from pysaal.time import Epoch

# %%
# Let's initialize a TLE object and a propagation epoch

l1 = '1 61429U          24362.90619720 +.00000000  00000 0  55480 0 4 0001'
l2 = '2 61429  88.9747 334.1365 0159713  22.5177  31.9343 14.3545506800001'

tle = TLE().from_lines(l1, l2)

epoch = Epoch(0.0).from_components(2024, 10, 10, 10, 10, 10.0)

# %%
# And propagate it to that epoch

tle_prop = tle.get_state_at_epoch(epoch)

print(f'TLE position: {tle_prop.cartesian_elements.position} [km]')
print(f'TLE velocity: {tle_prop.cartesian_elements.velocity} [km/s]')
