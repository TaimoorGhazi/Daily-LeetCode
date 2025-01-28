class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []

        row = [1]
        for i in range(1, rowIndex + 1):
            row = [1] + [row[j - 1] + row[j] for j in range(1, len(row))] + [1]
        
        return row


# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         result = []  # This will hold the rows of Pascal's Triangle.

#         for row_num in range(rowIndex + 1):  # Loop through each row.
#             row = [None] * (row_num + 1)  # Create a row with `row_num + 1` elements.

#             row[0], row[-1] = 1, 1  # The first and last elements of the row are always 1.

#             # Fill in the interior elements (if any).
#             for j in range(1, len(row) - 1):  # Start from index 1 to len(row) - 2.
#                 row[j] = result[row_num - 1][j - 1] + result[row_num - 1][j]

#             result.append(row)  # Add the row to the result.

#         return result[rowIndex]  # Return the complete Pascal's Triangle.
