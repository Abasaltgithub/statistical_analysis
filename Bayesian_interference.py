import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import theano

# Set Theano to use OpenMP
theano.config.openmp = True

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

plt.title('Kernel Density Estimation (KDE)')
plt.xlabel('Relative Fluorescence Unit (RFU)')
plt.ylabel('Density')
plt.legend()

# Prepare the data
mf_data = np.array(MF)
ctr_data = np.array(CTR)

if __name__ == '__main__':
    # Define Bayesian model
    with pm.Model() as model:
        # Prior distributions for mean and standard deviation
        mf_mean = pm.Normal('mf_mean', mu=1227559.4166666667, sd=100)
        mf_std = pm.HalfNormal('mf_std', sd=100)

        ctr_mean = pm.Normal('ctr_mean', mu=-181423.75, sd=100)
        ctr_std = pm.HalfNormal('ctr_std', sd=100)

        # Likelihood for the data
        mf_obs = pm.Normal('mf_obs', mu=mf_mean, sd=mf_std, observed=mf_data)
        ctr_obs = pm.Normal('ctr_obs', mu=ctr_mean,
                            sd=ctr_std, observed=ctr_data)

    # Perform Bayesian inference with parallel sampling
    with model:
        trace = pm.sample(1000, tune=2000, cores=4)

    # Display summary statistics
    summary = pm.summary(trace)
    print(summary)

    # Create and display trace plots
    pm.traceplot(trace)
    plt.show()
