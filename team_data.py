# %%
import pandas as pd
from data import team, crew

additional_risk = 0.48
# %%
team_data = pd.DataFrame(
    {"MEMBERS": [], "NUMBER OF MEMBERS": [], "TOTAL COST": [], "SECURITY COST": []}
)

team_data["MEMBERS"] = team["COMBINATIONS"]
team_data["NUMBER OF MEMBERS"] = team["NUMBER OF MEMBERS"]
# %%
cost_list = []
for i in team_data["MEMBERS"]:
    cost = 0
    for j in i:
        if len(i) == 2:
            risk_multi = 1 + additional_risk
        else:
            risk_multi = 1
        mem_cost = (
            crew.set_index("NAME")["COST"].loc[j]
            * (1 + crew.set_index("NAME")["RISK"].loc[j])
            * risk_multi
        )
        cost = cost + mem_cost
    cost_list.append(cost)
team_data["TOTAL COST"] = pd.Series(cost_list)
team_data["SECURITY COST"] = team_data["TOTAL COST"] * 0.05
# %%
