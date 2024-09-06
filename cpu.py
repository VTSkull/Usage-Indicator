import psutil


class CPU:
    def __init__(self):
        pass

    @staticmethod
    def Percents():
        percentages = []
        for percentage in psutil.cpu_percent(percpu=True, interval=1):
            percentages.append(percentage)
        return percentages

    def TotalPercent(self):
        total = 0
        num = 0

        for x in self.Percents():
            total += x
            num += 1

        total = total/num
        return total