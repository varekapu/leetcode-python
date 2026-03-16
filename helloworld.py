class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of both arrays

        for i in range(m+n-1):
            for j in range(n-1):
                if(nums2[j]>nums1[i]):
                    
            if n[len(nums2)-1]>

# Move main() outside the class
def main():
    nums1 = [1,2,3,0,0,0]
    m = 3 
    nums2 = [2,5,6] 
    n = 3
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    print(nums1)  # This will print the merged array

if __name__ == "__main__":
    main()