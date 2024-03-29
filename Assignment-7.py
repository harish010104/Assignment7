import numpy as np

## Iterate over each number in the input vector n times, n being the number of columns in the o/p matrix and output 
## an intermediate vector. Use diff order formula based on increasing and decreasing condition.
## Reshape the intermediate vector using the size of the input vector (rows) and n (columns) to generate the o/p matrix. 
   
def gen_vander_matrix(ipvector, n, increasing=False):
    
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    
    return op_matx

print("------------OUTPUT-------------\n")

inputvector = np.array([1,2,3,4,5])
no_col_opmat = 3
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")

inputvector = np.array([1,2,4,6,8,10])
no_col_opmat = 5
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("---------------------------------------------------------------\n")
print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the