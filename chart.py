# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn styling for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data: customer engagement (avg. session duration in minutes)
np.random.seed(42)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = [f"{h}:00" for h in range(8, 21)]  # business hours: 8AM - 8PM

# Simulate engagement patterns with some realistic variation
data = np.random.normal(loc=10, scale=3, size=(len(hours), len(days)))
for i, hour in enumerate(hours):
    for j, day in enumerate(days):
        if 11 <= int(hour.split(":")[0]) <= 14 and day not in ["Saturday", "Sunday"]:
            data[i, j] += 5  # Lunch peak
        if 17 <= int(hour.split(":")[0]) <= 19 and day in ["Monday", "Tuesday", "Wednesday", "Thursday"]:
            data[i, j] += 3  # After work bump
        if day in ["Saturday", "Sunday"]:
            data[i, j] -= 2  # Weekend dip

data = np.clip(data, 0, None)

# Put data in DataFrame
df = pd.DataFrame(data, index=hours, columns=days)

# Create figure
plt.figure(figsize=(8, 8), dpi=64)

# Heatmap
ax = sns.heatmap(
    df,
    cmap="YlGnBu",
    linewidths=0.5,
    annot=True,
    fmt=".1f",
    cbar_kws={'label': 'Avg. Session Duration (min)'}
)

# Titles and labels
plt.title("Customer Engagement Patterns by Day & Hour", fontsize=16, pad=20)
ax.set_xlabel("Day of Week", fontsize=14)
ax.set_ylabel("Hour of Day", fontsize=14)

# Save as EXACT 512x512 pixels
plt.savefig("chart.png", dpi=64)
plt.close()
