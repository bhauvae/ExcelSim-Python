# %%
import pandas as pd
import numpy as np
from data import efficiency
from team_data import team_data
from room_data import room

# %%

eff = efficiency.set_index("CREW")
final_eff = pd.DataFrame(columns=room["ROOM"], index=team_data["MEMBERS"])
for a in room["ROOM"]:
    eff_list = []
    for i in team_data["MEMBERS"]:
        for j in i:
            eff_list.append(eff[a].loc[j])
        final_eff.loc[i,a] = np.mean(eff_list)

# %%
room_time = pd.DataFrame(columns=room["ROOM"], index=team_data["MEMBERS"])
for i in room["ROOM"]:
    for j in team_data["MEMBERS"]:
        room_time[i][j] = final_eff[i][j] * room.set_index("ROOM")["TIME"][i]

# %%
