import numpy as np

address , keys , name  = np.genfromtxt("C:/Users/admin/OneDrive/Documents/GitHub/AI-Course/FastFoodRestaurants (1).csv ", delimiter="," , dtype=None ,invalid_raise=False ,  unpack=True , usecols=(0, 3, 6,) , skip_header=1)

print("address:" , address[:10])
print("keys:" , keys[:10])
print("name:" , name[:10])