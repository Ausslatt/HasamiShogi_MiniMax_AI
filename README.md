# Hasami Shogi with MiniMax algorithm

This is a variant of the Japanese game Shogi, or Japanese chess. I am currently working on optimizing the game
logic before adding the AI. The final product will allow a human player to face the MiniMax algorithm using some
super fancy hueristic function.

---

## Usage:

To use this program you simply run main.py and the game will be played on the command line.

## Future improvements

### Hueristic

The efficacy of the minimax algorithm depends a lot on the quality of the evaluation function given to it. Currently, the program uses the most basic evaluation function optimizing for captured pieces. In future updates this will be optimized to a more sophisticated scoring function.

### Memory Efficiency

The current implementation performs its search on deep copies of the Shogi Game object. Adding functions to reverse moves on a single object would allow for increased search depth and therefore a smarter AI. 

### GUI

A better GUI could be made to make for a better user experience since at present the game is displayed on the command line.

### Human Players

The next step is to add the ability for a human player to face off against the minimax algo. Presently and only for demonstration purposes I have a "random" player facing off against the AI. While this is a baseline demonstration of the AI its hard to get a sense of the AI's capability. 

### Scoring Metrics

Adding the ability to track improvements on algorithm parameter changes would be useful in scoring the efficiency of the model. Some metrics could include number of moves made per win or numbers of moves made between capture moves. 






 





