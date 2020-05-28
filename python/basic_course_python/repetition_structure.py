## wile
bool = True
while(bool):
    print('wile')
    bool = False

## for
lists = ['one', 'two']
for list in lists:
    print(list)
## for using range
for number in range(5):
    print(number)
## for using break
for number in range(5):
    print("using breack {}".format(number))
    break

## for using continue
for number in range(5):
    print("using continue {}".format(number))
    if number > 1:
        continue
    print("number < 1")