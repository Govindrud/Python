from numpy import numerical operations
import numpy as np

#----------------------------------------------------------
# step 1: Define Input Features
#------------------------------------------------------------

# These are the inputs coming to the neuron (x1,x2,x3)

#Example : could be marks pixel values, or any features

inputs = np.array([2.0,3.0,4.0])


#------------------------------------------------------------
# step 2: Define Weights
#------------------------------------------------------------

# Each input has a corresponding weight(w1,w2,w3)
# Weights represent importance of each input

weights = np.array([0.5,0.3,0.2])


#------------------------------------------------------------
# step 3: Define Bias
#------------------------------------------------------------

#Bias is an additional parameter that helps shift the output
# It allows the model to fit data better

bias = 1.0

