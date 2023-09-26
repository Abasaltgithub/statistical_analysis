import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
MF = [-399842.75, -362561.75, -331441.75, -314125.75, -37207.75, 151070.25,
      -94601.75, -204425.75, 85473.25, -213663.75, -232127.75, -223629.75]
CTR = [945390., 1277288., 1160202., 2621650., 1108247., 1929341., 1263342.,
       1134048., 998966., 882972., 722089., 687178.]

# Combine the data into a DataFrame
data = pd.DataFrame({'Category': ['MF'] * len(MF) + ['CTR'] * len(CTR),
                     'Value': MF + CTR})

# Create the violin plot with both "MF" and "CTR" in one line
plt.figure(figsize=(8, 6))

ax = sns.violinplot(x='Category', y='Value', data=data, inner=None)
sns.stripplot(x='Category', y='Value', data=data, color='black',
              jitter=True, size=6)  # Add data points

plt.title('Overlapping Violin Plot of MF and CTR Data')
plt.xlabel('Category')  # Label the x-axis
plt.ylabel('Value')  # Label the y-axis
plt.show()
