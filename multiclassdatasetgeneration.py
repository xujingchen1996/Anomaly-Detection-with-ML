# -*- coding: utf-8 -*-
"""MultiClassDataSetGeneration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X_mfgSUst_rfIP6vzw6k96ssZG4_ha5v

# Generation of Data Sets
"""

import numpy as np

#Each features distribution and creation
f1 = np.random.normal(1, 0.2, 50000)
f2 = np.random.normal(20, 1, 50000)
f3 = np.random.random(50000)
f4 = np.random.normal(50, 30, 50000)
f5 = np.random.normal(2, 0.15, 50000)
f6 = np.random.exponential(2, 50000)
f7 = np.random.normal(0.04, 0.006, 50000)
f8 = np.random.normal(4, 0.03, 50000)
f9 = np.random.normal(15, 7, 50000)
f10 = np.random.normal(56, 12.5, 50000)
f11 = np.random.beta(5, 4, 50000)
f12 = np.random.beta(10, 2, 50000)
f13 = np.random.normal(-4, 0.05, 50000)
f14 = np.random.random(50000)
f15 = np.random.normal(45, 23, 50000)
f16 = np.random.normal(89, 14, 50000)
f17 = np.random.random(50000)
f18 = np.random.normal(150, 34, 50000)
f19 = np.random.normal(2, 0.5, 50000)
f20 = np.random.exponential(10, 50000)

#appending numpy arrays to overall features array
all = []

#loop through global variables appending arrays of features
for i in range(20):
  all.append(globals()[f"f{i+1}"])

#Transposing so each column is now a feature 
all = np.array(all)
features = all.transpose()

#label creation
labels = [0 for i in range(len(features))]

len(features)

len(labels)

"""### FDIA Function"""

#False Data Injection Function
def inject(features, mean, std):
  #labels initialization
  labels = []
  #iterating through all features
  for row in features:
    #random chance to inject or leave
    if np.random.random() > 0.5:
      #how many sensors to attack
      sensors_to_attack = np.random.randint(6, 14)
      #what indices to attack
      indices = np.random.choice(range(20), sensors_to_attack, replace=False)
      #what values to inject into indices
      values_to_inject = np.random.normal(mean, std, sensors_to_attack)
      #negating values from indices in row
      row[indices] -= values_to_inject
      #append 1 for compromised reading
      labels.append(1)
    else:
      labels.append(0)
  #return tuple of updated features and generated labels
  return (features, labels)

#tuple of new injected features and labels
inj_tuple = inject(features, 2, 0.5)
features = inj_tuple[0]
labels = inj_tuple[1]

#Simulating FDIA on generated data set

"""###Dos Function"""

#Simulating DoS on generated data set