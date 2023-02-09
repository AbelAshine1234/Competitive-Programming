class Solution(object):
    def findKthBit(self, n, k):
        binstr_length = [0] * (n+1)
        
        binstr_length[1] = 1
        
        for i in range(2, n+1):
            binstr_length[i] = 2 * binstr_length[i-1] + 1
            
        # ---------------------------------------------------
        def find_bit(n, k):
            
            if n == 1:
                # base case:
                return 0
            
            else:
                # general case:
                
                if k  <= binstr_length[n-1]:
                    
                    # k is on the left half, S_n-1
                    
                    return find_bit(n-1, k)
                
                elif k == (binstr_length[n-1] + 1):
                    
                    # k is on middle point, "1"
                    
                    return 1
                
                else:
                    toggle = lambda bit: bit^1
                    
                    # k is on the right half, reverse( invert(S_n-1) )
                    
                    return toggle( find_bit(n - 1, 2 * (binstr_length[n-1] + 1) - k) )
                
        # ---------------------------------------------------
        return str( find_bit(n, k) )
