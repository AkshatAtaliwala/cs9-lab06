class Apartment:
    def __init__(self, rent = 0.0, metersFromUCSB = 0, condition = 0):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def __eq__(self, other):
        if self.getApartmentDetails() == other.getApartmentDetails():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.rent < other.rent:
            return True
        elif not(self.rent < other.rent) and not(other.rent < self.rent):
            if self.metersFromUCSB < other.metersFromUCSB:
                return True
            elif not(self.metersFromUCSB < other.metersFromUCSB) and not(other.metersFromUCSB < self.metersFromUCSB):
                if self.condition > other.condition:
                    return True
        return False

    def __gt__(self, other):
        if self.rent > other.rent:
            return True
        elif self.rent == other.rent:
            if self.metersFromUCSB > other.metersFromUCSB:
                return True
            elif self.metersFromUCSB == other.metersFromUCSB:
                if self.condition < other.condition:
                    return True
        return False

    def getRent(self):
        return self.rent

    def getMetersFromUCSB(self):
        return self.metersFromUCSB

    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        if type(self.rent) == int:
            return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}/10".format(self.rent, self.metersFromUCSB, self.condition)

        if type(self.rent) == float:
            return "(Apartment) Rent: ${:.2f}, Distance From UCSB: {}m, Condition: {}/10".format(self.rent, self.metersFromUCSB, self.condition)
        