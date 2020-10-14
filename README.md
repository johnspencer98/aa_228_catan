# aa_228_catan

Hello, \
This repo contains the Catan AI project for Stanford's AA228. The game of Catan is heavily modified as the focus of the 
project is decision making and training our algorithms.

As a quick summary that has been done:  

**The Modified Game Board** 

The key components in Catan are the players, the tiles,
the edges (which can become roads), and the vertices (which cah become)
settlements or cities). The core functionality that is currently built into the game
is 4 tiles, that create 9 vertices connected by 12 edges.
The dice being used is only a four sided dice and each tile gets either a 1, 2, 3, or 4 to correspond to a certain dice roll. For
resource cards we are using a modified version where there only exists wood and brick, and a user can buy
settlements, cities and roads using different combinations of wood and brick resources. 

![Board Start](/images/board_start.png)

**The Modified Rules** 

As mentioned previously mentioned, players can buy all items in the game with only wood and brick. Furthermore, players in the four-tile version of Catan currently can place settlements 
adjacent to other settlements (in the regular game you need two edges of separation). And lastly, in the modified version we are playing
only to 5 victory points - currently there is no way to get victory points outside of building new settlements

**The Modified Player**

This version of Catan is strictly for evaluating AI performance and so there is no options to play, only options to simulate how different AI would play against eachother.
Currently there are two types of AI plays which can play against eachother: a random player which makes decisions purely based off chance, and a greedy player which makes decisions based off of simple heuristics to optimize for short term gain.

**What's Next**

In our final version, we will hopefully have a successful implementation of a new AI that is trained using Q-Learning


