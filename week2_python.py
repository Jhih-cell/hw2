# w2py-1
def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    sum=0
    for i in range(min,max+1):
        sum=sum+i
    print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3,最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8,最後印出 30

# w2py-2
def avg(data):
# 請用你的程式補完這個函式的區塊
    sum=0
    for i in range(data["count"]):
        sum=sum+data["employees"][i]["salary"]
    avg= sum/data["count"]
    print(avg)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式

# w2py-3
def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
#將全部數字相乘結果推進array
    arr=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            arr.append(nums[i]*nums[j])
    for k in range(0,len(arr)):
        if(arr[k]>arr[0]):
            arr[0]=arr[k]
    print (arr[0])
maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值

# w2py-4
def twoSum(nums, target):
# your code here
    sum=0
    arr=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            sum=nums[i]+nums[j]
            if(sum == target and i != j):
                arr.append(i)
                arr.append(j)
    return arr

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
