# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def my_convert(self, s: str, numRows: int) -> str:
        count_spaces_between = numRows - 2 if numRows - 2 > 0 else 0
        len_string = len(s)
        for row in range(numRows):
            for index in range(row, len_string, numRows + count_spaces_between):
                print(s[index], end=' ')
                if row == 0 or row == numRows - 1:
                        print(' ' * (count_spaces_between + 1), end='')
                else:
                    tmp_index = index + count_spaces_between + 1
                    if tmp_index < len_string:
                        print(s[tmp_index], end=' ')

            print()
            #     print('2'.join(['1' for i in range(count_spaces_between)]), sep=' ')


s = Solution()
s.my_convert(s="PAYPALISHIRING", numRows=4)
