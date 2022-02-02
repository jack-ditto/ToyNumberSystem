import itertools


class ToyNumberSystem:

    ''' Model a toy number system with num_bits bits and a exp_shift exponent shift.
    '''

    def __init__(self, num_bits=5, exp_shift=-3, sign_bit_start=0, sign_bit_end=1, exponent_bit_start=1, exponent_bit_end=4, mantissa_bit_start=4, mantissa_bit_end=5):

        self.num_bits = num_bits
        self.sign_bit_start = sign_bit_start
        self.sign_bit_end = sign_bit_end
        self.exponent_bit_start = exponent_bit_start
        self.exponent_bit_end = exponent_bit_end
        self.mantissa_bit_start = mantissa_bit_start
        self.mantissa_bit_end = mantissa_bit_end
        self.exp_shift = exp_shift

        # Alias method
        self.fl = self.map_to_system_number

    def map_to_system_number(self, n, method="rounding"):
        ''' Map a float to a number in the toy number system. 

            Method can be "rounding" or "chopping" 
        '''

        n = float(n)
        system_nums = self.gen_numbers_in_system()

        if not method in ["rounding", "chopping"]:
            print("Method must be \"rounding\" or \"chopping\".")

        closest_dist = float('inf')
        closest_num = 0
        for num in system_nums:

            if n == num:
                return n

            dist = abs(n - num)
            if method == "rounding":

                # LEQ for modpoints rounded up
                if dist <= closest_dist:

                    closest_dist = dist
                    closest_num = num

            elif method == "chopping":

                if dist < closest_dist and num < n:
                    closest_dist = dist
                    closest_num = num

        return closest_num

    def convert_binary_to_decimal(self, binary_string, exp_shift=None, method="rounding"):
        ''' Convert a binary string in our toy number system to a float.
        '''

        if not exp_shift:
            exp_shift = self.exp_shift

        if len(binary_string) != self.num_bits:

            print(f"Binary string must be {self.num_bits} characters long.")
            return

        sign_bit = int(
            binary_string[self.sign_bit_start: self.sign_bit_end], 2)

        exponent = int(
            binary_string[self.exponent_bit_start:self.exponent_bit_end], 2) + exp_shift

        mantissa_string = binary_string[self.mantissa_bit_start:self.mantissa_bit_end]
        mantissa = int(mantissa_string, 2) * 2**(-len(mantissa_string))

        evaluated = (1.0 + mantissa) * (2 ** exponent)

        if sign_bit:
            evaluated = -evaluated

        return evaluated

    def getbin(self, n, s=['']):
        ''' Recursively generate all binary combinations with n digits
        '''

        if n > 0:
            return [
                *self.getbin(n - 1, [i + '0' for i in s]),
                *self.getbin(n - 1, [j + '1' for j in s])
            ]
        return s

    def gen_numbers_in_system(self):
        ''' Return a list of all binary strings in our number system
        '''

        binary_strings = self.getbin(self.num_bits)

        possible_nums = [self.convert_binary_to_decimal(
            x) for x in binary_strings]

        return possible_nums


if __name__ == '__main__':

    t = ToyNumberSystem()
    resp = t.convert_binary_to_decimal("11010", exp_shift=-3)
    t.gen_numbers_in_system()

    print(t.fl(9999, method="chopping"))

    print(resp)
