# %%
import pandas as pd
import numpy as np
import itertools
from data import room

equip_cost = 205000 * 1.5  # risk adjusted

secret_room = "U"
room = room
# %%

room["LOOT"] = room["NUMBER OF PAINTINGS"] * room["VALUE PER PAINTING"]
room["TIME"] = room["NUMBER OF PAINTINGS"] * room["TIME PER PAINTING"]
# %%
room_data = pd.DataFrame(
    {
        "COMBINATIONS": [],
        "SECRET ROOM": [],
        "TOTAL LOOT": [],
        "NUMBER OF GUARDS": [],
    }
)
room_data["COMBINATIONS"] = pd.Series(itertools.combinations((room["ROOM"]), 3)).apply(''.join)

# %%
for i in range(len(room_data["COMBINATIONS"])):
    if np.isin(list(room_data.loc[i,"COMBINATIONS"]), secret_room, assume_unique=True).any():
        room_data.loc[i, "SECRET ROOM"] = True

    else:
        room_data.loc[i,"SECRET ROOM"] = False

# %%
loot_list = []
guard_list = []
for i in room_data["COMBINATIONS"]:
    loot = 0
    guard = 0
    for j in i:
        loot = loot + room.set_index("ROOM")["LOOT"][j]
        guard = guard + room.set_index("ROOM")["GUARDS"][j]
    loot_list.append(loot)
    guard_list.append(guard)
room_data["TOTAL LOOT"] = loot_list
room_data["NUMBER OF GUARDS"] = guard_list

# %%
