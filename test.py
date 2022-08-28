import sys
import numpy as np

if __name__=="__main__":
	mu = int(sys.argv[1]) if len(sys.argv) > 1 else 0
	sigma = float(sys.argv[2]) if len(sys.argv) > 2 else 1
	print(np.random.normal(mu,sigma))
