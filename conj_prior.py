import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def bayes_beta_dist(size):
    heads = [0,1,2,4,16,32]
    tails = heads
    n = len(heads)
    m = len(tails)
    fig, ax = plt.subplots(n,m,figsize=(size*1.615, size))
    for row in range(n):
        for col in range(m):
            x = np.linspace(0.0,1.0,100)
            ax[row,col].plot(x,beta.pdf(x,heads[row]+1,tails[col]+1), linewidth=2)
            ax[row,col].set_title("Heads: {}      Tails: {}"
                                  .format(str(heads[row]),str(tails[col])), fontsize=size, y=1.1)
            ax[row,col].yaxis.set_visible(False)
            ax[row,col].xaxis.set_visible(False)


    plt.suptitle('Conjugate Prior of Coin Bias', fontsize = size*4, y=.98)
    plt.subplots_adjust(hspace=.75)
#    plt.show()
    return fig

fig = bayes_beta_dist(10)
fig.savefig('conjugate_prior.png')
