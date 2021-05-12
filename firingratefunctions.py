import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import bk.load

def categorize_types_regions(session, brain_region):
    bk.load.current_session(session)
    neurons, metadata = bk.load.loadSpikeData(session)
    pyramidal = neurons[(metadata['Type']=='Pyr') & (metadata['Region']==brain_region)]
    interneurons = neurons[(metadata['Type']=='Int') & (metadata['Region']==brain_region)]
    other_neurons = neurons[metadata['Type']=='Unk']
    return pyramidal, interneurons, other_neurons

def calculate_firing_rate_per_state(neurons, state):
    """
    Returns a pandas Series with the mean firing rate of each of the neurons during a chosen state (REM, sws, drowsy, or wake)
    
    Keyword arguments:
    neurons -- numpy.ndarray containing series data of selected neurons 
    state -- string, should be one of the following: Rem, sws, drowsy, wake (default='REM')
    
    Restrictions:
    Can only be called when the neurons and session have already been loaded.
    """
    mean_firing_rates = pd.Series(index = np.arange(len(neurons)),dtype='float64')
    state_used = bk.load.states()[state]

    for i in range(len(neurons)):
        try:
            spk_time = neurons[i].restrict(state_used).as_units('ms').index.values
            mean_firing_rates[i] = len(spk_time)/state_used.tot_length('s')
        except Exception:
            pass #using this exeption because not all neurons have spikes in all states (represented by NaN values). The NaN values cannot be used to calculate firing rates.
    return mean_firing_rates


def calculate_firing_rate_per_state_per_type(session, states, brain_region):
    '''
    Returns 2 lists (one for each state) with the mean firing rate of each of the types of neurons (Pyramidal, interneurons, unknown) during the chosen state.
    
    Keyword arguments:
    session -- string containing the dircetory where the data files are stored
    states -- list of 2 strings, should be one of the following: REM, sws, drowsy, wake (default='REM')
    '''
    neurons_by_type=categorize_types_regions(session, brain_region)
    firing_rates_state0=[]
    firing_rates_state1=[]
    for i in neurons_by_type:
        state0=calculate_firing_rate_per_state(i, states[0])
        state1=calculate_firing_rate_per_state(i, states[1])
        firing_rates_state0.append(state0)
        firing_rates_state1.append(state1)
    return firing_rates_state0, firing_rates_state1


def calculate_firing_rates_multiple_sessions(sessions, states, brain_region):
    '''
    Returns N numpy arrays (one for each state) with the mean firing rate of each of the types of neurons (Pyramidal, interneurons, unknown) during the chosen state
    where N is the number of sessions.
    Returned lists structure = Number of sessions * number of types of cells(=3) * number of cells(depends on session)
    
    Keyword arguments:
    sessions -- list of strings containing the dircetories where the data files for each sessions are stored
    states -- list of 2 strings, should be one of the following: REM, sws, drowsy, wake (default='REM')
    '''
    
    all_sessions_state0=[]
    all_sessions_state1=[]

    for session in sessions:
        FR_per_cell_state0,FR_per_cell_state1=calculate_firing_rate_per_state_per_type(session, states, brain_region)
        all_sessions_state0.append(FR_per_cell_state0)
        all_sessions_state1.append(FR_per_cell_state1)
    return np.array(all_sessions_state0,dtype=object), np.array(all_sessions_state1,dtype=object)


def double_flatten(array):
    flat_1=np.concatenate(array).ravel()
    flat_2=np.concatenate(flat_1).ravel()
    return flat_2


def plot_scatter(sessions, states, brain_region):
    state0,state1=calculate_firing_rates_multiple_sessions(sessions, states, brain_region)
    identity=np.linspace(-10,100,101) 
    plt.plot(identity,identity, 'k-', color='b')
    title=brain_region+' : '+states[0]+ ' vs '+ states[1]
    for i in range(len(state0)):
        plt.scatter(state0[i][2],state1[i][2], color='gray',alpha=0.5)
        plt.scatter(state0[i][0],state1[i][0], color='r', alpha=0.5)
        plt.scatter(state0[i][1],state1[i][1], color='b', alpha=0.5)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel(f'{states[0]} rate (Hz)')
    plt.ylabel(f'{states[1]} rate (Hz)')
    plt.title(str(title))
    plt.legend(['Identity line','Other', 'Pyramidal', 'Interneurons'])
    plt.show()



def plot_histogram(data, title, bin_size=50, upper_axis_bound=100, lower_axis_bound=0.1):
    other,inter,pyr=np.hsplit(data,3)
    pyr=double_flatten(pyr)
    inter=double_flatten(inter)
    other=double_flatten(other)
    logbins = np.logspace(np.log10(lower_axis_bound),np.log10(upper_axis_bound),bin_size)
    plt.hist(other, logbins, color='gray', label='Other')
    plt.xscale('log')
    plt.hist(pyr, logbins, color='r', label='Pyramidal')
    plt.xscale('log')
    plt.hist(inter, logbins, color='b', label='Interneurons')
    plt.xscale('log')
    plt.title(str(title))
    plt.legend()
    plt.show()



def plot_both_histograms(sessions, states, brain_region,bin_size=50, upper_axis_bound=100, lower_axis_bound=0.1):
    state0,state1=calculate_firing_rates_multiple_sessions(sessions, states, brain_region)
    histogram_region_1=plot_histogram(state0, title=brain_region+ states[0])
    histogram_region_2=plot_histogram(state1, title=brain_region+ states[1])

