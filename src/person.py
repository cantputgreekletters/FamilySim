from typing import Self
from random import randint as rn

MALE = "GENDER_MALE"
FEMALE = "GENDER_FEMALE"

ALL_GENERATIONS = "ABCDEFGHIJKLMNOPQRSTUWXYZ"
ALL_GENERATIONS += ALL_GENERATIONS.lower()
ALL_GENERATIONS = [i for i in ALL_GENERATIONS]
AVAILABLE_GENERATIONS = len(ALL_GENERATIONS)

class Person:
    def __init__(self, gender : str, Generations : dict) -> None:
        self._gender : str = gender
        self._Generations : dict[str,int] = Generations
        self.has_mingled : bool = False
    
    def GenDifference(self, other_person : Self) -> int:
        points : int = 0
        for self_gen, other_gen in zip(self._Generations.values(), other_person._Generations.values()):
            points += abs(self_gen - other_gen)
        return points
    
    def set_gen_as_default(self, gen : str) -> None:
        self._Generations[gen] = 1

    def is_man(self) -> bool: 
        return(self._gender == MALE)
            
    def is_appropriate_person(self, other_person : Self) -> bool:
        st_1 = other_person._gender == self._gender
        st_2 = other_person.has_mingled
        if st_1 or st_2:
            return False
        return True

    def HasAllGens(self):
        for val in self._Generations.values():
            if val == 0:
                return False
        return True

    def __repr__(self) -> str:
        return f"Gender = {self._gender}, Generations = {self._Generations}"

class Couple:
    def __init__(self, p1 : Person, p2 : Person) -> None:
        self._person1 : Person = p1
        self._person2 : Person = p2
        self._baby_gen : dict = self._calc_gen()

    def _calc_gen(self) -> dict[str, int]:
        gens : dict[str, int] = {gen : 0 for gen in self._person1._Generations.keys()}
        for gen in gens:
            gen1 = self._person1._Generations[gen]
            gen2 = self._person2._Generations[gen]
            if gen1 == 0 and gen2 == 0:
                continue
            gens[gen] = max(gen1, gen2) + 1
        return gens
    
    def GenerateNewPerson(self, gender : str):
        Gender = gender
        Generations = self._baby_gen
        return Person(Gender, Generations)

    def Procreate(self) -> tuple[Person, Person]:
        #return tuple([self.GenerateNewPerson() for _ in range(rn(2,5))])
        return tuple([self.GenerateNewPerson(MALE), self.GenerateNewPerson(FEMALE)])
    
    def __repr__(self) -> str:
        return f"Person1 = ({self._person1}), Person2 = ({self._person2})"

if __name__ == "__main__":
   test = [Person(MALE, "sads") for _ in range(10)]