def findIndices(nums, indexDifference, valueDifference):
        # Function to find indices in the list 'nums' based on specified differences
        
        # Iterate over the list 'nums' using enumerate to get both index and value
        for index, num in enumerate(nums):
            # Storing the current index and value for comparison
            i1 = index
            v1 = num
            
            # Nested loop to compare the current element with other elements in the list
            for index, num in enumerate(nums):
                # Check conditions for both index and value differences
                if abs(i1 - index) >= indexDifference and abs(v1 - num) >= valueDifference:
                    # If conditions are met, return the indices [i1, index]
                    return [i1, index]

        # If no matching indices are found, return [-1, -1]
        return [-1, -1]

# Example usage:
nums1 = [5, 1, 4, 1]
indexDifference1 = 2
valueDifference1 = 4
print(findIndices(nums1, indexDifference1, valueDifference1))  # Output: [0, 3]

nums2 = [2, 1]
indexDifference2 = 0
valueDifference2 = 0
print(findIndices(nums2, indexDifference2, valueDifference2))  # Output: [0, 0]

nums3 = [1, 2, 3]
indexDifference3 = 2
valueDifference3 = 4
print(findIndices(nums3, indexDifference3, valueDifference3))  # Output: [-1, -1]