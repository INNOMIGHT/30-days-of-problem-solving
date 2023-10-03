def generate(numRows):
        res = [[1]]
        
        for i in range(1,numRows):
            temp = [0] + res[i-1]  + [0]
            row = []
            for j in range(len(temp)-1):
                row.append(temp[j] + temp[j+1])
           
            res.append(row)
        return res