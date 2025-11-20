bin_input=input("Enter a binary number: ")
def bin_to_dec(bin_num):
    dec_num=0
    bin_num=str(bin_num)
    # iterate over each bit from right to left and accumulate its decimal value
    for i in range(len(bin_num)):
        dec_num += int(bin_num[len(bin_num)-1-i]) * (2**i)
    return dec_num

print("The decimal equivalent of binary", bin_input, "is", bin_to_dec(bin_input))
