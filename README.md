# final-project-2024
DS5100 Final Project Repo

Metadata:

Author: Bill Locke
Project: The module is 'finalproject' (a simple Monte Carlo simulator)
using a set of 3 related classes:
    1. Die class 
    2. Game class
    3. Analyzer class
    
The classes are related in the following way: 
    Game objects are initialized with a Die object, 
    and Analyzer objects are initialized with a Game object.

        [Die] → [Game] → [Analyzer]

In this simulator, a “die” can be any discrete random variable 
associated with astochastic process, such as using a deck of cards, 
flipping a coin, rolling an actual die, or speaking a language.

Synopsis: 

Show brief demo code of how the classes are used, i.e. code snippets
showing how to install, import, and use the code to (1) create dice, 
(2) play a game, and (3) analyze a game. 
You can use preformatted blocks for the code.

Import modules as follows:

    import numpy as np
    import pandas as pd
    import unittest
    import finalproject
    from die import Die
    from game import Game
    from anlyzer import Analyzer


(1) create dice
faces = np.arange (6)  # creates array
faces_df = Die(faces)

faces_df.change_weight (4, 5)

die = faces_df.create_die (faces_df)    # create die with updated weights

die_deep2 = faces_df.show_die_state (die)  # show die state

results = faces_df.roll_die(1000)   # roll die

results.value_counts()   # tally roll results

faces_df.plot_results (results)   # plot roll results

(2) play a game

faces = np.arange (6)  # creates array
faces_df1 = Die(faces) # instantiate Game objects
faces_df2 = Die(faces)

faces_df1.change_weight (4, 5)

die1 = faces_df1.create_die (faces_df1)  # create die
die2 = faces_df2.create_die (faces_df2)

die_deep1 = faces_df1.show_die_state (die1)
die_deep2 = faces_df2.show_die_state (die2)

die_list = [die1, die2]

n_rolls = 10

results1 = faces_df1.roll_die(n_rolls)
print ('results1:', results1)
faces_df1.plot_results (results1)

results1 = die1.play(n_rolls)
faces_df1.plot_results (results1)

results2 = faces_df2.roll_die(n_rolls)
faces_df2.plot_results (results2)

results_df = pd.DataFrame()
results1 = faces_df1.roll_die(n_rolls)
results_df = results_df.concat ([results1])

(3) analyze a game

*** UNDER CONSTRUCTION ***

API description: A list of all classes with their public methods and attributes. Each
item should show their docstrings. All parameters (with data types and defaults)
should be described. All return values should be described. Do not describe private
methods and attributes.

List of classes and methods - from class and method docstrings
Help on class Die in module __main__:

class Die(builtins.object)
 |  Die(faces)
 |  
 |  General Definition
 |  A die has 𝑁 sides, or “faces”, and 𝑊 weights,
 |  and can be rolled to select a face.
 |  For example, a “die” with 𝑁=2 is a coin, and
 |  a one with 𝑁=6 is a standard die.
 |  Normally, dice and coins are “fair,” meaning that the
 |  each side has an equal weight.
 |  An unfair die is one where the weights are unequal.
 |  Each side contains a unique symbol.
 |  Symbols may be all alphabetic or all numeric.
 |  𝑊 defaults to 1.0 for each face
 |  but can be changed after the object is created.
 |  The weights are just positive numbers (integers or floats, including 0),
 |  not a normalized probability distribution.
 |  The die has one behavior, which is to be rolled one or more times.
 |  Specific Methods and Attributes:
 |      1. An initializer
 |      2. Change the weight of a single side.
 |      3. Create die
 |      4. Roll die
 |      5. Show die's current state
 |  
 |  Methods defined here:
 |  
 |  __init__(self, faces)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  change_weight(self, face_to_change, new_weight)
 |      Takes two arguments: the face value to be changed and the new weight.
 |  
 |  create_die(self, faces_df)
 |      Create the die using the object's weights. Save to self as a DataFrame.
 |  
 |  plot_results(self, my_results)
 |      Show the results of rolling the dice n times with a simple bar graph.
 |  
 |  roll_die(self, number_of_rolls)
 |      takes a parameter of how many times the die is to be rolled; defaults to 1.
 |  
 |  show_die_state(self, die)
 |      A method to show the die’s current state.
 |      Returns a copy of the private die data frame.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)


Help on class Game in module __main__:

class Game(builtins.object)
 |  Game(die_list)
 |  
 |  General Definition
 |  A game consists of rolling of one or more similar dice (Die objects)
 |      one or more times.
 |  By similar dice, we mean that each die in a given game 
 |      has the same number of sides and associated faces, 
 |      but each die object may have its own weights.
 |  Each game is initialized with a Python list 
 |      that contains one or more dice.
 |  Game objects have a behavior to play a game, 
 |      i.e. to roll all of the dice a given number of times.
 |  Game objects only keep the results of their most recent play.
 |  Specific Methods and Attributes;
 |      1. An initializer
 |      2. A play method
 |      3. Show results of the most recent play
 |  
 |  Methods defined here:
 |  
 |  __init__(self, die_list)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  play(self, number_of_rolls)
 |      Takes parameter specifying how many times 
 |          the dice should be rolled. Saves result of the play
 |          to a private data frame.
 |      The data frame should be in wide format, 
 |          i.e. have the roll number as a named index, 
 |          columns for each die number 
 |          (using its list index as the column name),
 |          and the face rolled in that instance in each cell.
 |  
 |  show_game_results(self, my_results)
 |      Show the results of rolling the dice n times with a simple bar graph.
 |  
 |  show_results(self, form='w')
 |      Takes parameter specifying wide or narrow format. 
 |      Returns a copy of the private play data frame
 |          to the user.
 |      Takes a parameter to return the data frame 
 |          in narrow or wide form which defaults to wide form.
 |      The narrow form will have a MultiIndex, 
 |          comprising the roll number and the dienumber (in that order), 
 |          and a single column with the outcomes (i.e. the face rolled).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

Help on class Analyzer in module __main__:

class Analyzer(builtins.object)
 |  Analyzer(die_list)
 |  
 |  General Definition
 |  An Analyzer object takes the results of a single game and 
 |  computes various descriptive statistical properties about it.
 |  Specific Methods and Attributes:
 |      1. An initializer
 |      2. Jackpot
 |      3. Face counts per roll
 |      4. Combo_count
 |      5. Permutation count
 |  
 |  Methods defined here:
 |  
 |  __init__(self, die_list)
 |      Takes a game object as its input parameter.
 |      Throws a ValueError if the passed value is not a Game object
 |  
 |  combo_count(self)
 |      Computes the distinct combinations of faces rolled,
 |          along with their counts.
 |      Combinations are order-independent and may contain repetitions.
 |      Returns a data frame of results.
 |      The data frame should have a MultiIndex of distinct combinations
 |          and a column for the associated counts.
 |  
 |  face_counts_per_roll(self, form='w')
 |      Computes how many times a given face is rolled in each event.
 |      For example, if a roll of five dice has all sixes, 
 |          then the counts for this roll would be 
 |          for the face value ‘6’ and for the other faces.
 |      Returns a data frame of results.
 |      The data frame has an index of the roll number,
 |          face values as columns, 
 |          and count values in the cells (i.e. it is in wide format).
 |  
 |  jackpot(self, number_of_rolls)
 |      A jackpot is a result in which all faces are the same,
 |          e.g. all ones for a six-sided die.
 |      Computes how many times the game resulted in a jackpot.
 |      Returns an integer for the number of jackpots.
 |  
 |  permutation_count(self)
 |      Computes the distinct permutations of faces rolled, a
 |          long with their counts.
 |      Permutations are order-dependent and may contain repetitions.
 |      Returns a data frame of results.
 |      The data frame should have a MultiIndex of distinct permutations
 |      and a column for the associated counts.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 
 Parameters and Return Values
 
 The Die class          M) = method
                        P) = parameter
                        R) = rerturn
    M) initializer      P) faces: NumPy array of faces weights, default = 1; numeric
                        R) instantiated object
    M) change_weight    P) face_to_change; numeric / alpha depending on die type
                        P) new_weight; nume
                        R) updated weights with changed face
    M) create die       P) faces; array of faces weights
                        R) self.die; die object with faces and normalized weights
    M) roll_die         P) number_of_rolls; integer; default = 1
                        R) self.result; DataFrame of rolls results; roll #, face
    M) show_die_state   P) self.die; die object
                        R) deep copy of die object
    M) plot_results     P) self.result; DataFrame with roll results
                        R) # of times each face was thrown
                        R) plot of # of times each face was thrown

 The Game class         M) = method
                        P) = parameter
                        R) = rerturn
    M) initializer      P) dies to be played; list
                        R) instantiated die objects
    M) play             P) number_of_rolls; integer
                        R) roll results for each die; dataframe
    M) show_results     P) format; alpha ‘n’ or ‘w’ (default)
                        R) DataFrame of rolls, count_per_face in specified format
    M)show_game_results P) results DataFrame of results
                        R) plot of results
                        
 The Analyzer class     M) = method
                        P) = parameter
                        R) = rerturn
    M) initializer      P) die_list; list of die objects to analyze
                        R) instantiated die objects
    M) jackpot          P) number_of_rolls; integer <- TBR
                        R) number_of_jackpots; integer
    M) face_counts      P) format; alpha <- TBR
                        R) # times each face thrown per roll <- DataFrame
    M) combo            P) results DataFrame
                        R) # of times each result combination was thrown
    M) permutation      P) results DataFrame
                        R) # of times each result permutation was thrown