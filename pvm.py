count=0
def orders(*items,**details):
    global count
    print(f"details:{details}")
    print(f"items:{items}")
    count+=1
    print(f"total orders:{count}")
orders("pizza","burger",name="bhargavi",place="hyderabad")

