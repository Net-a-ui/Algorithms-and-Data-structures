'''
Employee base class
'''

class Employee():

    def __init__(self, id_num = 0, first_name = "no data", last_name = "no data"):
        self.id_num = id_num
        self.first_name = first_name
        self.last_name = last_name

    def setData(self, id_num = 0, first_name = "no data", last_name = "no data"):
        self.id_num = id_num
        self.first_name = first_name
        self.last_name = last_name

    def setId(self, id_num = 0):
        self.id_num = id_num

    def setFirstName(self, first_name = "no data"):
        self.first_name = first_name

    def setLastName(self, last_name = "no data"):
        self.last_name = last_name

    def getId(self):
        return self.id_num

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getData(self):
        return "%-6d %-15s %-15s" % (self.id_num, self.first_name, self.last_name)

    def earnings(self):
        return 0
