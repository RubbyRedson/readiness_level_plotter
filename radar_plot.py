# Libraries
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import sys


# In order to run the script you need to provide the team name and 6 readiness levels as parameters
team_name = sys.argv[1]
date = datetime.datetime.today().strftime('%Y-%m-%d')

customer_readiness_level = sys.argv[2]
team_readiness_level = sys.argv[3]
business_readiness_level = sys.argv[4]
ipr_readiness_level = sys.argv[5]
funding_readiness_level = sys.argv[6]
technology_readiness_level = sys.argv[7]

# Set data
df = pd.DataFrame({
    'Customer': [customer_readiness_level],
    'Team': [team_readiness_level],
    'Business': [business_readiness_level],
    'IPR': [ipr_readiness_level],
    'Funding': [funding_readiness_level],
    'Technology': [technology_readiness_level]
})

# number of variable
categories = list(df)
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values = df.loc[0].values.flatten().tolist()
values += values[:1]
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='black', size=8)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9], ["1", "2", "3", "4", "5", "6", "7", "8", "9"], color="grey", size=7)
plt.ylim(0, 10)

# Title
plt.title(team_name + " Readiness Level, " + date)

# Plot data
ax.plot(angles, values, linewidth=1, linestyle='solid')

# Fill area
ax.fill(angles, values, 'b', alpha=0.1)
plt.savefig('./readiness_level_'+date+'.png')