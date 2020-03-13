class Robot:
    def __init__(self,name,color,weight):
        self.color=color
        self.name=name
        self.weight=weight
    def whatisYourname(self):
        print(f'my name is {self.name}')
        print(f'my weight is {self.weight}')
        print(f'my color is {self.color}')

#
# r1 =Robot()
# r2 =Robot()
r1 = Robot( 'Mike','white', 55) #You can change number by replacing number in r1 and r2 with a different number
r2 = Robot('Adam','green',80)

# r1.color ='white'
# r1.name = 'Mike'
# r1.weight = 50
#
# r2.color = 'white'
# r2.name = 'Adam'
# r2.weight = 75


r1.whatisYourname()
r2.whatisYourname()
