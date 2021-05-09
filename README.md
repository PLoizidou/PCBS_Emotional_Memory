# Emotional Memory Project


## Plan
This is a project aiming ot replicate the analysis and graphs shown in Girardeau et al. 2017 (https://www.nature.com/articles/nn.4637.pdf?origin=ppub). Due to limited computational power and memory the analysis will only be done on one session of one rat. Moreover analysis will be limited to neural data (not behavioral).  All the analysis and illustrations will be performed in Python. The main Python modules to be used are numpy, pandas, matplotlib, and neuroseries (https://github.com/NeuroNetMem/neuroseries). I am familiar with all but the last module.  

**There are 3 main steps to complete:**
1. Acquire the data which are publicly available (https://crcns.org/data-sets/hc). I expect data regarding neural activity of cells recorded, sleep scoring, as well as some information about the location of the recording and the type of the cell (pyramidal, interneuron, etc.). 
2. Set up the loading of the data into the workspace and turn them into data that can be read by python. 
3. Replicate Figure 2C: plot the firing rates of the first type of cells against the second. To do so I need to 
      - compute the firing rates for each cell for each of the periods: REM and NREM
      - compute firing rate distribution for each type of cell


The most important question is whether any of the findings can be replicated with only a fraction of raw data.


## Data
The data were acquired from: https://crcns.org/data-sets/hc
