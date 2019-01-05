# Carnatic_FSM

A generative model for Indian Carnatic music using Finite State Machines. While, obviously, more sophisticated models could be built for generating (Indian classical) music, it is worth noting that this non-neural-network based approach is a plausible baseline at the very least.

Blog post explaining the approach - [Coming soon]

To try, install Music21 using pip and then from carnatic_fsm/carnatic_fsm run

    python simulate_fsm.py abhogi aadi

This would simulate a pre-generate finite state machine for *abhogi raagam* set to *aadi taalam's* rhythm, and generate a midi file to listen to and also the musical score (requires museScore to be installed). Comment out line 101 in simulate_fsm.py if you just want the midi output.

## Sample generated music
Music generated using this model based in *abhogi raagam* is available [here](http://pages.iu.edu/~madcanda/carnatic_fsm/simulated_abhogi.mp3)

## Music library
This repo uses [Music21](http://web.mit.edu/music21/) to programatically construct the musical piece and save it as a score as well as in midi format.


### Resources
http://web.mit.edu/music21/doc/about/what.html  
http://www.hitxp.com/keyboard-music-notes/western-notations-guide-convert-classical-indian-carnatic/  
http://www.mtosmt.org/issues/mto.15.21.4/schachter_examples.pdf  
