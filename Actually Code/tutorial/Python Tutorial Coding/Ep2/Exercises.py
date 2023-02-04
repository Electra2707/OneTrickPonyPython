from Basic import ask_num

print("Add the numbers to the list")
list1 = []
sum = 0
while True:
    num = ask_num()
    list1.append(num)
    sum += num
    try:
        confirmation = input("Add more numbers? S/N: ").upper()
        if confirmation == "N":
            break
        else:
            pass
    except ValueError:
        pass

average = sum/len(list1)
print(average)
