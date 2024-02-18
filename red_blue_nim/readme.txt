Programming language : Python 3.11.1


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

