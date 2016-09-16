import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def bayes_beta_dist(size):
    '''function generates a configurable chart of beta distributions for 
    an array of heads/tails counts. '''
    heads = [0,1,2,4,16,32]
    tails = heads
    n = len(heads)
    m = len(tails)
 #   fig, ax = plt.subplots(n,m,figsize=(size*1.615, size))
    for row in range(n):
        for col in range(m):
            x = np.linspace(0.0,1.0,100)
            plt.plot(x,beta.pdf(x,heads[row]+1,tails[col]+1), linewidth=2)
    plt.yaxis.set_visible(False)
    plt.xaxis.set_visible(False)


    plt.suptitle('Conjugate Prior of Coin Bias', fontsize = size*4, y=.98)
    plt.subplots_adjust(hspace=.75)
    plt.show()
    return fig

if __name__ == '__main__':
    fig = bayes_beta_dist(10)
   # fig.savefig('conjugate_prior.png')
