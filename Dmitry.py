class People(object):
    people = 0

    def __init__(self, g =0, age = 13, sex = "мужской", name = "сеоежа", prof = "игрок"):
        self.age = age
        self.sex = sex
        self.name = name
        self.prof = prof
        self.namber = g
        People.people+=1
    def invite(self):
        if (self.namber==1):
            print("в кванторимум добавился один человек")

if __name__ == "__main__":

    rostic = People()
    print(rostic.age)