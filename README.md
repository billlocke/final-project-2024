# final-project-2024
DS5100 Final Project Repo

Metadata:

Author: Bill Locke
Project: DS5100 Final Project

The module is a simple Monte Carlo simulator using a set of 3 related
classes:
    1. Die class 
    2. Game class
    3. Analyzer class
    
The classes are related in the following way: Game objects are initialized with a Die
object, and Analyzer objects are initialized with a Game object.

    [Die] → [Game] → [Analyzer]

In this simulator, a “die” can be any discrete random variable associated with a
stochastic process, such as using a deck of cards, flipping a coin, rolling an actual die, or speaking a language.

Metadata: Specify your name and the project name (i.e. Monte Carlo Simulator).

Synopsis: 

Show brief demo code of how the classes are used, i.e. code snippets
showing how to install, import, and use the code to (1) create dice, (2) play a game,
and (3) analyze a game. You can use preformatted blocks for the code.

    The following are how Die class methods are called:
    
    faces = np.arange (6)  # creates array
    faces_df = Die(faces)

    faces_df.change_weight (4, 5)

    die = faces_df.create_die (faces_df)    # create die with updated weights

    print ('show die state with method call:')
    die_deep2 = faces_df.show_die_state (die)

    results = faces_df.roll_die(10)
    faces_df.plot_results (results)







API description: A list of all classes with their public methods and attributes. Each
item should show their docstrings. All parameters (with data types and defaults)
should be described. All return values should be described. Do not describe private
methods and attributes.