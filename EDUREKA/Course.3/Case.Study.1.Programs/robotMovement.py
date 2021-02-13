class robotMovement:

    def track_Movement(movements):
        l = len(movements)
        countUp, countDown, countLeft, countRight = (0,)*4
        for i in range(l):
            if (movements[i] == 'U'):
                countUp += 1
            elif (movements[i] == 'D'):
                countDown += 1
            elif (movements[i] == 'R'):
                countRight += 1
            elif (movements[i] == 'L'):
                countLeft += 1
        print('Final Postion : ' + '(' + str(countRight - countLeft) + ',' + str(countUp - countDown) + ')')
    
    if __name__ == "__main__":
        track_Movement('UUUUUDDDLLLRR')
