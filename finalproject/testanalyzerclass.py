import numpy as np
import pandas as pd
import unittest
import finalproject
from die import Die
from game import Game
from analyzer import Analyzer
        
class AnalyzerTestSuite(unittest.TestCase):
    
    def test_1_jackpot(self): 
        # 
        print ('entering test_1_jackpot')        
 
        faces = np.arange (6)  # creates array
        faces_df = Die(faces)
        print ('initialized:')

        faces_df.change_weight (4, 5)
        print ('weight changed:')

    def test_2_face_counts_per_roll(self):
        print ('entering test_2_create_die')
        # 
        '''Create the die using the object's weights. Save to self as a DataFrame.'''
        n_sides = len(self.faces_df.weights)
        my_probs = [i/sum(self.faces_df.weights) for i in self.faces_df.weights]
        self.die = pd.DataFrame({
        'side': range(1, n_sides + 1),
        'weights': my_probs
        })
        self.assertTrue(isinstance (self.die, pd.DataFrame))
        return self.die

    def test_3_combo_count(self):
        print ('entering test_3_combo_count')

    def test_4_permutation_count(self):
        print ('entering test_4_permutation_count')

if __name__ == '__main__':
    unittest.main(verbosity=3)
