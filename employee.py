"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from multiprocessing.spawn import prepare


class Employee:
    def __init__(self, name, perPayAmount):
        self.name = name
        self.perPayAmount = perPayAmount

    def getRegularPay(self):
        return self.perPayAmount

    def get_pay(self):
        return self.getRegularPay()

    def __str__(self):
        return self.name

    def getBonusComm(self, bonusAmount):
        return bonusAmount
    
    def getContractComm(self, contractCommissionAmount, contractNumber):
        return contractCommissionAmount*contractNumber

    def str(self):
        pass
    

class salaryEmployee(Employee):
    def __init__(self, name, perPayAmount):
        super().__init__(name, perPayAmount)
    def str(self):
        return (self.name + ' works on a monthly salary of ' + str(self.perPayAmount) + '. Their total pay is ' + str(self.get_pay()) + '.')


class salaryBonusEmployee(salaryEmployee):
    def __init__(self, name, perPayAmount, bonusAmount):
        super().__init__(name, perPayAmount)
        self.bonusAmount = bonusAmount

    def get_pay(self):
        return super().getRegularPay() + super().getBonusComm(self.bonusAmount)
        
    def str(self):
        return (self.name + ' works on a monthly salary of ' + str(self.perPayAmount) + '. Their total pay is ' + str(self.get_pay()) + '.')

class salaryContractEmployee(salaryEmployee):
    def __init__(self, name, perPayAmount, contractCommissionAmount, contractNumber):
        super().__init__(name, perPayAmount)
        self.contractCommissionAmount = contractCommissionAmount
        self.contractNumber = contractNumber

    def get_pay(self):
        return super().getRegularPay()+super().getContractComm(self.contractCommissionAmount, self.contractNumber)

    def str(self):
        return (self.name + ' works on a monthly salary of '+ str(self.perPayAmount) + ' and receives a commission for '
        + str(self.contractNumber) + ' contract(s) at '+ str(self.contractCommissionAmount) + '/contract. Their total pay is ' + str(self.get_pay()) + '.')


class hourlyEmployee(Employee):
    def __init__(self, name, perPayAmount, hour):
        super().__init__(name, perPayAmount)
        self.hour = hour

    def getRegularPay(self):
        return self.perPayAmount*self.hour

    def get_pay(self):
        return super().getRegularPay()*self.hour

    def str(self):
        return (self.name + ' works on a contract of ' + str(self.hour) + ' at ' + str(self.perPayAmount) + 
        '/hour. Their total pay is ' + str(self.get_pay()) + '.')


class hourlyBonusEmployee(hourlyEmployee):
    def __init__(self, name, perPayAmount, hour, bonusAmount):
        super().__init__(name, perPayAmount, hour)
        self.bonusAmount = bonusAmount

    def get_pay(self):
        return super().getRegularPay()+self.bonusAmount

    def str(self):
        return (self.name + ' works on a contract of ' + str(self.hour) + ' at ' + str(self.perPayAmount) 
        + '/hour and receives a bonus commission of ' + str(self.bonusAmount) + '. Their total pay is ' + str(self.get_pay()) + '.')


class hourlyContractEmployee(hourlyEmployee):
    def __init__(self, name, perPayAmount, hour, contractCommissionAmount, contractNumber):
        super().__init__(name, perPayAmount, hour)
        self.contractCommissionAmount = contractCommissionAmount
        self.contractNumber = contractNumber

    def get_pay(self):
        return super().getRegularPay()+super().getContractComm(self.contractCommissionAmount, self.contractNumber)

    def str(self):
        return (self.name + ' works on a contract of ' + str(self.hour) + ' at ' + str(self.perPayAmount)
        + '/hour and receives a commission for ' + str(self.contractNumber) + ' contract(s) at ' + str(self.contractCommissionAmount)
        + '/contract. Their total pay is ' + str(self.get_pay()) + '.')



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = salaryEmployee('Billie', 4000)
print(billie.get_pay())
print(billie.str())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = hourlyEmployee('Charlie', 25, 100)
print(charlie.get_pay())
print(charlie.str())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = salaryContractEmployee('Renee', 3000, 200, 4)
print(renee.get_pay())
print(renee.str())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = hourlyContractEmployee('Jan', 25, 150, 220, 3)
print(jan.get_pay())
print(jan.str())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = salaryBonusEmployee('Robbie', 2000, 1500)
print(robbie.get_pay())
print(robbie.str())


# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = hourlyBonusEmployee('Ariel', 30, 120, 600)
print(ariel.get_pay())
print(ariel.str())

