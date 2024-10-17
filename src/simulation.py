from person import Person, Couple, AVAILABLE_GENERATIONS, ALL_GENERATIONS, MALE, FEMALE
class Simulation:
    def __init__(self, use_gens : int) -> None:
        self._current_gen : list[Person] = []
        self._previous_couples : list[Couple] = []
        self._use_gens : int = use_gens
        self._gens_generated : int = 0

    def _Count_Men(self) -> int:
        return sum([person.is_man() for person in self._current_gen])
    
    def _Finish_Condition(self) -> bool:
        for person in self._current_gen:
            if not person.HasAllGens():
                return False
        return True
    
    def _Procreate(self) -> None:
        #self._current_gen = [couple.Procreate() for couple in self._previous_couples]
        new_wave : list[Person] = []
        for couple in self._previous_couples:
            new_wave += couple.Procreate()
        if(len(new_wave) == 0):
            quit(-1)
        self._current_gen = new_wave

    def _Generate_First_Generation(self):
        generation : list[Person] = []
        sim_gens = ALL_GENERATIONS[0:self._use_gens]
        for gen in sim_gens:
            p1 = Person(MALE, {u:0 for u in sim_gens})
            p1.set_gen_as_default(gen)
            p2 = Person(FEMALE, {u:0 for u in sim_gens})
            p2.set_gen_as_default(gen)
            generation += (p1,p2)
        self._current_gen = generation

    def _make_one_more_baby(self):
        self._current_gen += [couple.GenerateNewPerson() for couple in self._previous_couples]
    @staticmethod
    def _shuffle_the_list(target_list):
        L = len(target_list)
        for i in range(L // 3):
            target_list[i],target_list[L - i - 1] = target_list[L - i - 1],target_list[i]
    
    @staticmethod
    def _select(hunter : list[Person],deer : list[Person]) -> list[Couple]:#backtracking
        couples_list : list[Couple] = []
        max_person : Person
        max_points : int = -1
        points : int
        for h in hunter:
            max_person = None
            max_points = -1
            for d in deer:
                if (h.is_appropriate_person(d)):
                    points = h.GenDifference(d)
                    if (points <= max_points): continue
                    max_person = d
                    max_points = points
            couples_list.append(Couple(h, max_person))
            max_person.has_mingled = h.has_mingled = True
        if(couples_list == []):
            print("Returning empty list....")
            print(f"Hunters = {hunter}, Deers = {deer}")
            quit(-1)
        elif(len(couples_list) != len(hunter)):
            print("Returning smaller list (couples_list < hunter)")
        return couples_list
    
    def _mingle(self, chaser_gender : str) -> None:
        men = list(filter(lambda x: x.is_man(), self._current_gen))
        women = list(filter(lambda x: not x.is_man(), self._current_gen))
        couples : list[Couple] = []
        """def find_couple(hunter : Person):# implement randomness
            for deer in chased: 
                if hunter.is_appropriate_person(deer):
                    hunter.has_mingled = deer.has_mingled = True
                    couples.append(Couple(hunter, deer))
                    print(couples)
                    break"""
        if chaser_gender == MALE:
            chaser = men
            chased = women
        else:
            chaser = women
            chased = men
        if(chaser == []):
            print("Chaser is empty... : []")
            print(f"has generated {self._gens_generated} generations")
            quit(-1)
        #use backtracking
        couples : list[Couple] = self._select(chaser, chased)
        if(couples == []):
            print("couples returned empty list... retrying")
            self._Procreate()
            return self._MakeCouples()
        
        if(chaser == []): #if not everyone found their thing
            #reset mingle or else death comes`
            for person in self._current_gen:
                person.has_mingled = False
            #
            #self._make_one_more_baby()
            if(self._gens_generated == 1):
                self._shuffle_the_list(self._current_gen)
                return self._MakeCouples()
            self._Procreate()
            return self._MakeCouples()
        
        self._previous_couples = couples # :)

    def _MakeCouples(self) -> None:
        men = self._Count_Men()
        if men > len(self._current_gen) - men:
            self._mingle(FEMALE)
        else:
            self._mingle(MALE)

    def Simulate(self) -> int:
        self._Generate_First_Generation()
        while not self._Finish_Condition():
            self._gens_generated += 1
            self._MakeCouples()
            self._Procreate()
            self._shuffle_the_list(self._previous_couples)
            if self._gens_generated >= AVAILABLE_GENERATIONS ** 2 * self._gens_generated:
                print(f"Reached too many generations!, gen count = {self._gens_generated}")
                raise(Exception)
        return self._gens_generated
    
    def GetLastGen(self):
        #USE ONLY FOR TESTING!!!
        return self._current_gen
if __name__ == "__main__":
   for _ in range(10000):
        Sim = Simulation(3)
        print(Sim.Simulate())
        LG = Sim.GetLastGen()
        print(LG)
        print(len(LG))