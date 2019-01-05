'''
Includes code to read a set of files that have pieces based on a
particular raagam and generate its finite-state-machine
transition probability representation

Author: Madhavun Candadai
Created: Jan 2018
'''
import sys,os
import numpy as np
from config import config

def generate_fsm(raagam):
    '''
    This function computes the finite-state-machine transition matrix for a raagam
    It reads all dat files (musical pieces) in that raagam's associated folder and
    produces a fsm for each file as well as the generic fsm for the raagam

    ARGS:
    raagam: string - name of the raagam

    SAVES:
    transition_probs: ND-array - transition probabilities across all files given
    piecewise_transition_probs: list - with ND-array transition probabilities for each file
    '''

    # read list of unique notes associated with the raagam
    try:
        unotes = list(np.load(config['RAAGAM_BASEPATH']+raagam.lower()+'/metadata.npy'))
    except:
        raise Exception("Raagam metadata (Aarohanam and Avarohanam) is not available - "+config['RAAGAM_BASEPATH']+raagam.lower()+'/metadata.npy')

    # get list of files to process
    filenames = []
    for filename in os.listdir(config['RAAGAM_BASEPATH']+raagam.lower()):
        if filename[-3:] == 'dat':
            filenames.append(config['RAAGAM_BASEPATH']+raagam.lower()+'/'+filename)

    # transition probs for each piece
    piecewise_transition_probs = []

    for filename in filenames:
        print('Processing '+filename+'.......',end='',flush=True)

        # creating frequency matrix for this piece - start with an equiprobable matrix
        p_transition_probs = np.ones((len(unotes),len(unotes)))

        for line in open(filename):
            print(line)
            if len(line) > 0:
                line.strip()
                # Counting note transitions÷
                prev_note = ',' # start with a blank note
                for p_note in line[:-1].split(' '):
                    if len(p_note) > 0:
                        try:
                            toInd = unotes.index(p_note)
                            fromInd = unotes.index(prev_note)
                            p_transition_probs[fromInd,toInd] += 1
                        except:
                            print('\nNote incompatible with raagam found:'+p_note+", ignoring note")
                        if p_note == ',': pass # retain preivous note on sustain
                        else: prev_note = p_note # update previous note to current note if it was not sustain

        # convert frequencies to probabilities
        ps = np.sum(p_transition_probs,1)
        ps[np.where(ps==0)] = .1
        p_transition_probs = np.transpose(np.transpose(p_transition_probs)/ps) #len(piece.split(' '))
        piecewise_transition_probs.append(p_transition_probs)
        print('done')

    # transition probabilities matrix between the unique notes in the piece
    transition_probs = np.zeros((len(unotes),len(unotes)))
    # computing generic transition_probs from piecewise_transition_probs
    for transition_prob in piecewise_transition_probs:
        transition_probs += transition_prob
    transition_probs /= len(filenames)

    # saving generic and file specific transition_probs
    np.save(config['RAAGAM_BASEPATH']+raagam+'/'+raagam+'_fsm.npy',transition_probs)
    for p_ind,p_fsm in enumerate(piecewise_transition_probs):
        np.save(filenames[p_ind][:-3]+'_fsm.npy',p_fsm)



if __name__ == "__main__":
    assert len(sys.argv) == 2, "Requires raagam name to process"
    raagam = sys.argv[1]
    generate_fsm(raagam)
