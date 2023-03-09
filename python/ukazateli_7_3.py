class Backpack:
    def add(self, item):
        print("В рюкзаке лежит", item)
        self.content = item

my_backpack = Backpack()
print(Backpack.add)
print(my_backpack.add)

my_backpack.add(item='ноутбук')
print(my_backpack)

