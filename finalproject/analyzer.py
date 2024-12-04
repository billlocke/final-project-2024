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
        
        ### jackpot PSEUDO CODE:
        
        Input is DataFrame with roll # index, 
            and column for each Die result (face):
        
                Die1 Die2 Die3
        roll #
            1     6    4    3
            2     1    3    3
            3     4    5    1
            4     1    1    1
            5     6    2    5
            
        jackpot_number = 0
        For each roll n
            if Die1 face == Die2 face == Die3 face
                jackpot_number += 1
        return jackpot_number

        loop_result_list = []    # contains each die's roll result
        for i in range(len(self.die_list)):
            loop_result = self.die_list[i].roll_die(number_of_rolls)
            loop_result_list.append (loop_result)
            
        print ('length of loop_result_list:', len(loop_result_list))
        print ('loop_result_list:', loop_result_list)
            
        self.results1 = self.die_list.roll_die(number_of_rolls)
        print ('rolled die:') 
        print ('results:', self.results1)

        ### END jackpot PSEUDO CODE
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
           
        ### face_counts_per_roll PSEUDO CODE:
        
        Input is DataFrame with roll # index, 
            and column for each Die result (face):
        
                Die1 Die2 Die3
        roll #
            1     6    4    3
            2     1    3    3
            3     4    5    1
            4     1    1    1
            5     6    2    5

        For each roll n
            all die_face_count in row <- 0
            for each Die_n_value
                face_count[Die_n_value] += 1
        return results_data_frame (below)

        Results DataFrame
                Face1 Face2 Face3 Face4 Face5 Face6
        roll #
            1     0     0     1     1     0     1
            2     1     0     2     0     0     0
            3     1     0     0     1     1     0
            4     3     0     0     0     0     0
            5     0     1     0     0     1     1
                
        ### END face_counts_per_roll PSEUDO CODE

        '''
        
    def combo_count (self, ):
        '''
        Computes the distinct combinations of faces rolled,
            along with their counts.
        Combinations are order-independent and may contain repetitions.
        Returns a data frame of results.
        The data frame should have a MultiIndex of distinct combinations
            and a column for the associated counts.
        
        ### combo_count PSEUDO CODE:
        
        Input is DataFrame with roll # index, 
            and column for each Die result (face):
        
                Die1 Die2 Die3
        roll #
            1     6    4    3
            2     1    3    3
            3     4    5    1
            4     1    1    1
            5     6    2    5
            6     1    5    4

        face_values_list = []
        For each roll n
            populate roll_list with roll's face values
            sort (face_values)
            append roll_list to face_values_list
        sort (face_value_list)

        face_values_list DataFrame:

        roll_list before sorting
        roll #
            1  [3, 4, 6]
            2  [1, 3, 3]
            3  [1, 4, 5]
            4  [1, 1, 1]
            5  [2, 5, 6]
            6  [1, 4, 5]
            
        roll_list after sorting
        roll #
            4  [1, 1, 1]
            2  [1, 3, 3]
            3  [1, 4, 5]
            6  [1, 4, 5]
            5  [2, 5, 6]
            1  [3, 4, 6]
        
        face_value_list = ['roll_list', 'count']
        for i in range(len(row_list))
            if row_list[i] not in face_value_list
                add row_list[i] to face_values_list[0]
                count[i] <- 1
            else count[i] += 1
        return face_values_list
        
        combo_list dataframe:
        
        roll_list  count
        [1, 1, 1]    1
        [1, 3, 3]    1
        [1, 4, 5]    2
        [2, 5, 6]    1
        [3, 4, 6]    1
                 

        ### END combo_count PSEUDO CODE
        '''

        
    def permutation_count (self, ):
        '''
        Computes the distinct permutations of faces rolled, a
            long with their counts.
        Permutations are order-dependent and may contain repetitions.
        Returns a data frame of results.
        The data frame should have a MultiIndex of distinct permutations
        and a column for the associated counts.

        ### permutation_count PSEUDO CODE:
        
        Input is DataFrame with roll # index, 
            and column for each Die result (face):
        
                Die1 Die2 Die3
        roll #
            1     6    4    3
            2     1    3    3
            3     4    5    1
            4     1    1    1
            5     6    2    5
            6     1    5    4
            7     1    3    3

        face_values_list = []
        For each roll n
            populate roll_list with roll's face values
            sort (face_values)
            append roll_list to face_values_list
        sort (face_value_list)

        face_values_list DataFrame:

        roll_list before sorting
        roll #
            1  [6, 4, 3]
            2  [1, 3, 3]
            3  [4, 5, 1]
            4  [1, 1, 1]
            5  [6, 2, 5]
            6  [1, 5, 4]
            7  [1, 3, 3]
            
        roll_list after sorting
        roll #
            4  [1, 1, 1]
            2  [1, 3, 3]
            7  [1, 3, 3]
            6  [1, 5, 4]
            3  [4, 5, 1]
            5  [6, 2, 5]
            1  [6, 4, 3]
        
        face_value_list = ['roll_list', 'count']
        for i in range(len(row_list))
            if row_list[i] not in face_value_list
                add row_list[i] to face_values_list[0]
                count[i] <- 1
            else count[i] += 1
        return face_values_list
        
        permutation_list dataframe:
        
        roll_list  count
        [1, 1, 1]    1
        [1, 3, 3]    2
        [1, 5, 4]    1
        [4, 5, 1]    1
        [6, 2, 5]    1
        [6, 4, 3]    1
                 

        ### END permutation_count PSEUDO CODE
        '''
                
        self.form = form.lower()
        if self.form != 'w' or self.form != 'n':
            raise ValueError('form is not "w" or "n".')
        return

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
