class Sport():
    def __init__(self, event, entry):
        self.event = event
        self.entry = entry
    # end def __init__

    def getEntry(self):
        return self.entry + '명'
    # end def team

    def showinfo(self):
        print(f'종목 : {self.event}')
        print(f'엔트리 : {self.entry}명')
    # end def
# end class Sport

class BaseBall(Sport):
    def __init__(self, event, entry, hit):
        super().__init__(event, entry)
        self.hit = hit
    # end def __init__

    def showinfo(self):
        super().showinfo()
        print(f'타율 : {self.hit:.6f}')
    # end showinfo
# end class BaseBall

class FootBall(Sport):
    def __init__(self, event, entry, goal):
        super().__init__(event, entry)
        self.goal = goal
    # end def __init__
    def showinfo(self):
        super().showinfo()
        print('골 수 : ' + str(self.goal))
    # end showinfo
# end class FootBall

baseball = BaseBall('야구',9,0.235000)
baseball.showinfo()
print('-'*30)

football = FootBall('축구',11,5)
football.showinfo()
print('-'*30)

