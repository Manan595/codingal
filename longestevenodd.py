def longestEvenOddSubarray(arr, n):
    longest = 1
    cnt = 1

    for i in range(n - 1):
        if (arr[i] + arr[i + 1]) % 2 == 1:
            cnt = cnt + 1
        else:
            longest = max(longest, cnt)
            cnt = 1

    if longest == 1:
        return 0

    return max(cnt, longest)


# Driver code
arr = [3, 2, 4, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 4, 2]
n = len(arr)

print(longestEvenOddSubarray(arr, n))