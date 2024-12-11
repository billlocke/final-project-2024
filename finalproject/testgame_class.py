import numpy as np
import pandas as pd
import unittest
#import finalproject
from die import Die
from game import Game

class GameTestSuite(unittest.TestCase):
    
    def test_1_play(self): 
        # 
        print ('entering test_1_play')        
 
        loop_result_list = []    # contains each die's roll result
        self.df_to_return = pd.DataFrame (index = range(len(self.die_list)))
        self.df_to_return.index.name = 'Roll#'
        
        for i in range(len(self.die_list)):    # roll each die
            loop_result = self.die_list[i].roll_die(number_of_rolls)
            
            self.df_to_return = pd.concat ([self.df_to_return, loop_result], axis=1,\
                                          ignore_index=True)
            loop_result_list.append (loop_result)
                
        self.assertTrue(len(self.die_list) > 0)


    def test_2_show_game_results(self):
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
    
if __name__ == '__main__':
    unittest.main(verbosity=3)