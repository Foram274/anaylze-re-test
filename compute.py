import sys

# taking values from command line
threshold = float(sys.argv[1])
limit = float(sys.argv[2])

input_values = []
output_values = []
sum = 0.0

# for taking input from user
while True:
    print('enter input')
    num = round(float(input()), 1)
    input_values.append(num)
    print('Do you want to enter more numbers? Yes/No')
    choice = str(input())
    if(choice == 'No' or choice == "no"):
        break


for i in input_values:
    temp = i - threshold
    temp1 = sum+temp

    if(temp1<limit):
        if(temp>0):
            output_values.append(temp)
            sum = temp1
        else:
            output_values.append(0.0)
    else:
        output_values.append(limit-sum)
        sum = limit

output_values.append(sum)           # adding the sum at the end

# printing the output values including sum
for i in output_values:
    print(i)