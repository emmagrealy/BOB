class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def highest(self):
        return max(self.scores)

    def top(self):
        return sorted(self.scores)[-1:-4:-1]

    def report(self):
        pass
        if self.scores[-1] >= max(self.scores):
            return "Your latest score was 70. That's your personal best!"
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(self.scores[-1],
                                                                                             max(self.scores) -
                                                                                             self.scores[-1])


#Manage a game player's High Score list.
#Your task is to build a high-score component of the classic Frogger game, one of the highest selling 
#and addictive games of all time, and a classic of the arcade era. Your task is to write methods that 
#return the highest score from the list, the last added score, the three highest scores, 
#and a report on the difference between the last and the highest scores.