import random
import numpy as np
from scipy.stats import binom
import pandas as pd

def get_minimum_targets_binom(p, alpha, k):
    minimum_targets = []
    p_np = p[1:]

    for i in range(k):
        mt = []
        for p_j in p_np:
            mt.append(binom.ppf(alpha, i+1, p_j))
        minimum_targets.append(mt)   
    df = pd.DataFrame(data=(np.array(minimum_targets)).astype(int))
    df.columns = p_np
    df.index = np.array(range(k))+1
    df.to_html("binomial2Multinomial_"+str(p)+".html")
    return minimum_targets 

def create_ranking_yang_stoyanovich(p, k, minimum_targets):
    ''' Create a ranking of 'k' positions in which at each position the
        probability that the candidate is protected is 'p'.
    '''
    ranking = []
    cumulative_p = [p[0]]
    counter = [0]*len(p)
    singleTest = [0]*k
    multipleTest = 0
    multiple_incremented = False
    
    for x in range(1, len(p)):
        cumulative_p.append(cumulative_p[x-1]+p[x])
    for i in range(k):
        rand_p = random.random()
        if rand_p <= cumulative_p[0]:
            ranking.append(0)
            counter[0] = counter[0] + 1
        else:     
            for j in range(1, len(cumulative_p)):
                if rand_p > cumulative_p[j-1] and rand_p <= cumulative_p[j]:
                    ranking.append(j)
                    counter[j] = counter[j] + 1
        if(any(counter[a+1]<minimum_targets[i][a] for a in range(len(counter)-1))):
#             print "k = ",i+1,", ",counter[1:],": ",minimum_targets[i]
            singleTest[i] = singleTest[i] + 1
            if multiple_incremented == False :
                multipleTest = multipleTest + 1
                multiple_incremented = True
    return ranking, np.array(singleTest), multipleTest

def perform_single_multiple_test(N, p ,k ,alpha):
    minimum_targets = get_minimum_targets_binom(p, alpha, k)
    singleTest = np.zeros(k)
    multipleTest = 0

    for i in range(N):
        ranking, single, multiple = create_ranking_yang_stoyanovich(p, k,minimum_targets)
        print single
        singleTest = singleTest + single
        print "singleTest: ",singleTest
        multipleTest = multipleTest + multiple

    df = pd.DataFrame(data=(np.array(singleTest)).astype(int))
    df.columns = ["# failed rankings at k"]
    df.index = np.array(range(k))+1
    df.to_html("singleTest"+str(p)+".html")
    return singleTest, multipleTest

p = [0.4,0.6]
k = 100
N = 100
alpha = 0.1

perform_single_multiple_test(N, p ,k ,alpha)        