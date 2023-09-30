# %%
from data import exit_method
# %%
exit_data = exit_method
exit_data["RISK ADJUSTED COST"] = exit_data["COST PER MEMBER- MINUTE"] * (1+exit_data["RISK OF INTERCEPTION"])
# %%
