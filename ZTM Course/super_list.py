class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()

print(len(super_list))
print(super_list.append(5))
print(super_list.append(10))
print(super_list[1])