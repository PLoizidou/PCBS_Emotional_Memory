
""" This is file that can be run to obtain different comparisons across brain states for three different kinds of neurons. The user can choose the sessions of interest (sessions are represented by local directories with the files associated with each session), two brain states among 'sws', 'wake','Rem', and 'drowsy', and finally a brain structure among 'Hpc' and 'BLA'"""

import firingratefunctions as fr
import pickle

with open('sessions.pkl', 'rb') as f:
    session_paths = pickle.load(f)

fr.plot_scatter(session_paths, ['wake','sws'], 'Hpc')

fr.plot_scatter(session_paths, ['wake','Rem'], 'Hpc')

fr.plot_both_histograms(session_paths, ['wake','sws'], 'Hpc',bin_size=50, upper_axis_bound=100, lower_axis_bound=0.1)

fr.plot_both_histograms(session_paths, ['wake','Rem'], 'Hpc',bin_size=50, upper_axis_bound=100, lower_axis_bound=0.1)