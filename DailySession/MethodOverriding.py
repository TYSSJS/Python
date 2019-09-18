class Meoverride():
    def override(self):
        print("Check Method override from parent")

    def override(self):
        print("check from child")
ride=Meoverride()
ride.override()
# Method overriding will override the parent method implementation into the child method