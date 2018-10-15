def container(height):
    left = 0
    right = len(height)-1
    maxcontainer = 0
    while left < right:
        for i in range(len(height)):
            maxcontainer = max(maxcontainer, min((height[left], height[right]))*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    return maxcontainer

height = [1,8,6,2,5,4,8,3,7]
print(container(height))
