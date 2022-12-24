def hello():
    print("hi there")
hello()    

    
def pack(item1, item2, item3):
    return item1, item2, item3
print(pack("milk", "bread", "butter"))

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("my lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat my {my_list[0]}")
            else:
                print(f"Next I eat my {my_list[i]}")
                
eat_lunch([])
eat_lunch(["apple", "Sandwich", "pudding", "cookie"])
eat_lunch(["orange"])