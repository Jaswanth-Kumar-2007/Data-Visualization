import matplotlib as mpl 
mpl.use("PDF") 
import matplotlib.pyplot as plt 
from scipy.stats import norm 
import numpy as np 

import math 
mu = 0 
variance = 1 
sigma = math.sqrt(variance) 
x = np.linspace(-3, 3, 201) 
plt.plot(x, norm.pdf((x-mu)/sigma),linewidth=2.0, label='normal')
plt.plot(x, norm.cdf((x-mu)/sigma),linewidth=2.0, label='normal')
plt.legend(bbox_to_anchor=(.35,1)) 

plt.savefig('Gaussian.pdf', bbox_inches='tight')