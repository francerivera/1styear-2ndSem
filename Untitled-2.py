class Character:
    def __init__(self,name,hp,mana,atk,armor):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.atk = atk
        self.armor = armor
        
        print("Created " + self.name)

char1 = Character("Garen","800","0","70","120")
char2 = Character("Neeko","500","250","90","70")
char3 = Character("Zed","600","150","80","90")


class Animal:
    def __init__(self,type,voice):
        self.type = type
        self.voice = voice

    def speak(self):
        print(self.voice)

    def introduce(self):
        print("I am a " + self.type)

a1 = Animal("Dog","Arf")
a1.introduce()
a1.speak()

a2 = Animal("Cat","Meow")
a2.introduce()
a2.speak()


class User:
    def __init__(self,firstName,lastName,likesCount,friendsName):
        self.firstName = firstName
        self.lastName = lastName
        self.likesCount = likesCount
        self.friendsName = friendsName

    def introduce(self):
        print("Hi I am " + (self.firstName) + " " + (self.lastName))

    def fullProfile(self):
        print("Full Name : " + self.firstName + " " + self.lastName)
        print("Likes     : " + str(self.likesCount))
        print("Friends   : ")
        for friend in self.friendsName:
            print("  -" + friend)

user1 =  User("France","Rivera",100,["John","Michael","Albert"])
user1.introduce()
user1.fullProfile()





