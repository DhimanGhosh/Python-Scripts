class csv:
    __csv_file = None
    __reader = None
    __writer = None
    __row_count = 0
    __matrix = None
    
    def __init__(self, file = 'blank.csv'):
        global __csv_file
        __csv_file = file

    def __read(self, delimiter):
        lines = []
        with open(__csv_file, 'rt') as csv_data:
            lines.append(csv_data.readlines())
        return lines if len(lines[0])>0 else None

    def __write(self, row_data, rows, cols):
        global __row_count, __matrix
        __matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(cols):
            __matrix[__row_count][i] = row_data[i]
        __row_count += 1

    def reader(self, delimiter=','):
        __reader = self.__read(delimiter)
        res1 = []
        for row in __reader:
            row_data = row.split(delimiter)
            res = []
            for data in row_data:
                res.append(data)
            res1.append(res)
        __reader = res
        return __reader

    def writer(self, row_data, rows, cols):
        for i in range(cols):
            self.__write(row_data, rows, cols)
        pass
        
        
if __name__ == '__main__':
    csv.run()
    file = 'sample.csv'
    c = csv(file)
    print(c.reader())
