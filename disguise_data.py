# %%
from data import disguise
TIME = 60
# %%
disguise_data = disguise
disguise_data["RISK ADJUSTED COST"] = disguise_data["COST PER MEMBER"] * (1+disguise_data["RISK OF DETECTION"])
disguise_data["TOTAL TIME"] = disguise_data["TIME MULTIPLIER"] * TIME
# %%
