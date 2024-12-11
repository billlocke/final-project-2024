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
            
        ### play PSEUDO CODE:
        
        # loop through items in list - for loop
        # roll die for each of the die

        loop_result_list = []    # contains each die's roll result
        self.df_to_return = pd.DataFrame (index = range(len(self.die_list)))
        self.df_to_return.index.name = 'Roll#'
        
        for i in range(len(self.die_list)):    # roll each die
            loop_result = self.die_list[i].roll_die(number_of_rolls)
#            print ('loop_result type:', type (loop_result))
            
#            df_to_return = loop_result
            
            self.df_to_return = pd.concat ([self.df_to_return, loop_result], axis=1,\
                                          ignore_index=True)
            print ('df_to_return:\n', self.df_to_return)
            loop_result_list.append (loop_result)
        
#        results_df1 = pd.concat ([results2,results1], axis=1)

#        print ('length of loop_result_list in play:', len(loop_result_list))
#        print ('loop_result_list in play:\n', loop_result_list)

        '''# NEW CODE
        
        print ('loop_result_list type:', type(loop_result_list))
        df_to_return = pd.DataFrame (loop_result_list, columns=['Die', 'Roll', 'Face'])
        print ('df_to_return type:', type(df_to_return))   
        return df_to_return
    
        # END NEW CODE'''
        
#        self.results1 = self.die_list.roll_die(number_of_rolls)
#        print ('rolled die:') 
#        print ('results:', self.results1)
#        print ('results_list in play:\n', loop_result_list)

        ### END PSEUDO CODE

    def show_results (self, form = 'w'):
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
        if self.form != 'w' or self.form != 'n':
            raise ValueError('form is not "w" or "n".')
        return

        # stack loop_result_list
    
        # verify faces is type (np.ndarray); TypeError if not
        if not isinstance (self.faces, np.ndarray):
            raise TypeError('faces is not an np array')

        # Tests to see if the values are distinct; ValueError if not
        if len(self.faces) != len(set(self.faces)):    # 'set' values are unique
            raise ValueError('faces are not unique')
            # NOTE: faces = np.unique (faces) removes "redundant" values        

        # Internally initializes the weights to 1.0 for each face.
        self.weights = np.ones(len(self.faces))
        #print (faces, weights)

        # Saves both faces and weights in a private data frame
        #   with faces in the index.
        index_values = [self.faces]
        self.faces_df = pd.DataFrame({'weights': self.weights}, index=index_values)

    def show_game_results(self, my_results):
        '''Show the results of rolling the dice n times with a simple bar graph.'''
        my_results.value_counts().sort_index().plot.bar(rot=0);
        # A method to show the die’s current state.
        #  Returns a copy of the private die data frame.