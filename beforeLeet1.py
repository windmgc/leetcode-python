__author__ = 'windmgc'
def fun1():
    count = 10**5
    nums = []
    for i in range(count):
        nums.append(i)
    nums.reverse()
    for i in range(nums.__len__()):
        print nums[i]

def fun2():
    count = 10**5
    nums = []
    for i in range(count):
        nums.insert(0,i)
    for i in range(nums.__len__()):
        print nums[i]

def main():
    fun1()
    # fun2()

if __name__ == '__main__':
    main()
