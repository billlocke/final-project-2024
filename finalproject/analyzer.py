import numpy as np
import pandas as pd
import unittest
import finalproject
from die import Die
#from game import Game

class Analyzer():
    '''General Definition
    An Analyzer object takes the results of a single game and 
    computes various descriptive statistical properties about it.
    Specific Methods and Attributes:
        1. An initializer
        2. Jackpot
        3. Face counts per roll
        4. Combo_count
        5. Permutation count
    '''
    def __init__(self, die_list):
        '''     
        Takes a game object as its input parameter.
        Throws a ValueError if the passed value is not a Game object
        '''
        self.die_list = die_list
        return
    
    def jackpot (self, number_of_rolls):
        '''
        A jackpot is a result in which all faces are the same,
            e.g. all ones for a six-sided die.
        Computes how many times the game resulted in a jackpot.
        Returns an integer for the number of jackpots. 
        '''
        self.number_of_rolls = number_of_rolls
        
        self.results1 = self.die_list.roll_die(self.number_of_rolls)
        print ('rolled die:') 
        print ('results:', self.results1)


    def face_counts_per_roll  (self, form = 'w'):
        '''
        Computes how many times a given face is rolled in each event.
        For example, if a roll of five dice has all sixes, 
            then the counts for this roll would be 
            for the face value ‘6’ and for the other faces.
        Returns a data frame of results.
        The data frame has an index of the roll number,
            face values as columns, 
            and count values in the cells (i.e. it is in wide format).   
           
        '''
        
    def combo_count (self, ):
        '''
        Computes the distinct combinations of faces rolled,
            along with their counts.
        Combinations are order-independent and may contain repetitions.
        Returns a data frame of results.
        The data frame should have a MultiIndex of distinct combinations
            and a column for the associated counts.
        
        '''

        
    def permutation_count (self, ):
        '''
        Computes the distinct permutations of faces rolled, a
            long with their counts.
        Permutations are order-dependent and may contain repetitions.
        Returns a data frame of results.
        The data frame should have a MultiIndex of distinct permutations
        and a column for the associated counts.
        
        '''

        '''my_results.value_counts().sort_index().plot.bar(rot=0);
        NARROW = pd.DataFrame(my_results).stack
        print ('NARROW:\n', NARROW)
        WIDE = pd.DataFrame(my_results).unstack()
        print ('my_results dimensions:', my_results.shape)
        print ('WIDE dimensions:', WIDE.shape)
        print ('WIDE:\n', WIDE)
'''