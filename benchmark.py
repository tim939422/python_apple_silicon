import time
import numpy as np
import scipy as sp
from scipy import linalg

def benchmark_numpy_svd():
    """benchmark svd function of numpy
    
    Fork from:
    https://gist.github.com/MarkDana/a9481b8134cf38a556cf23e1e815dafb
    
    """
    print("----------------------------------------------")
    print("Running benchmark_numpy_svd:")
    print("----------------------------------------------\n\n")
    rng = np.random.default_rng(seed=42)
    a = rng.uniform(size=(300, 300))
    runtimes = 10
    
    timecosts = []
    for i in range(runtimes):
        s_time = time.time()
        for i in range(100):
            a += 1
            np.linalg.svd(a)
            
        timecosts.append(time.time() - s_time)
        
    print(f'mean of {runtimes} runs: {np.mean(timecosts):.5f}s')    

def benchmark_scipy_svd():
    """benchmark svd function of scipy
    
    Adapted from benchmark_numpy_svd:
    
    """
    print("----------------------------------------------")
    print("Running benchmark_scipy_svd:")
    print("----------------------------------------------\n\n")
    rng = np.random.default_rng(seed=11)
    a = rng.uniform(size=(300, 300))
    runtimes = 10
    
    timecosts = []
    for i in range(runtimes):
        s_time = time.time()
        for i in range(100):
            a += 1
            linalg.svd(a)
            
        timecosts.append(time.time() - s_time)
        
    print(f'mean of {runtimes} runs: {np.mean(timecosts):.5f}s')
    
def benchmark_numpy_dario():
    """benchmark numpy 
    
    Adapted from dario.py mentioned in:
    https://gist.github.com/MarkDana/a9481b8134cf38a556cf23e1e815dafb
    
    """
    
    print("----------------------------------------------")
    print("Running benchmark_numpy_dario:")
    print("----------------------------------------------\n\n")
    
    s_time = time.time()
    
    rng =  np.random.default_rng(seed=121)
    
    # create matrix for benchmark
    size = 4096
    A, B = rng.random((size, size)), rng.random((size, size))
    C, D = rng.random((size * 128,)), rng.random((size * 128,))
    E = rng.random((size // 2, size // 4))
    F = rng.random((size // 2, size // 2))
    F = np.dot(F, F.T)
    G = rng.random((size // 2, size // 2))
    
    # matrix multiplication
    N = 20
    t = time.time()
    for i in range(N):
        np.dot(A, B)
    delta = time.time() - t
    print(f'Dotted two {size:d}x{size:d} matrices in {delta/N:.2f}s. (averaged by {N:d} runs)')
    del A, B
    
    # vector multiplication
    N = 5000
    t = time.time()
    for i in range(N):
        np.dot(C, D)
    delta = time.time() - t
    print(f'Dotted two vectors of length {size * 128:d} in {1e3 * delta / N:.2f}ms. (averaged by {N:d} runs)')
    del C, D
    
    # Singular Value Decomposition (SVD)
    N = 3
    t = time.time()
    for i in range(N):
        np.linalg.svd(E, full_matrices = False)
    delta = time.time() - t
    print(f"SVD of a {size // 2:d}x{size // 4:d} matrix in {delta/N:.2f}s. (averaged by {N:d} runs)")
    del E
    
    # Cholesky Decomposition
    N = 3
    t = time.time()
    for i in range(N):
        np.linalg.cholesky(F)
    delta = time.time() - t
    print(f"Cholesky decomposition of a {size // 2:d}x{size // 2:d} matrix in {delta/N:.2f}s. (averaged by {N:d} runs)")
    del F
    
    # Eigendecomposition
    N = 3
    t = time.time()
    for i in range(N):
        np.linalg.eig(G)
    delta = time.time() - t
    print(f"Eigendecomposition of a {size // 2:d}x{size // 2:d} matrix in {delta/N:.2f}s. (averaged by {N:d} runs)")
    del G
    
    print('')
    print(f'Total scripting time : {time.time() - s_time:.2f}s')

def main():
    print("----------------------------------------------")
    print("Numpy configuration")
    print("----------------------------------------------\n\n")
    print(np.show_config())
    print('\n\n')
    
    print("----------------------------------------------")
    print("Scipy configuration")
    print("----------------------------------------------\n\n")
    print(sp.show_config())
    print('\n\n')
    
    
    benchmark_numpy_svd()
    print('\n\n')
    benchmark_scipy_svd()
    print('\n\n')
    benchmark_numpy_dario()
    

if __name__ == '__main__':
    main()