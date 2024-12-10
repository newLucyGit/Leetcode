def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1

        for i in range(len(matrix)):
            # print("matrix: ", matrix[i][r])
            if matrix[i][r] >= target:
                # print("2) matrix: ", matrix[i][r], " l", l, " r",r)
                if matrix[i][r] == target:
                    return True
                
                while l <= r:
                    mid = l + ((r - l) // 2)
                    # print("1) mid: ", mid, " l", l, " r", r)
                    
                    if matrix[i][mid] > target:
                        r = mid - 1
                        # print("2) mid: ", mid, " l", l, " r", r)

                    elif matrix[i][mid] < target:
                        l = mid + 1
                        # print("3) mid: ", mid, " l", l, " r", r)
                    
                    else:
                        # print("4) mid: ", mid, " l", l, " r", r)
                        return True

                return False

        return False