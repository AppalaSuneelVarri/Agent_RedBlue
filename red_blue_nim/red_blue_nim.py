import sys
from math import inf

def red_blue_nim(num_red, num_blue, first_player='human', depth=3):
    # define evaluation function
    def evaluate(state):
        red_score = 2 * state[0]
        blue_score = 3 * state[1]
        score= red_score + blue_score
        return score if first_player else -score
        variation = abs(red_score - blue_score)
        score = red_score * 2 + blue_score * 3
        if first_player:
            return score + variation
        else:
            return -score - variation

    
    # define min-max function with alpha-beta pruning
    def min_max(state, depth, alpha, beta, maximizing_player):
        if depth == 0 or state[0] == 0 or state[1] == 0:
            return evaluate(state), None
        
        if maximizing_player:
            value = -inf
            best_move = None
            for i in range(2):
                if state[i] > 0:
                    new_state = list(state)
                    new_state[i] -= 1
                    current_value, _ = min_max(new_state, depth-1, alpha, beta, False)
                    if current_value > value:
                        value = current_value
                        best_move = i
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
            return value, best_move
        
        else:
            value = inf
            best_move = None
            for i in range(2):
                if state[i] > 0:
                    new_state = list(state)
                    new_state[i] -= 1
                    current_value, _ = min_max(new_state, depth-1, alpha, beta, True)
                    if current_value < value:
                        value = current_value
                        best_move = i
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
            return value, best_move
    
    # initialize game state
    state = [num_red, num_blue]
    current_player = first_player
    
    # game loop
    while True:
        if state[0] == 0 or state[1] == 0:
            break
        
        if current_player == 'computer':
            _, move = min_max(state, depth, -inf, inf, True)
            pile = 'red' if move == 0 else 'blue'
            state[move] -= 1
            print(f"Computer removes 1 marble from {pile} pile")
        
        else:
            valid_input = False
            while not valid_input:
                pile = input("Enter pile to remove from (red or blue): ")
                if pile == 'red' and state[0] > 0:
                    valid_input = True
                    state[0] -= 1
                elif pile == 'blue' and state[1] > 0:
                    valid_input = True
                    state[1] -= 1
                else:
                    print("Invalid input, try again")
        
        current_player = 'computer' if current_player == 'human' else 'human'
    
    # calculate final scores
    computer_score = evaluate(state) if current_player == 'computer' else -evaluate(state)
    human_score = evaluate(state) if current_player == 'human' else -evaluate(state)
    
    # determine winner and display score
    if computer_score > human_score:
        print(f"Computer wins with a score of {computer_score}!")
    elif human_score > computer_score:
        print(f"Human wins with a score of {human_score}!")
    else:
        print("It's a tie!")

# accept command-line arguments
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("File should be called as python red_blue_nim.py [num_red] [num_blue] [first_player=computer] [depth=3]")
        sys.exit(1)
    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    first_player = 'computer' if len(sys.argv) < 4 else sys.argv[3]
    depth = 3 if len(sys.argv) < 5 else int(sys.argv[4])

    red_blue_nim(num_red, num_blue, first_player, depth)
