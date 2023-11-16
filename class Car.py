class Car:
    def __init__(self, number, speed, color, nitroSpeed, model) :
        self.number = number 
        self.speed = speed
        self.color = color
        self.nitroSpeed = nitroSpeed
        self.model = model

    def turn(self, direction) :
        print(f"The car turns {direction}.")

    def accelerate(self):
        if self.nitroSpeed :
            print("Nitro boost activated!")
            self.speed += 20
        else:
            self.speed += 10
        print(f"The car accelerates to {self.speed} km/h.")

    def brake(self) :
        self.speed -= 5
        print(f"The car slows down to {self.speed} km/h.")

    def boost(self) :
        if not self.nitroSpeed:
            print("Nitro boost activated!")
            self.nitroSpeed = True
        else:
            print("Nitro boost is already activated.")
    
    def info(self) :
        print('The Model of Car {} is {}, color is {}, speed is {},'.format(self.number,  self.model, self.color, self.speed))

# Example Test
car1 = Car(1, 0, "Red", False, "Sedan")

car1.info()
car1.accelerate()
car1.turn("left")
car1.brake()
car1.boost()
car1.accelerate()
