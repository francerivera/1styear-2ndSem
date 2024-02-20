class Blender:
    def blend(fruit1: str = None, fruit: str = None, n = 1):
        if fruit1 and fruit2 is None:
            print("There is nothing to blend here, boss.")
        else:
            for i in range(n):
                print(f"Blending {fruit1} and {fruit2}, boss.")

fruits = Blender
fruits.blend()
fruits.blend("Apple", "Banana")
fruits.blend("Strawberry", "Blueberry", 3)
