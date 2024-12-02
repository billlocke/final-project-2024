import numpy as np
import pandas as pd
import unittest
from die import Die

class DieTestSuite(unittest.TestCase):
    
    def test_1_change_weight(self): 
        # 
        print ('entering test_1_change_weight')        
 
        faces = np.arange (6)  # creates array
        faces_df = Die(faces)
        print ('initialized:')

        faces_df.change_weight (4, 5)
        print ('weight changed:')

    def test_2_create_die(self):
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
#        return self.die

    def test_3_roll_die(self):
        print ('entering test_3_roll_die')        
        # 
#        self.number_of_rolls = number_of_rolls
        # print (self.die, '\nsum of weights:', sum(self.die.weights))
        # print ('number of rolls:', self.number_of_rolls)   ##

        # This is essentially a random sample with replacement,
        #   from the private die data frame, that applies the weights.
        results = []
        for i in range(self.number_of_rolls):
            result = self.die.side.sample(weights=self.die.weights, replace=True).values[0]
            results.append(result)
        self.result = pd.DataFrame(results)
        self.assertTrue(self.number_of_rolls >= 0)
        return (self.result)
        #return pd.Series(results)

    def test_4_show_die_state(self):
        print ('entering test_4_show_die_state')
        self.die = die
        die_deep = self.die.copy()
        self.assertTrue(isinstance (die_deep, pd.DataFrame))
        return die_deep

faces = np.arange (6)  # creates array
faces_df = Die(faces)
print ('initialized in test:')

faces_df.change_weight (4, 5)
print ('weight changed in test:')

die = faces_df.create_die (faces_df)    # create die with updated weights
print ('die created in test:')
#print ('this is the created die:\n', die)

#print ('show die state with method call:')
die_deep2 = faces_df.show_die_state (die)
print ('show die state2 in test:\n', die_deep2)

results = faces_df.roll_die(10)
print ('roil_die in test:')
print ('results:', results)
faces_df.plot_results (results)
print ('plot_results in test:')

if __name__ == '__main__':
    unittest.main(verbosity=3)
