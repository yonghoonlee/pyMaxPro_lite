import time
import numpy as np
import numpy.matlib as matlib
from scipy.optimize import dual_annealing

class maxpro_design:
    def __init__(self):
        self.s = 2.0
        self.n = 8
        self.p = 2
        self.random_seed = np.random.RandomState(100)
        self.no_local_search = True
        self.L_BFGS_B_eps = 1e-4
        self.L_BFGS_B_maxiter = 10
        self.dual_annealing_maxiter = 2000
        self.x = None

    def objective(self, xin):
        obj = 0.0
        n = self.n
        p = self.p
        x = xin.reshape((n,p))
        for idx in range(0, n-1): # 0 1 2 ... n-2
            for jdx in range(idx+1, n): # idx+1 idx+2 ... n-1
                obj += 1.0/np.prod(np.abs(x[idx,:] - x[jdx,:])**self.s)
        return obj

    def solve(self):
        res = dual_annealing(
            self.objective,
            bounds = [(0.0, 1.0)]*(self.n*self.p),
            maxiter = self.dual_annealing_maxiter,
            local_search_options = {
                'method': 'L-BFGS-B',
                'bounds': [(0.0, 1.0)]*(self.n*self.p),
                'options': {
                    'eps': self.L_BFGS_B_eps,
                    'maxiter': self.L_BFGS_B_maxiter,
                },
            },
            seed = self.random_seed,
            no_local_search = self.no_local_search,
        )
        self.x = res.x.reshape((self.n, self.p))
        return self.x

if __name__ == '__main__':
    
    start_time = time.time()
    
    mpd = maxpro_design()
    mpd.n = 8
    mpd.p = 2
    mpd.s = 2.0
    x = mpd.solve()

    print('Execution time: {:} seconds'.format(time.time() - start_time))

    from matplotlib import pyplot as plt
    fig = plt.figure()
    for idx in range(0, mpd.n):
        plt.plot(x[idx,0],x[idx,1],'ks')
    plt.show()
