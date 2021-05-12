# Emotional Memory Project: How do the firing rates of pyramidal and inetrneurons vary across different brain states?

The hippocampus and the basolateral amygdala are the two brain regions thought to be important in the formation and consolidation of this type of memory. Giradeau et al, 2017 [1] recorded neural ensembles in these two regions while four rats learned the location of an aversive air puff on a linear track, as well as during sleep before and after training. The dynamics of this brain regions and how they might contribute to memory consolidation are currently unknown. One first step to understand this mechanism, and the main goal of this project,  is to analyze how the the firing rate of cells in each region vary across different brain states: wake, drowsy, rapid eye movement (REM) sleep and non-rapid eye movement (NREM) sleep. In doing so, it is relevant to separate the cells based on their physiology. Three main categories of cells were identified in the dataset (after spike sorting and connectivity analysis): pyramidal neurons, interneurons, and unknown/other cells (not clearly belonging to either of the other two categories).

![RatBrain-Interactions](https://user-images.githubusercontent.com/54603452/118034569-69ed5980-b36a-11eb-8cea-de84dbf16b00.png)

## Dataset
The data are [publicly available](https://crcns.org/data-sets/hc/hc-14) and more details about them can be found [here](https://crcns.org/data-sets/hc/hc-14/about-hc-14).

The dataset used includes files with information about spike activity, sleep scoring, as well as some the location of the recording and the type of the cell (pyramidal, interneuron, etc.). 

The total sessions of recordings for the four rats were initially 61. Three sessions were excluded because of incomplete data resulting in a final dataset of 58 sessions. Each session usually includes a long wake period and multiple sleep (drowsy, REM, NREM) periods.
Between 1300 and 2300 neurons were recorded from each rat (summed across all sessions, all regions, and all states).
 
All the data were saved locally. Each session corresponded to a different local directory of which the path is included in a list found in [here](https://github.com/PLoizidou/PCBS_Emotional_Memory/blob/main/save_session_paths.py). The file as in its current state is not particularly useful for other users, but provides an example of how local paths can saved as binary data and then incorporated in the analysis.

### Notation:
**Brain states:**
- REM sleep:'Rem'
- NREM sleep: 'sws' (standing for slow wave sleep)
- Wake periods: 'Wake'
- Periods of drowsiness (falling asleep): 'drowsy'

**Brain types:**
- Pyramidal cells: 'Pyr'
- Interneurons:'Int'
- Unknown/Other cells: 'Unk'

**Brain regions:**
- Basolateral Ammygdala: 'BLA'
- Dorsal Hippocampus: 'Hpc'

## What the analysis does

The goal of this analysis was to result in the graphs shown below and allow the user to do any comparison of interest between brain states.

![alt text](https://github.com/PLoizidou/PCBS_Emotional_Memory/blob/main/Figures/GG2017.PNG)

1. It loads spike data and metadata (using the bk.load module).
2. Separates neurons into neuron types.
3. Computes the firing rates for each of the neuron types for two specified states.
4. Plots a scatter plot showing how the firing rates of cells during a period relate to the firing rates of another period.
5. Plots a histogram showing the distribution of firing rates for different types of cells during the selected brain states.
 
## How to run the analysis
The analysis can be run easily by choosing (a) the sessions the user wants to include, (b) the two brain states that the user wishes to compare, and (c) the brain structure of interest. 
Running the following script will result in the same comparisons shown in Figure 3C of Girardeau et al, 2017 [1](http://girardeaulab.org/wp-content/uploads/2018/08/Girardeau2017.pdf)

## Results obtained
### Wake vs NREM @BLA
**Scatter Plot:**

![wake_sws](https://user-images.githubusercontent.com/54603452/118032871-6d7fe100-b368-11eb-9774-7d33cd22dc25.png)

**Histograms:**

![BLA wake](https://user-images.githubusercontent.com/54603452/118034219-0531ff00-b36a-11eb-87d0-c927612a7519.png)

![BLA NREM](https://user-images.githubusercontent.com/54603452/118034226-095e1c80-b36a-11eb-867d-0cefdb34e3ee.png)

### Wake vs REM @BLA
**Scatter Plot:**

![wake_rem](https://user-images.githubusercontent.com/54603452/118034298-1f6bdd00-b36a-11eb-8c6b-2e6a623db7c1.png)

**Histograms:**

![BLA wake](https://user-images.githubusercontent.com/54603452/118034324-25fa5480-b36a-11eb-92fb-9a52fd487670.png)

![BLA REM](https://user-images.githubusercontent.com/54603452/118034342-28f54500-b36a-11eb-8dbf-78e3146114ba.png)

**The same analysis was ran on the dorsal hippocampus:**
### Wake vs REM @Hpc
**Scatter Plot:**

![wake_rem_Hpc](https://user-images.githubusercontent.com/54603452/118035539-9a81c300-b36b-11eb-94fc-c3145d4871ea.png)

**Histograms:**

![Hpc wake](https://user-images.githubusercontent.com/54603452/118035776-f8aea600-b36b-11eb-94e3-c92e902821da.png)

![Hpc REM](https://user-images.githubusercontent.com/54603452/118035782-f9dfd300-b36b-11eb-978d-2ff77d46f980.png)

### Wake vs NREM @Hpc
**Scatter Plot:**

![wake_Nrem_Hpc](https://user-images.githubusercontent.com/54603452/118035844-0f54fd00-b36c-11eb-926a-d669dca4b5b0.png)


**Histograms:**

![Hpc wake](https://user-images.githubusercontent.com/54603452/118035857-154ade00-b36c-11eb-9a0a-568fe8d34a09.png)

![Hpc NREM](https://user-images.githubusercontent.com/54603452/118035866-18de6500-b36c-11eb-8bbb-0bb9ecee2431.png)


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
- Regular expressions and clean code are very useful. !
- I think the biggest contribution of this course to my skills was to make programming appear a bit more fun and a bit less scary. 

## What did I miss in this course?
- While I loved some exercises (the one with the tree drawing was by far my favourite), I missed classes on libraries like NumPy, pandas, and Matplotlib which I feel are very useful for cognitive sciences.  


[[1] Girardeau, G., Inema, I., & Buzsáki, G. (2017). Reactivations of emotional memory in the hippocampus–amygdala system during sleep. Nature neuroscience, 20(11), 1634.](http://girardeaulab.org/wp-content/uploads/2018/08/Girardeau2017.pdf)
