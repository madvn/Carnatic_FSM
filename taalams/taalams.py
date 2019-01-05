'''
File containing a dict with beat counts for different taalams

Run this file, after every update to create the updated pickle

Madhavun Candadai
Jan, 2018
'''
import pickle

# taalam information
taalam_dict = {
'aadi' : 8,
'roopak': 6
}

# save taalam_dict to pickle file
pickle.dump(taalam_dict,open('taalam.pkl','wb'),pickle.HIGHEST_PROTOCOL)
