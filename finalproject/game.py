import numpy as np
import pandas as pd
import unittest
#import finalproject
from die import Die

class Game():
    '''General Definition
    A game consists of rolling of one or more similar dice (Die objects)
        one or more times.
    By similar dice, we mean that each die in a given game 
        has the same number of sides and associated faces, 
        but each die object may have its own weights.
    Each game is initialized with a Python list 
        that contains one or more dice.
    Game objects have a behavior to play a game, 
        i.e. to roll all of the dice a given number of times.
    Game objects only keep the results of their most recent play.
    Specific Methods and Attributes;
        1. An initializer
        2. A play method
        3. Show results of the most recent play
    '''
    
    def __init__(self, die_list):
        self.die_list = die_list
        ''' Takes a NumPy array of faces as an argument.'''
        return
    
    def play (self, number_of_rolls):
        '''
        Takes parameter specifying how many times 
            the dice should be rolled. Saves result of the play
            to a private data frame.
        The data frame should be in wide format, 
            i.e. have the roll number as a named index, 
            columns for each die number 
            (using its list index as the column name),
            and the face rolled in that instance in each cell.'''
            
        loop_result_list = []    # contains each die's roll result
        self.df_to_return = pd.DataFrame (index = range(len(self.die_list)))
        self.df_to_return.index.name = 'Roll#'
        
        for i in range(len(self.die_list)):    # roll each die
            loop_result = self.die_list[i].roll_die(number_of_rolls)            
            self.df_to_return = pd.concat ([self.df_to_return, loop_result], axis=1,\
                                          ignore_index=True)
            print ('df_to_return:\n', self.df_to_return)
            loop_result_list.append (loop_result)
        
        return self.df_to_return
    
    def show_results (self, results_df, form = 'w'):
        '''
        Takes parameter specifying wide or narrow format. 
        Returns a copy of the private play data frame
            to the user.
        Takes a parameter to return the data frame 
            in narrow or wide form which defaults to wide form.
        The narrow form will have a MultiIndex, 
            comprising the roll number and the dienumber (in that order), 
            and a single column with the outcomes (i.e. the face rolled).
        '''

        self.form = form.lower()
        if self.form != 'w' and self.form != 'n':
            raise ValueError('form is not "w" or "n".')
        return results_df