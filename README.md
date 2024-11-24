# final-project-2024
DS5100 Final Project Repo

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
stochastic process, such as using a deck of cards, flipping a coin, rolling an actual die,
or speaking a language.