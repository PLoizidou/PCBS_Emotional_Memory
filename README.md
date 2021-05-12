# Emotional Memory Project: How do the firing rates of pyramidal and inetrneurons vary across different brain states?

The hippocampus and the basolateral amygdala are the two brain regions thought to be important in the formation and consolidation of this type of memory. Giradeau et al, 2017 [1] recorded neural ensembles in these two regions while four rats learned the location of an aversive air puff on a linear track, as well as during sleep before and after training. The dynamics of this brain regions and how they might contribute to memory consolidation are currently unknown. One first step to understand this mechanism, and the main goal of this project,  is to analyze how the the firing rate of cells in each region vary across different brain states: wake, drowsy, rapid eye movement (REM) sleep and non-rapid eye movement (NREM) sleep. In doing so, it is relevant to separate the cells based on their physiology. Three main categories of cells were identified in the dataset (after spike sorting and connectivity analysis): pyramidal neurons, interneurons, and unknown cells (not clearly belonging to either of the other two categories).


## Plan
This is a project aiming to replicate the analysis and graphs shown in Girardeau et al. 2017 (https://www.nature.com/articles/nn.4637.pdf?origin=ppub). Due to limited computational power and memory the analysis will only be done on one session of one rat. Moreover analysis will be limited to neural data (not behavioral).  All the analysis and illustrations will be performed in Python. The main Python modules to be used are numpy, pandas, matplotlib, and neuroseries (https://github.com/NeuroNetMem/neuroseries). 

**There are 3 main steps to complete:**

2. Set up the loading of the data into the workspace and turn them into data that can be read by python. 
3. Replicate Figure 2C: plot the firing rates of the first type of cells against the second. To do so I need to 
      - compute the firing rates for each cell for each of the periods: REM and NREM
      - compute firing rate distribution for each type of cell during each state.


## Dataset
The data are publicly available and were acquired from: https://crcns.org/data-sets/hc/hc-14
More details about the data can be found here: https://crcns.org/data-sets/hc/hc-14/about-hc-14

The dataset used includes files with information about spike activity, sleep scoring, as well as some the location of the recording and the type of the cell (pyramidal, interneuron, etc.). 

The total sessions of recordings for the four rats were initially 61. Three sessions were excluded because of incomplete data resulting in a final dataset of 58 sessions. Each session usually includes a long wake period and multiple sleep (drowsy, REM, NREM) periods.
Between 1300 and 2300 neurons were recorded from each rat (summed across all sessions, all regions, and all states).
 
All the data were saved locally. Each session corresponded to a different local directory of which the path is included in a list found in the file:
The file as it is right now is not particularly useful for other users, but provides an example of how local paths can incorporated in the analysis.

### Notation:
Brain states:
REM sleep:'sws' (standing for slow wave sleep)
NREM sleep: 'Nrem'
Wake periods: 'Wake'
Periods of drowsiness (falling asleep): 'drowsy'

Brain types:
Pyramidal cells: 'Pyr'
Interneurons:'Int'
Unknown cells: 'Unk'

Brain regions:
Basolateral Ammygdala: 'BLA'
Hippocampus: 'Hpc'

## What the analysis does
1. It loads spike data and metadata (using the bk.load module).
2. Separates neurons into neuron types
3. Computes the firing rates for each of the neuron types for specified states.
4. Plots a scatter plot showing how the firing rates of cells during a period relate to the firing rates of another period.
5. Plots a histogram showing the distribution of firing rates for different types of cells during the selected brain states.

 
## How to run the analysis

## Results obtained

## To do
- An obvious limitation of this project is the inability of the user to run the script without needing to download a heavy dataset. So, the next step is to use datalad, get the data from crcn.org, and allow other users to run the code easily. 
- A second limitation is that this code is adapted to the data in hand: recordings from two regions and three types of cells (pyramidal, interneurons, unknown/other). Therefore, it needs adaptations to work on different datasets.
- There is no option to compare the firing rates of different cells across two different brain states (i.e. pyramidal neurons during REM sleep vs. interneurons during NREM sleep)
- Future addition should be a statistical test evaluating if the distributions are significantly different across states.

## My coding experience
- I have used the modules numpy, pandas, and matplotlib before for other projects.
- I have been using some of the functions found in the bk module since February for my internship. However, I am using functions regarding local field potentials not spikes. This script also uses neuroseries which I am not very familiar with.
- I would consider myself an intermediate python user.

## What have I learned?
- I am going to use spike data for my internship this summer, so, this project was a good introduction to the nature of binary data and how to use them. 
- I usually write very ugly code, with lots of repeats, which I can only use once because I don't remeber what's going on the next day. This project forced me to write functions and make them short and understandable(hopefully).
- Git and Github Desktop! I had no idea how much I needed this.
- Regular expressions and clean code are very useful. 
- I think the biggest contribution of this course to my skills was to make programming appear a bit more fun and a bit less scary. 

## What did I miss in this course?
- While I loved some exercises (the one with the tree drawing was by far my favourite), I missed classes on libraries like NumPy, pandas, and Matplotlib which I feel are very useful for cognitive sciences.  


[1] Girardeau, G., Inema, I., & Buzsáki, G. (2017). Reactivations of emotional memory in the hippocampus–amygdala system during sleep. Nature neuroscience, 20(11), 1634.
