class de:
    def __init__(self,pyspark,sql,python):
        self.pyspark = "repartition,coalesce"
        self.sql = "window"
        self.python = "very imp"

    def crack(self):
        if self.sql != "cte":
            print("can not crack de interview")
        else:
            self.sql = "cte"
            self.python = "dsa"

    def de_info(self):
        print(f" to crack de interview {self.python} and {self.sql} and {self.pyspark} ")

de1  =  de("a","b","c")
de1.de_info()
de1.crack()






