import psutil


class RAM:
    def __init__(self):
        self.memory = psutil.virtual_memory()

    def Percent(self):
        return self.memory[2]

    def Total(self, value="b"):
        value = value.lower()

        mem = self.memory[0]

        if value == "kb":
            mem = mem / 1024
        if value == "mb":
            mem = mem / 1048576
        if value == "gb":
            mem = mem / 1073741824
        mem = round(mem, 2)

        return mem

    def Used(self, value="b"):
        value = value.lower()

        mem = self.memory[3]

        if value == "kb":
            mem = mem / 1024
        if value == "mb":
            mem = mem / 1048576
        if value == "gb":
            mem = mem / 1073741824
        mem = round(mem, 2)

        return mem

    def Free(self, value="b"):
        value = value.lower()

        mem = self.memory[4]

        if value == "kb":
            mem = mem / 1024
        if value == "mb":
            mem = mem / 1048576
        if value == "gb":
            mem = mem / 1073741824
        mem = round(mem, 2)

        return mem
