# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:27:41 2020

@author: azer
"""

import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import sys
import statistics as stat

# SCP here!!!


d_gap = 8;

filename5 = 'C://Users//azer//workspace//uw_thesis//figures//metrics//unilever//dist_4.csv';
print filename5;
csv_data5 = pd.read_csv(filename5, sep=',',header=None);
neg_area_vals_5 = csv_data5.values[:,0];

negative_list_wrong = [];
for i in range(0, len(neg_area_vals_5)):
    negative_list_wrong.append(neg_area_vals_5[i]);
    
#scf_vals = negative_list_wrong;


## HISTOGRA< HERE

h_gap = 0.05;
r_vals = np.arange(h_gap, 20, h_gap);
r_vals = np.insert(r_vals, 0, 0);

green_array = negative_list_wrong;
green_array = [x for x in green_array if x >= 1e-5];
green_idx = r_vals[:len(green_array)];
#green_array_grad = np.abs( np.gradient(green_array) );



plt.clf()
plt.xlim([0, max(green_idx)])
plt.ylim([0, max(green_array)])
plt.plot(green_idx, np.asarray(green_array), 'b', linewidth=1);
plt.plot([3, 3], [0, 0.5], 'k--')
plt.plot([5, 5], [0, 0.5], 'k--')
#plt.scatter(green_idx, green_array, color = 'rgb')
plt.show();