import HouseParkTest

class HouseKim(HouseParkTest.HousePark) :
    lastname = "박"  
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네" %(self.fullname, where, day))
        
juliet = HouseKim("줄리엣")
juliet.travel("독도", 3)
