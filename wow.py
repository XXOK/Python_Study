class Study():

    def getMinSum(self,A,B):

        for x, y in enumerate(A):
            print(x,y)
        for x, y in enumerate(B):
            print(x, y)

        return A[0]*B[-1]
    
if __name__ == '__main__':

    claxx = Study()

    print(claxx.getMinSum([1,2],[3,4]))
    print("안녕하세요"[0:5])