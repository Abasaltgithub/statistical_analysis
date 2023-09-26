import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data
CTR = [-399842.75, -362561.75, -331441.75, -314125.75, -37207.75, 151070.25,
       -94601.75, -204425.75, 85473.25, -213663.75, -232127.75, -223629.75]
MF = [945390., 1277288., 1160202., 2621650., 1108247., 1929341., 1263342.,
      1134048., 998966., 882972., 722089., 687178.]

# Combine the data into a DataFrame
data = pd.DataFrame({'Category': ['MF'] * len(MF) + ['CTR'] * len(CTR),
                     'Value': MF + CTR})

# Create KDE plots for "MF" and "CTR"
plt.figure(figsize=(10, 6))

sns.kdeplot(data=data[data['Category'] == 'MF'],
            x='Value', label='MF', shade=True)
sns.kdeplot(data=data[data['Category'] == 'CTR'],
            x='Value', label='CTR', shade=True)

# Plot data points along y = 0.25 * 10**-6
y_position = 0.05 * 10**-6

# Plot all data points at the specified y-axis position
mf_data = data[data['Category'] == 'MF']['Value']
ctr_data = data[data['Category'] == 'CTR']['Value']

plt.scatter(mf_data, [y_position] * len(mf_data),
            color='blue', label='MF Data', alpha=0.5)
plt.scatter(ctr_data, [y_position] * len(ctr_data),
            color='orange', label='CTR Data', alpha=0.5)

plt.title('Kernel Density Estimation (KDE)')
plt.xlabel('Relative Fluorescence Unit (RFU)')
plt.ylabel('Density')
plt.legend()
plt.show()
