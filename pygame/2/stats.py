class Stats():

    """отслеживание статистики"""

    def __init__(self):

        """ициализирует статистику"""

        self.resert_stats()
        self.run_game=True
        with open('pygame/2/highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def resert_stats(self):

        """статистика,изменяющаяся во время игры"""

        self.guns_left=2
        self.score=0












































