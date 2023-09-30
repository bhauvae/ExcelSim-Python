# %%
import pandas as pd
from room_data import room_data
from weapon_data import weapon_data
from team_data import team_data
from efficiency_data import room_time

weapon_data = weapon_data.set_index("NON-LETHAL WEAPON")
# %%
total_guard_time = pd.DataFrame({"COMBINATIONS" : room_data["COMBINATIONS"]})

for i in weapon_data.index:
    total_guard_time[i] = (
        room_data["NUMBER OF GUARDS"]
        * weapon_data["TIME PER GUARD"][i]
    )

# %%
team_time = pd.DataFrame(index=room_data["COMBINATIONS"],columns=team_data["MEMBERS"])

for a in team_data["MEMBERS"]:
    for i in room_data["COMBINATIONS"]:
        time_total = 0
        for j in i:
            time_total = time_total + room_time[j][a]
        team_time[a][i] = time_total / len(a)
# %%
