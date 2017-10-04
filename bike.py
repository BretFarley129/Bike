class Bike(object):
    def __init__(self, p, ms):
        self.price = p
        self.max_speed = ms
        self.miles = 0

    def displayInfo(self):
        print "Price: {} \nMax Speed: {} \nMiles: {}".format(str(self.price), str(self.max_speed), str(self.miles))
        return self
    
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing..."
        if self.miles > 0:
            self.miles -= 5
        return self

bike1 = Bike(250, "100 mph")
bike1.ride().ride().ride().reverse().displayInfo()
bike2 = Bike(500, "2 mph")
bike2.ride().ride().reverse().reverse().displayInfo()
bike3 = Bike(43905, "54 mph")
bike3.reverse().reverse().reverse().displayInfo()