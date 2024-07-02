class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        // 소수 판별 -> 소수 : true , 소수 X : false
        boolean b=true;
        // 숫자 3개 선택
        for(int i=0; i<nums.length-2 ;i++)
        {
            for (int j=i+1;j<nums.length-1;j++)
            {
                for(int p=j+1; p<nums.length; p++)
                {
                    int sum=nums[i]+nums[j]+nums[p];
                    // 소수 판별
                    for(int k=2; k<sum ; k++)
                    {
                        b=true;
                        if(sum % k==0)
                        {
                            b=false;
                            break;
                        }
                    }
                    // 소수일때
                    if(b)
                        answer++;
                }
            }
        }
        return answer;
    }
}

