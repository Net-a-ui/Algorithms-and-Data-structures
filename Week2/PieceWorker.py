# Juvenal Nava
# Programming Assignment 2

from Employee import Employee

class PieceWorker(Employee):

    def __init__(self, id_num = 0, first_name = "no data", last_name = "no data",
                 wage_per_piece = 0.0, quantity = 0):
        super().__init__(id_num, first_name, last_name)
        self.wage_per_piece = wage_per_piece
        self.quantity = quantity

    def setData(self, id_num = 0, first_name = "no data", last_name = "no data",
                wage_per_piece = 0.0, quantity = 0):
        super().setData(id_num, first_name, last_name)
        self.wage_per_piece = wage_per_piece
        self.quantity = quantity

    def setWagePerPiece(self, wage_per_piece = 0.0):
        self.wage_per_piece = wage_per_piece

    def setQuantity(self, quantity = 0):
        self.quantity = quantity

    def getWagePerPiece(self):
        return self.wage_per_piece

    def getQuantity(self):
        return self.quantity

    def displayData(self):
        return super().getData() + " %.2f %d" % (
            self.wage_per_piece, self.quantity)

    def earnings(self):
        weekly_pay = self.wage_per_piece * self.quantity
        return "%-18s %s %10.2f" % (
            "Piece Worker", super().getData(), weekly_pay)
