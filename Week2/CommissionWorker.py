from Employee import Employee

class CommissionWorker(Employee):

    def __init__(self, id_num = 0, first_name = "no data", last_name = "no data",
                 salary = 0.0, comm_rate = 0.0, sales = 0.0):
        super().__init__(id_num, first_name, last_name)
        self.salary = salary
        self.comm_rate = comm_rate
        self.sales = sales

    def setData(self, id_num = 0, first_name = "no data", last_name = "no data",
                salary = 0.0, comm_rate = 0.0, sales = 0.0):
        super().setData(id_num, first_name, last_name)
        self.salary = salary
        self.comm_rate = comm_rate
        self.sales = sales

    def setSalary(self, salary = 0.0):
        self.salary = salary

    def setCommRate(self, comm_rate = 0.0):
        self.comm_rate = comm_rate

    def setSales(self, sales = 0.0):
        self.sales = sales

    def getSalary(self):
        return self.salary

    def getCommRate(self):
        return self.comm_rate

    def getSales(self):
        return self.sales

    def displayData(self):
        return super().getData() + " %.2f %.3f %.2f" % (
            self.salary, self.comm_rate, self.sales)

    def earnings(self):
        weekly_pay = (self.salary / 52) + (self.sales * self.comm_rate)
        return "%-18s %s %10.2f" % (
            "Commission Worker", super().getData(), weekly_pay)
