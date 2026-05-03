#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
from sklearn import __version__ as sklearn_version
import dvc
import mlflow
from termcolor import colored

print(colored("MLOps Environment Ready!", "green"))
print("Python Environment")
print(f"  Python version: {sys.version.split()[0]}")
print(f"  Python location: {sys.executable}")
print("Core Libraries")
print(f"  pandas {pd.__version__}")
print(f"  numpy {np.__version__}")
print(f"  scikit-learn {sklearn_version}")
print(f"  dvc {dvc.__version__}")
print(f"  mlflow {mlflow.__version__}")
print(colored("Ready to start MLOps adventures!", "cyan"))
