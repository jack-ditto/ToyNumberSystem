from ToyNumberSystem import ToyNumberSystem


# Init a Toy Number System
t1 = ToyNumberSystem()
t2 = ToyNumberSystem(num_bits=5, exp_shift=-1, sign_bit_start=0, sign_bit_end=1,
                     exponent_bit_start=1, exponent_bit_end=3, mantissa_bit_start=3, mantissa_bit_end=5)


bin_num = "10101"
ret = t1.convert_binary_to_decimal(bin_num)  # Default method is "rounding"
print(f"Binary string {bin_num} is {ret} in this number system.")

bin_num = "01010"
ret = t1.convert_binary_to_decimal(bin_num, method="chopping")
print(f"Binary string {bin_num} is {ret} in this number system.")

bin_num = "10101"
ret = t2.convert_binary_to_decimal(bin_num, method="rounding")
print(f"Binary string {bin_num} is {ret} in this number system.")


ret = t1.gen_numbers_in_system()
print(ret)

ret = t2.gen_numbers_in_system()
print(ret)
