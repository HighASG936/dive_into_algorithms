
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

def get_results(loweroutcomes, higheroutcomes, split_candidate, lowest_error,   best_split,      \
                                                                                best_lowermean,  \
                                                                                best_highermean, ):
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
                                                                                lowest_error,    \
                                                                                best_split,      \
                                                                                best_lowermean,  \
                                                                                best_highermean,  )
    return best_split, lowest_error, best_lowermean, best_highermean 

def adding_depth(depth, data, best_var, best_split, generated_tree, best_lowermean, best_highermean):
    """
    
    """    
    if depth < maxdepth:
        splitdata1 = data.loc[data[best_var] <= best_split,:]
        splitdata2 = data.loc[data[best_var] > best_split,:]

        if len(splitdata1.index) > 10 and len(splitdata2.index) > 10:
            generated_tree[0][3] = getsplit(depth + 1, splitdata1, variables, outcome_variable)   
            generated_tree[1][3] = getsplit(depth + 1, splitdata2, variables, outcome_variable)
        else:
            depth = maxdepth + 1
            generated_tree[0][3] = best_lowermean
            generated_tree[1][3] = best_highermean       
    else:
        generated_tree[0][3] = best_lowermean
        generated_tree[1][3] = best_highermean       
    
    return generated_tree 

def getsplit(depth, data, variables, outcome_variable):
    """ """
    best_var = ''
    lowest_error = float('inf')
    best_split = None
    predictedvalues = list(data.loc[:, outcome_variable])
    best_lowermean = -1
    best_highermean = -1 

    for var in variables:
        allvalues = list(data.loc[:, var])
        splitted = get_splitpoint(allvalues, predictedvalues)

        if splitted[1] < lowest_error:
            best_split = splitted[0]
            lowest_error = splitted[1]
            best_var = var
            best_lowermean = splitted[2]
            best_highermean = splitted[3]
    
    generated_tree = [
                        [best_var, float('-inf'), best_split,[]], \
                        [best_var, best_split, float('inf'), []]
                     ]
    
    adding_depth(depth, data, best_var, best_split, generated_tree, best_lowermean, best_highermean)
    return generated_tree

def get_prediction(observation, tree):
    j = 0
    keepgoing = True
    prediction = -1

    while keepgoing:
        j += 1
        variable_tocheck = tree[0][0]
        bound1 = tree[0][1]
        bound2 = tree[0][2]
        bound3 = tree[1][2]

        if observation.loc[variable_tocheck] < bound2:
            tree = tree[0][3]
        else:
            tree = tree[1][3]
        if isinstance(tree, float):
            keepgoing = False
            prediction = tree
    return prediction
    

if __name__ == '__main__':
    
    #Downloading our dataset
    ess = pd.read_csv('ess.csv', low_memory=False)    
    
    #Looking at the data
    print(ess.shape)
    print(ess.loc[:,'happy'].head())
    print(ess.loc[:,'sclmeet'].head())
    ess = get_restricted_dataset(ess)

    #Max Depth
    maxdepth = 4

    #Splitting our data
    meanlower, meanhigher = splitting_our_data(ess)
    print(f"{meanlower:.2}, {meanhigher:.2}")

    #Smarter Splitting
    allvalues = list(ess.loc[:, 'hhmmb'])
    predictedvalues = list(ess.loc[:, 'happy'])
    print(get_splitpoint(allvalues, predictedvalues))#best_split-lowest_error-best_lowermean-best_highermean

    #Choosing Splitting Variables
    variables = ['sclmeet', 'rlgdgr', 'hhmmb', 'netusoft', 'agea', 'eduyrs', 'health']
    outcome_variable = 'happy'
    print(getsplit(0, ess, variables, outcome_variable))

    #Evaluation our decision tree
    predictions = []
    thetree = getsplit(0, ess, variables, outcome_variable)

    for k in range(0, 30):
        observation = ess.loc[k, :]
        predictions.append(get_prediction(observation, thetree))
    
    print(predictions)

    predictions = []

    for k in range(0, len(ess.index)):
        observation = ess.loc[k, :]
        predictions.append(get_prediction(observation, thetree))

    ess.loc[:, 'predicted'] = predictions
    errors = abs(ess.loc[:, 'predicted'] - ess.loc[:, 'happy'])

    print(f"{np.mean(errors):.3}")

    
