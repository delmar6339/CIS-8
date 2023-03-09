f = open("ps8p4file.txt", "r")

#initialize counters and sums to 0
c = 0.0
totp_ex = 0.0

#get first data line
item = str(f.readline().rstrip('\n'))

while item != "":
    qty = float(f.readline())
    price = float(f.readline())

    # calculate extended price and sum/count in the loop
    ep = qty * price
    totp_ex += ep
    c += 1

    #display a line of data
    print("Item is:   ", item)
    print("Quanity is:   ", qty)
    print("Price is:   ", price)
    print("Extended Price is:  ", ep)

    # get next data
    item = str(f.readline().rstrip('\n'))

# close the file
f.close()

# after the loop
# final calculations
# display them and sums and counts
print("Total Extended Price:         ", totp_ex)
print("Number of Orders:         ", c)
avg = totp_ex / c 
print("Average Order:           ", avg)




