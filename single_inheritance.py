
class Person():
    def __init__(self,name,place_of_recidence):
        self.name1=name
        self.place_of_recid=place_of_recidence
    def display_attributes(self):
        return (self.name1,self.place_of_recid)


class Sister(Person):
    def __init__(self,name,place_of_recidence,exam_subjects):
        super().__init__(name,place_of_recidence)
        self.ex_sub=exam_subjects
        print(super().display_attributes())
        print(self.ex_sub)
class Uncle(Person):
    def __init__(self,name,place_of_recidence,business):
        super().__init__(name,place_of_recidence)
        self.business1=business
        print(super().display_attributes())
        print(self.business1)
        
def main():
     sis_obj=Sister('sukanya','karad','HPCSA')
     un_obj=Uncle('Pranjali','Pune','Supercom')
     print(sis_obj.display_attributes())
     print(un_obj.display_attributes())
     print(sis_obj.ex_sub)
     print(un_obj.business1)
if __name__ == "__main__":
    main()