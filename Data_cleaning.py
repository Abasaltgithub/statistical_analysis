import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data from CTR_30min.xlsx
ctr_data = {
    'None': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'column_1': [4016343, 4084744, 4378978, 4321584, 4501659, 4184058, 4319132, 4181046],
    'column_2': [4053624, 4102060, 4567256, 4211760, 4202522, 4192556, 4938770, 4225795]
}

ctr_df = pd.DataFrame(ctr_data)
negative_ctr_avg = (ctr_df.iloc[6]['column_1'] + ctr_df.iloc[6]['column_2'] +
                    ctr_df.iloc[7]['column_1'] + ctr_df.iloc[7]['column_2']) / 4

# Data from MF_30min.xlsx
mf_data = {
    'None': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'column_1': [4125034, 4339846, 4287891, 4442986, 4178610, 3901733, 3331912, 3133419],
    'column_2': [4456932, 5801294, 5108985, 4313692, 4062616, 3866822, 3157275, 3095970]
}

mf_df = pd.DataFrame(mf_data)
negative_mf_avg = (mf_df.iloc[6]['column_1'] + mf_df.iloc[6]['column_2'] +
                   mf_df.iloc[7]['column_1'] + mf_df.iloc[7]['column_2']) / 4

# Subtract negative_mf_avg from mf_data
mf_df['column_1'] = mf_df['column_1'] - negative_mf_avg
mf_df['column_2'] = mf_df['column_2'] - negative_mf_avg
for key in ctr_data:
    if key != 'None':
        mf_df[key] = mf_df[key][:-2]
mf_df = mf_df.dropna()

# Subtract negative_ctr_avg from ctr_data
ctr_df['column_1'] = ctr_df['column_1'] - negative_ctr_avg
ctr_df['column_2'] = ctr_df['column_2'] - negative_ctr_avg
for key in ctr_data:
    if key != 'None':
        ctr_df[key] = ctr_df[key][:-2]
ctr_df = ctr_df.dropna()


# Print data as a 1D array
mf_data_array = mf_df[['column_1', 'column_2']].values.ravel()
ctr_data_array = ctr_df[['column_1', 'column_2']].values.ravel()


bin = 30
# Specify the same data range for both histograms
data_range = (-1*10**6, 3*10**6)

# Create a combined histogram plot
plt.figure(figsize=(10, 6))
plt.hist(mf_data_array, bins=bin, range=data_range, color='b', alpha=0.7,
         label='MF Data', edgecolor='black', density=True)

mu_mf, std_mf = norm.fit(mf_data_array)
xmin, xmax = plt.xlim()
x = np.linspace(-1 * 10**6, 3*10**6, 100)
p_mf = norm.pdf(x, mu_mf, std_mf)
plt.plot(x, p_mf, 'k', linewidth=2)


plt.hist(ctr_data_array, bins=bin, range=data_range, color='g', alpha=0.7,
         label='CTR Data', edgecolor='black', density=True)
mu_ctr, std_ctr = norm.fit(ctr_data_array)
xmin, xmax = plt.xlim()
p_ctr = norm.pdf(x, mu_ctr, std_ctr)
plt.plot(x, p_ctr, 'k', linewidth=2)

plt.title('MF Data vs. CTR Data Histogram')
plt.xlabel('Relative Fluorescence Unit (RFU) ')
plt.ylabel('Density of Data')
plt.legend()

plt.tight_layout()
plt.show()

# Calculate the PDF functions for MF Data and CTR Data
pdf_mf = norm.pdf(x, mu_mf, std_mf)
pdf_ctr = norm.pdf(x, mu_ctr, std_ctr)

# Print the PDF functions for MF Data and CTR Data
print("PDF for MF Data:")
print(
    f"PDF(x) = (1 / ({std_mf:.4f} * sqrt(2 * pi))) * exp(-(x - {mu_mf:.4f})^2 / (2 * {std_mf**2:.4f}))")

print("\nPDF for CTR Data:")
print(
    f"PDF(x) = (1 / ({std_ctr:.4f} * sqrt(2 * pi))) * exp(-(x - {mu_ctr:.4f})^2 / (2 * {std_ctr**2:.4f}))")


# Print the PDF functions for MF Data and CTR Data
print("PDF for MF Data:")
print("Mean:", mu_mf)
print("Standard Deviation:", std_mf)

print("\nPDF for CTR Data:")
print("Mean:", mu_ctr)
print("Standard Deviation:", std_ctr)
