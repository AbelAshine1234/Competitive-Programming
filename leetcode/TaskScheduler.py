class Solution(object):
    def leastInterval(self, tasks, n):
      
        
        counts = list(collections.Counter(tasks).values()) # [3,3]
        max_count = max(counts) # 3
        num_of_chars_with_max_count = counts.count(max_count) # 2, A and B
        
        num_of_chunks_with_idles = max_count-1 # 2  -> A  A  A

        length_of_a_chunk_with_idle = n+1  # 3 -> A _ _ A _ _ A 

        length_of_the_final_chunk = num_of_chars_with_max_count  # 2  

        length_of_all_chunks = (num_of_chunks_with_idles*length_of_a_chunk_with_idle) + length_of_the_final_chunk # 2*3 + 2 = 8 

        return max(len(tasks), length_of_all_chunks)
        
