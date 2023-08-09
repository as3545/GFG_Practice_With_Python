#Code
ans = []
        ans2 = []
        for i in range(N):
            if key == a[i]:
                ans.append(i)
        if len(ans)==0:
            return [-1,-1]
        elif len(ans)==1:
            ans.append(ans[0])
            return ans
        elif len(ans)>2:
            ans2.append(min(ans))
            ans2.append(max(ans))
            return ans2
        else:
            return ans
