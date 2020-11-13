

class DES:

    __pc_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44,
              36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20,
              12, 4]

    __pc_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37,
              47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    __iter_n_shift_ = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    __i_p = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48,
             40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13,
             5, 63, 55, 47, 39, 31, 23, 15, 7]

    __e_p = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

    __S1 = {
        0: [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        1: [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        2: [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        3: [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    }

    __S2 = {
        0: [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        1: [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        2: [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        3: [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    }

    __S3 = {
        0: [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        1: [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        2: [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        3: [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    }

    __S4 = {
        0: [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        1: [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        2: [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        3: [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    }

    __S5 = {
        0: [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        1: [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        2: [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        3: [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    }

    __S6 = {
        0: [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        1: [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        2: [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        3: [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    }

    __S7 = {
        0: [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        1: [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        2: [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        3: [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    }

    __S8 = {
        0: [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        1: [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        2: [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        3: [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0,  3, 5, 6, 11]
    }

    __final_permuatation_f = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9,
                              19, 13, 30, 6, 22, 11, 4, 25]

    __inverse_p = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5,
                   45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10,
                   50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

    C0 = []
    D0 = []

    def hex_to_int(self, text):
        return [int(charater, 16) for charater in text]

    def char_to_bin(delf, charater):
        bits = []
        while charater > 0:
            if charater % 2 == 1:
                bits.append(1)
            else:
                bits.append(0)
            charater = int(charater / 2)

        if len(bits) != 4:
            for i in range(4 - len(bits)):
                bits.append(charater % 2)

        bits.reverse()
        return bits

    def hex_to_binary(self, text, present=False):
        item_list = self.hex_to_int(text)
        letters_bits = []
        for item in item_list:
            temp = self.char_to_bin(item)
            if present:
                letters_bits.append(temp)
            else:
                for temp_bit in temp:
                    letters_bits.append(temp_bit)

        return letters_bits

    def generate_shifts(self):
        d = self.D0[:]
        c = self.C0[:]
        for shift_index in range(len(self.__iter_n_shift_)):
            shift_value = self.__iter_n_shift_[shift_index]
            for shift_no in range(shift_value):
                first = c[0]
                del c[0]
                c.append(first)

                first = d[0]
                del d[0]
                d.append(first)
                yield (shift_index+1, (c, d))

    def generate_round_keys_using_shifts(self, shift_index, shift_pairs):
        combined_pairs = [*shift_pairs[0], *shift_pairs[1]]
        return [combined_pairs[self.__pc_2[index] - 1] for index in range(len(self.__pc_2))]

    def generate_keys(self, original_key_bits):

        unique_indexes = [0, 1, 3, 5, 7, 9, 11, 13, 14, 16, 18, 20, 22, 24, 26, 27]

        # Applying PC-1 on originial_key_bits
        pc_1 = [original_key_bits[self.__pc_1[index] - 1] for index in range(len(self.__pc_1))]
        self.C0 = pc_1[:28]
        self.D0 = pc_1[28:]

        counter = 0
        self.__round_keys_k = []
        print(f"Format of Cs, Ds below: (Number=n,([Cn],[Dn]))")
        for item in self.generate_shifts():
            if counter in unique_indexes:
                print(item)
                self.__round_keys_k.append(self.generate_round_keys_using_shifts(item[0], item[1]))
            counter += 1
        else:
            print("Keys Generated!")
            print(self.__round_keys_k)

    def xor_chiper(self, bit_set_1, bit_set_2):
        if len(bit_set_1) != len(bit_set_2):
            return None
        else:
            xor_bits = []
            for index in range(len(bit_set_1)):
                xor = bit_set_1[index] ^ bit_set_2[index]
                xor_bits.append(xor)
            return xor_bits

    def get_row_col_mapping(self, bits_6, s_box_n):
        s_box_mapping = {
            1: self.__S1,
            2: self.__S2,
            3: self.__S3,
            4: self.__S4,
            5: self.__S5,
            6: self.__S6,
            7: self.__S7,
            8: self.__S8,
        }

        row_mapping = {
            '00': 0,
            '01': 1,
            '10': 2,
            '11': 3,
        }

        column_mapping = {
            '0000': 0,
            '0001': 1,
            '0010': 2,
            '0011': 3,
            '0100': 4,
            '0101': 5,
            '0110': 6,
            '0111': 7,
            '1000': 8,
            '1001': 9,
            '1010': 10,
            '1011': 11,
            '1100': 12,
            '1101': 13,
            '1110': 14,
            '1111': 15
        }

        return_value_mapping = {
            0: [0,0,0,0],
            1: [0,0,0,1],
            2: [0,0,1,0],
            3: [0,0,1,1],
            4: [0,1,0,0],
            5: [0,1,0,1],
            6: [0,1,1,0],
            7: [0,1,1,1],
            8: [1,0,0,0],
            9: [1,0,0,1],
            10: [1,0,1,0],
            11: [1,0,1,1],
            12: [1,1,0,0],
            13: [1,1,0,1],
            14: [1,1,1,0],
            15: [1,1,1,1]
        }

        s_box_model = s_box_mapping.get(s_box_n)

        # Bits slicing and combining to map row and columns
        first_last_bits = '' + str(bits_6[0]) + str(bits_6[-1])
        row_no = row_mapping.get(first_last_bits)
        mid_4_bits = ''
        for bit in bits_6[1:-1]:
            mid_4_bits += str(bit)
        column_no = column_mapping.get(mid_4_bits)

        mapping_value = s_box_model[row_no][column_no]
        return return_value_mapping.get(mapping_value)

    def final_permuatation_f(self, mapped_bits):
        return [mapped_bits[self.__final_permuatation_f[index] - 1] for index in range(len(self.__final_permuatation_f))]

    def get_s_box_mapping(self, xor_bits):
        mapped_bits_32 = []
        counter = 1
        for index in range(0, len(xor_bits), 6):
            mapping = self.get_row_col_mapping(xor_bits[index: index + 6], counter)
            for bit in mapping:
                mapped_bits_32.append(bit)
            counter += 1
        else:
            return self.final_permuatation_f(mapped_bits_32)

    def f_Rn_Kn(self, R_n, K_n):
        # Applying expanded permutation
        R_n = [R_n[self.__e_p[index] - 1] for index in range(len(self.__e_p))]
        if len(R_n) != len(K_n):
            return None
        else:
            xor_bits = []
            # print(f"R: {R_n}")
            # print(f"K: {K_n}")
            for index in range(len(R_n)):
                xor = R_n[index] ^ K_n[index]
                xor_bits.append(xor)

            # print(f"XOR: {xor_bits}")
            # x = self.get_s_box_mapping(xor_bits)
            # print(f"MAP: {x}")
            return self.get_s_box_mapping(xor_bits)

    def round(self, left_ip, right_ip):
        L_n = right_ip
        R_n = left_ip

        print(f"\nL0: {left_ip}\n")
        print(f"R0: {right_ip}\n")

        for i in range(16):
            K_n = self.__round_keys_k[i]
            f_R_Kn = self.f_Rn_Kn(L_n, K_n)
            # bef_4 = R_n
            R_n = self.xor_chiper(R_n, f_R_Kn)
            temp = L_n
            L_n = R_n
            R_n = temp
            print(f'{i}---------------------------------------------------------')
            # print(f"F: {f_R_Kn}")
            print(f"L: {R_n}")
            print(f"R: {L_n}")
            print('-------------------------------------------------------------')
        else:
            # print('  ', L_n)
            # print('  ', R_n)
            return [*L_n, *R_n]

    def encrypt_bits(self, message_bits):
        # Applying Intitial-Permutation
        initial_permutation = [message_bits[self.__i_p[index] - 1] for index in range(len(self.__i_p))]
        print(f"\nIP: {initial_permutation}\n\n")
        left_i_p = initial_permutation[:32]
        right_i_p = initial_permutation[32:]
        enc_msg_bits = self.round(left_ip=left_i_p, right_ip=right_i_p)
        # Applying Inverse Permutation as self.__inverse_p
        return [enc_msg_bits[self.__inverse_p[index] - 1] for index in range(len(self.__inverse_p))]

    def encrypt(self, text):
        msg_bits = self.hex_to_binary(text, present=False)
        return self.encrypt_bits(msg_bits)

    def convert_to_hex(self, encrypted_bits):

        return_value_mapping = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'A',
            '1011': 'B',
            '1100': 'C',
            '1101': 'D',
            '1110': 'E',
            '1111': 'F'
        }

        mapping_bits_list = []
        for index in range(0, len(encrypted_bits), 4):
            char_bits = ''
            bits_4 = encrypted_bits[index: index + 4]
            for bit in bits_4:
                char_bits += str(bit)
            else:
                mapping_bits_list.append(char_bits)
        else:
            return_value = ''
            for key in mapping_bits_list:
                return_value += return_value_mapping.get(key)
            else:
                return return_value

