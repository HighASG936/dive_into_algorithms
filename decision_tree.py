import pandas as pd
import numpy as np


def restrict_dataset(ess):
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

def splitting_our_data(ess):
    """ """
    social = list(ess.loc[:, 'sclmeet'])
    happy = list(ess.loc[:, 'happy'])

    low_social_happiness = [hap for soc, hap in zip(social, happy) if soc <= 5]
    high_social_happiness = [hap for soc, hap in zip(social, happy) if soc > 5]

    meanlower = np.mean(low_social_happiness)
    meanhigher = np.mean(high_social_happiness)

    return float(meanlower), float(meanhigher)


if __name__ == '__main__':
    
    #Downloading our dataset
    ess = pd.read_csv('ess.csv')    
    
    #Looking at the data
    print(ess.shape)
    print(ess.loc[:,'happy'].head())
    print(ess.loc[:,'sclmeet'].head())
    ess = restrict_dataset(ess)

    #Splitting our data
    meanlower, meanhigher = splitting_our_data(ess)
    print(f"{meanlower:.2}, {meanhigher:.2}")

    #Smtarter Splitting
    

