import numpy as np

def calculate(list):
    import numpy as np

def calculate(list):
    while True:
        try:
            a = np.array(list)
            matrix = a.reshape(3,3)
            mean_ax1 = []
            mean_ax2 = []
            mean_flatenned = a.mean()
            variance_ax1 = []
            variance_ax2 = []
            variance_flattened = a.var()
            std_ax1 = []
            std_ax2 = []
            std_flattened = a.std()
            max_ax1 = []
            max_ax2 = []
            max_flattened = a.max()
            min_ax1 = []
            min_ax2 = []
            min_flattened = a.min()
            sum_ax1 = []
            sum_ax2 = []
            sum_flattened = a.sum()
            
            for i in range(matrix[0].size):
                mean_ax1.append(matrix[:,i].mean())
                variance_ax1.append(matrix[:,i].var())
                std_ax1.append(matrix[:,i].std())
                max_ax1.append(matrix[:,i].max())
                min_ax1.append(matrix[:,i].min())
                sum_ax1.append(matrix[:,i].sum())
                
            for i in range(matrix[:, 0].size):
                mean_ax2.append(matrix[i].mean())
                variance_ax2.append(matrix[i].var())
                std_ax2.append(matrix[i].std())
                max_ax2.append(matrix[i].max())
                min_ax2.append(matrix[i].min())
                sum_ax2.append(matrix[i].sum())
                
            calculations = {
                'mean' : [mean_ax1, mean_ax2, mean_flatenned],
                'variance' : [variance_ax1, variance_ax2, variance_flattened],
                'standard deviation' : [std_ax1, std_ax2, std_flattened],
                'max' : [max_ax1, max_ax2, max_flattened],
                'min' : [min_ax1, min_ax2, min_flattened],
                'sum' : [sum_ax1, sum_ax2, sum_flattened]
            }
            return calculations
        
        except ValueError:
            if len(list) != 9 :
                raise ValueError('List must contain nine numbers!')
