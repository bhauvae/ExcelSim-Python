# %%
import pandas as pd
from simulation import sim

if __name__ == "__main__":
  solution = pd.DataFrame(sim[["TEAM","ROOMS","DISGUISE","WEAPON","EXIT","EQUIPMENT USED","PROFIT"]])
  top = solution.sort_values(by="PROFIT",ascending=False).head()
# %%
