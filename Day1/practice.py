
def mySqrt(x:int) -> int:
    min, max = 0, x  # starting from 0 to the x value
    res = 0
    while min <= max:
        mid = int((min + max)/2)
        squared = mid * mid
        if squared == x:
            return mid
        elif squared > x:
            max = mid - 1
        else:
            min = mid + 1
            res = mid
    return res

print(mySqrt(16))
print(mySqrt(8))
print(mySqrt(1))