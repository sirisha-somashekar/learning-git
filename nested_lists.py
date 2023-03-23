# create a nested list which takes user input

# enter number of items in sublist: 2
# enter number of items in list: 5
# your list: [['sirisha', 22], ['muzammil', 22], ...]

n = int(input('enter number of items in sublist: '))
m = int(input('enter number of items in list: '))

main_list = []
for index in range(0, m):
    sub_list = []
    for index_1 in range(0, n):
        element = input('enter the element: ')
        sub_list.append(element)
    main_list.append(sub_list)

print(main_list)