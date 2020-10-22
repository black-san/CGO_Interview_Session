def computeEarliestTime( X, A ):
    ''' PARAMS:
                X - the position that the frog need to jump to
                A - the sequence of the falling of leaves A[k] is the position by K is the time that this position
                was covered by leaves
        RETURN:
                -1 - if there is no way that frog can jump across the river
                else - return the minimum time that frog spends to jump across the river
    '''
    
    #   list all positions that is the way to jump to the opposite side
    steps = list(range(1, X + 1))

    #   check if the number of steps that need to jump and the sequence of the falling of leaves are less than 1
    #   return -1 to notice that a frog cannot cross to the opposite side
    if X < 1 or len(A) < 1:
        return -1
    
    #   set the initial earliest time is -1
    time = -1

    #   loop in steps from 1 to N
    for element in steps:

        #   check if the current step is in the falling sequnce
        if element in A:
            
            #   check if this position was covered by leaves later than the previous position
            if A.index(element) > time:

                #   set the earliest time to be equal to the time (second) that this position was covered by leaves
                time = A.index(element)
        
        #   if there is a step that is not contain in the falling sequence, it means this position has not cover by any leave
        else: return -1

    #   return the time that all positions were covered by leaves
    return time    