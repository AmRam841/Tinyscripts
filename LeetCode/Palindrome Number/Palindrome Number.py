class Solution(object):
    def isPalindrome(self, x):
       if x < 0 :
           print("NO!")
           return False 
       


       
       OG_x = x
       lengh = len(str(x))
       reversednum = 0
       for _ in range(lengh):
           #first we take the last digit and store it in the place holder
           reversednumholder = x % 10
           #then we do a little thing here , we take the number 0 in the reversednum and then *10 why ? well think about it . 0 * 10 + somenumber =>> some number like 4 
           # then the next time the reverseednum is 4 and now we want to add another number but we dont want this new number (lets say 5 ) to resualt in 9 we want it to be 45 so we make it * 10 Get it ? 
           reversednum = reversednum * 10 + reversednumholder
           x //= 10

       if reversednum == OG_x :
           print("YES!")
           return True
       else:
           print("No!")
           return False
              
         




los = Solution()  
los.isPalindrome(int(input()))   