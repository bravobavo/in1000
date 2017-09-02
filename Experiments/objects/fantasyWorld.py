class Transport:
    count = 0
    def __init__(self, transportType, maxSpeed):
        Transport.count += 1
        self.count = Transport.count
        self.transportType = transportType
        self.maxSpeed = maxSpeed

    def showSpeed(self):
        print("My speed is: "+ self.maxSpeed)

vehicle = Transport("car", "90km" )
vehicle.showSpeed ()
print(Transport.count)
