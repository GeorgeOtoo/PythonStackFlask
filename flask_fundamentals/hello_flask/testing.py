""" 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        targetVariable = 0
        unique = 1
        for unique in range(len(nums)-1):
            if nums[targetVariable] != nums[unique]:
                nums[targetVariable + 1] = nums[unique]
                targetVariable = targetVariable + 1
        return targetVariable + 1
"""

for i in range(0,3):
    print(i, end="")
    for j in range(8):
        print("george", end=" ")
    print("\n")


#    <h1>Welcome!</h1>

#     {% for i in range(times): %}
#         <div class="box"></div>
#     {% endfor %} 