# %%
from data import weapons
# %%
weapon_data = weapons
weapon_data["RISK ADJUSTED COST"] = weapon_data["COST PER MEMBER"] * (1+weapon_data["RISK"])
# %%
