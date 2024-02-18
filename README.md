# Agent_RedBlue
Problem Statement:

The provided Python script implements a game called Red-Blue Nim, which is a two-player game involving the strategic removal of marbles from two piles: a red pile and a blue pile. The game is played in turns, with players selecting a pile and removing a marble from it. The player who removes the last marble wins the game.

The objective of this project is to enhance the existing Red-Blue Nim game implementation by incorporating artificial intelligence (AI) to serve as an opponent for human players. The AI opponent should be capable of making strategic decisions to maximize its chances of winning the game against a human player.

The key components of this project include:

Game Initialization: The game starts with a specified number of marbles in the red and blue piles, as provided by the user through command-line arguments.
Game Loop: Players take turns removing marbles from the piles until one of the piles becomes empty.
AI Opponent: Implement the Minimax algorithm with alpha-beta pruning to create an AI opponent capable of making optimal decisions during its turn. The AI opponent should analyze the current state of the game and select the best move to maximize its chances of winning.
User Interaction: Allow the human player to input their moves by choosing a pile (red or blue) to remove a marble from. Ensure that the input is validated to prevent invalid moves.
Game Outcome: Determine the winner of the game based on the final state of the piles and display the corresponding scores.
Command-Line Interface: Enable the game to be run from the command line, allowing users to specify parameters such as the initial number of marbles in each pile, the starting player, and the depth of the Minimax algorithm.
By completing this project, you will have created an interactive Red-Blue Nim game with an AI opponent capable of providing a challenging gameplay experience for human players. Additionally, you will gain experience in implementing and optimizing game-playing algorithms using Minimax with alpha-beta pruning.


Evaluation function:

Getting the sum of total score and also the difference in scores would give us the evlauation of the function.

Code structure:

We have defined the evaluation function for returning the utility value of the player
Defined the min-max function with alpha-beta pruning and returning the utility value and best move
Later, we define the initial game state and also defined the steps to be taken for human and computer
Later we calculated the scores and also determined the winner and display the score.


TO RUN THE SCRIPT:

Download the red_blue_nim.py file to your local PC and open in sublime text editor

Right Click and select 'Open Terminal Here' option

Then we are prompted with the command line(Windows Powershell) and pass the arguments respectively as shown below:

python red_blue_nim.py 4 2  
The above invocation takes computer as default player and depth as default 3 


python red_blue_nim.py 5 5 'human'
gives human the first chance to play.

