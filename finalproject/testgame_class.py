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
 
        faces = np.arange (6)  # creates array
        faces_df1 = Die(faces) # instantiate DIe objects
        faces_df2 = Die(faces)
        #print ('initialized:')

        faces_df1.change_weight (4, 5)
        #print ('weight changed:')

        die1 = faces_df1.create_die (faces_df1)  # create die
        die2 = faces_df2.create_die (faces_df2)
        #print ('created die:')

        print ('show die state 1:')
        die_deep1 = faces_df1.show_die_state (die1)
        #print (die_deep1)
        #print ('show die state 2:')
        die_deep2 = faces_df2.show_die_state (die2)
        #print (die_deep2)

        die_list = [faces_df1, faces_df2]
        #print ('die_list:', die_list)

        game_to_play = Game(die_list)     # instantiate Game
        n_rolls = 10

        #print ('play die 2:') 
        results2 = game_to_play.play(n_rolls)
                
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