def printArray(arr):
    for element in arr:
        print(element)

# Example usage (this will be handled by the locked Solution class in the challenge)
if __name__ == '__main__':
    n = int(input())
    int_array = list(map(int, input().split()))
    printArray(int_array)
    
    n = int(input())
    string_array = input().split()
    printArray(string_array)
