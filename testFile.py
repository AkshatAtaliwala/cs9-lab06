from Apartment import Apartment
from lab06 import mergesort
from lab06 import ensureSortedAscending
from lab06 import getNthApartment
from lab06 import getTopThreeApartments

def test_SampleOutput1():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 200, 7)
    a2 = Apartment(1000, 100, 9)
    a3 = Apartment(1000, 214, 10)
    a4 = Apartment(300, 112, 3)
    a5 = Apartment(300.50, 250, 2)
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert getNthApartment(apartmentList, len(apartmentList)) == "(Apartment) Rent: $300.50, Distance From UCSB: 250m, Condition: 2/10"
    mergesort(apartmentList)
    assert getTopThreeApartments(apartmentList) == "1st: (Apartment) Rent: $300, Distance From UCSB: 112m, Condition: 3/10, 2nd: (Apartment) Rent: $300.50, Distance From UCSB: 250m, Condition: 2/10, 3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: 9/10"
    assert getNthApartment(apartmentList, len(apartmentList)) == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 3/10"

def test_SampleOutput2():
    a0 = Apartment(2400, 50, 10)
    a1 = Apartment(2200, 50, 2)
    apartmentList = [a0, a1]
    mergesort(apartmentList)
    assert getNthApartment(apartmentList, 3) == "(Apartment 3) DNE"
    assert getTopThreeApartments(apartmentList) == "1st: (Apartment) Rent: $2200, Distance From UCSB: 50m, Condition: 2/10, 2nd: (Apartment) Rent: $2400, Distance From UCSB: 50m, Condition: 10/10"

def test_Apartment():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 200, 7)
    a2 = Apartment(1204.56, 200, 3)
    a3 = Apartment(300, 112, 3)
    assert (a0 > a1) == True
    assert (a1 > a0) == False
    assert (a0 == a2) == True

    assert a0.getRent() == 1204.56
    assert a0.getMetersFromUCSB() == 200
    assert a0.getCondition() == 3
    assert a0.getApartmentDetails() == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 3/10"

    assert a3.getRent() == 300
    assert a3.getMetersFromUCSB() == 112
    assert a3.getCondition() == 3
    assert a3.getApartmentDetails() == "(Apartment) Rent: $300, Distance From UCSB: 112m, Condition: 3/10"

def test_mergesort_sortedascending():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 200, 7)
    a2 = Apartment(1000, 100, 9)
    a3 = Apartment(1000, 214, 10)
    a4 = Apartment(300, 112, 3)
    a5 = Apartment(300.50, 250, 2)
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True

def test_getNth_getTopThree():
    a0 = Apartment(1204.56, 200, 3)
    a1 = Apartment(1204.56, 200, 7)
    a2 = Apartment(1000, 100, 9)
    a3 = Apartment(1000, 214, 10)
    a4 = Apartment(300, 112, 3)
    a5 = Apartment(300.50, 250, 2)
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert getNthApartment(apartmentList, 2) == "(Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 7/10"
    assert getNthApartment(apartmentList, 0) == "(Apartment 0) DNE"
    assert getNthApartment(apartmentList, len(apartmentList)) == "(Apartment) Rent: $300.50, Distance From UCSB: 250m, Condition: 2/10"
    assert getNthApartment(apartmentList, 7) == "(Apartment 7) DNE"

    assert getTopThreeApartments(apartmentList) == "1st: (Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 3/10, 2nd: (Apartment) Rent: $1204.56, Distance From UCSB: 200m, Condition: 7/10, 3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: 9/10"
    mergesort(apartmentList)
    assert getTopThreeApartments(apartmentList) == "1st: (Apartment) Rent: $300, Distance From UCSB: 112m, Condition: 3/10, 2nd: (Apartment) Rent: $300.50, Distance From UCSB: 250m, Condition: 2/10, 3rd: (Apartment) Rent: $1000, Distance From UCSB: 100m, Condition: 9/10"