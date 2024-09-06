import GPUtil


class GPU:
    def __init__(self):
        gpus = GPUtil.getGPUs()
        self.gpu = gpus[0]

    def LoadPercent(self):
        return self.gpu.load * 100

    def MemUsagePercent(self):
        return self.gpu.memoryUtil * 100

    def Temp(self):
        return self.gpu.temperature

    def FreeMem(self, value="mb"):
        value = value.lower()
        mem = self.gpu.memoryFree

        if value == "gb":
            mem = mem / 1024
        return mem

    def UsedMem(self, value="mb"):
        value = value.lower()
        mem = self.gpu.memoryUsed

        if value == "gb":
            mem = mem / 1024
        return mem

    def TotalMem(self, value="mb"):
        value = value.lower()
        mem = self.gpu.memoryTotal

        if value == "gb":
            mem = mem / 1024
        return mem
