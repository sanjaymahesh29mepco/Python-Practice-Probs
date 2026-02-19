import numpy as np
a=["#,1,2,3,A,B,C"]
b=["#,1,3,2,D,E,F"]
c=["$,1,2,1,X,Y,Z"]
print(np.setdiff1d(a,b))