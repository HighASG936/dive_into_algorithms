
import pandas as pd
import numpy as np


def get_restricted_dataset(ess):
    """
    Return dataset without incompleted responses
    """
    ess = ess.loc[ess['sclmeet'] <= 10, :].copy()
    ess = ess.loc[ess['rlgdgr'] <= 10, :].copy()
    ess = ess.loc[ess['hhmmb'] <= 50, :].copy()
    ess = ess.loc[ess['netusoft'] <= 5, :].copy()
    ess = ess.loc[ess['agea'] <= 200, :].copy()
    ess = ess.loc[ess['health'] <= 5, :].copy()
    ess = ess.loc[ess['happy'] <= 10, :].copy()
    ess = ess.loc[ess['eduyrs'] <= 100, :].copy().reset_index(drop=True)
    
    return ess

def get_low_social_happiness(social, happy):
    """ """
    return [hap for soc, hap in zip(social, happy) if soc <= 5]

def get_high_social_happiness(social, happy):
    """ """
    return [hap for soc, hap in zip(social, happy) if soc > 5]

def splitting_our_data(ess):
    """ """
    social = list(ess.loc[:, 'sclmeet'])
    happy = list(ess.loc[:, 'happy'])
    meanlower = np.mean(get_low_social_happiness(social, happy))
    meanhigher = np.mean(get_high_social_happiness(social, happy))
    return float(meanlower), float(meanhigher)

def get_loweroutcomes(allvalues, predictedvalues, split_candidate):
    """Return a list """
    return [outcome for value, outcome in zip(allvalues, predictedvalues) \
                     if value <= split_candidate] 

def get_higheroutcomes(allvalues, predictedvalues, split_candidate):
    """ """
    return [outcome for value, outcome in zip(allvalues, predictedvalues) \
                     if value > split_candidate] 

def get_lowererrors(meanlower, loweroutcomes):
    """ """
    return [abs(outcome - meanlower) for outcome in loweroutcomes]

def get_higererrors(meanhigher, higheroutcomes):
    """ """
    return [abs(outcome - meanhigher) for outcome in higheroutcomes]

def get_results(loweroutcomes, higheroutcomes, split_candidate, lowest_error):
    """ """
    if np.min([len(loweroutcomes), len(higheroutcomes)]) > 0 :
        meanlower = np.mean(loweroutcomes)
        meanhigher = np.mean(higheroutcomes)
        lowererrors = get_lowererrors(meanlower, loweroutcomes)
        higererrors = get_higererrors(meanhigher, higheroutcomes)
        total_error = sum(lowererrors) + sum(higererrors)
        if total_error < lowest_error:
            best_split = split_candidate
            lowest_error = total_error
            best_lowermean = meanlower
            best_highermean = meanhigher
    return best_split, lowest_error, best_lowermean, best_highermean

def get_splitpoint(allvalues, predictedvalues):
    """ """
    lowest_error = float('inf')
    best_split = None
    best_lowermean = np.mean(predictedvalues)
    best_highermean = np.mean(predictedvalues)
    for pctl in range(0, 100):
        split_candidate = np.percentile(allvalues, pctl)
        loweroutcomes = get_loweroutcomes(allvalues, predictedvalues, split_candidate)
        higheroutcomes = get_higheroutcomes(allvalues, predictedvalues, split_candidate)
        best_split, lowest_error, best_lowermean, best_highermean = get_results(loweroutcomes,   \
                                                                                higheroutcomes,  \
                                                                                split_candidate, \
                                                                                 lowest_error)
        return best_split, lowest_error, best_lowermean, best_highermean 

if __name__ == '__main__':
    
    #Downloading our dataset
    ess = pd.read_csv('ess.csv', low_memory=False)    
    
    #Looking at the data
    print(ess.shape)
    print(ess.loc[:,'happy'].head())
    print(ess.loc[:,'sclmeet'].head())
    ess = get_restricted_dataset(ess)

    #Splitting our data
    meanlower, meanhigher = splitting_our_data(ess)
    print(f"{meanlower:.2}, {meanhigher:.2}")

    #Smarter Splitting
    allvalues = list(ess.loc[:, 'hhmmb'])
    predictedvalues = list(ess.loc[:, 'happy'])
    print(get_splitpoint(allvalues, predictedvalues))#best_split-lowest_error-best_lowermean-best_highermean

