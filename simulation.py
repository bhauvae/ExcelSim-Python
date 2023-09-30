# %%
import pandas as pd
import itertools
from team_data import team_data
from room_data import room_data,equip_cost
from disguise_data import disguise_data
from exit_data import exit_data
from time_data import total_guard_time, team_time
from weapon_data import weapon_data


# %%
index = itertools.product(team_data["MEMBERS"],room_data["COMBINATIONS"],disguise_data["DISGUISE"],weapon_data["NON-LETHAL WEAPON"],exit_data["EXIT"],[False,True])
sim = pd.DataFrame(data=list(index),columns=["TEAM","ROOMS","DISGUISE","WEAPON","EXIT","EQUIPMENT USED"])

sim["EQUIPMENT REQUIRED"] = pd.merge(sim,room_data[["COMBINATIONS","SECRET ROOM"]],left_on=["ROOMS"],right_on=["COMBINATIONS"],how="left")["SECRET ROOM"]

sim["EQUIPMENT COST"] = sim["EQUIPMENT USED"] * equip_cost

sim["NUMBER OF MEMBERS"] = sim["TEAM"].map(lambda x: len(x))

sim["TIME AVAILABLE"] = sim["DISGUISE"].map(dict(disguise_data[["DISGUISE","TOTAL TIME"]].values))


sim["GUARD TIME"] = pd.merge(sim,total_guard_time.set_index("COMBINATIONS").unstack().to_frame("GUARD TIME"),left_on=["WEAPON","ROOMS"],right_index=True,how='left')["GUARD TIME"] / sim["NUMBER OF MEMBERS"]

sim["ROOM TIME"] = pd.merge(sim,team_time.unstack().to_frame("ROOM TIME"),left_on=["TEAM","ROOMS"],right_index=True,how='left')["ROOM TIME"]


sim["TIME TAKEN"] =  sim["GUARD TIME"] + sim["ROOM TIME"]

sim["QUALIFIED"] = (sim["TIME AVAILABLE"] >= sim["TIME TAKEN"]) & (~(sim["EQUIPMENT USED"] ^ sim["EQUIPMENT REQUIRED"]))

sim["TOTAL LOOT"] = pd.merge(sim,room_data[["COMBINATIONS","TOTAL LOOT"]].set_index("COMBINATIONS"),left_on=["ROOMS"],right_index=True,how='left')["TOTAL LOOT"] * sim["QUALIFIED"]

sim["TEAM COST"] = pd.merge(sim,team_data[["MEMBERS","TOTAL COST"]].set_index("MEMBERS"),left_on=["TEAM"],right_index=True,how='left')["TOTAL COST"]

sim["SECURITY COST"] = pd.merge(sim,team_data[["MEMBERS","SECURITY COST"]].set_index("MEMBERS"),left_on=["TEAM"],right_index=True,how='left')["SECURITY COST"] * (~sim["QUALIFIED"])

sim["DISGUISE COST"] = pd.merge(sim,disguise_data[["DISGUISE","RISK ADJUSTED COST"]].set_index("DISGUISE"),left_on=["DISGUISE"],right_index=True,how='left')["RISK ADJUSTED COST"] * sim["NUMBER OF MEMBERS"]

sim["WEAPON COST"] = pd.merge(sim,weapon_data[["NON-LETHAL WEAPON","RISK ADJUSTED COST"]].set_index("NON-LETHAL WEAPON"),left_on=["WEAPON"],right_index=True,how='left')["RISK ADJUSTED COST"] * sim["NUMBER OF MEMBERS"]

sim["EXIT COST"] = pd.merge(sim,exit_data[["EXIT","RISK ADJUSTED COST"]].set_index("EXIT"),left_on=["EXIT"],right_index=True,how='left')["RISK ADJUSTED COST"] * sim["NUMBER OF MEMBERS"] * sim["TIME TAKEN"]

sim["TOTAL COST"] = sim["TEAM COST"] + sim["SECURITY COST"]+ sim["EQUIPMENT COST"] + sim["DISGUISE COST"] + sim["WEAPON COST"] + sim["EXIT COST"]
# %%

sim["PROFIT"] = sim["TOTAL LOOT"] - sim["TOTAL COST"]

# %%
sim.sort_values(by="PROFIT",ascending=False)
# %%
