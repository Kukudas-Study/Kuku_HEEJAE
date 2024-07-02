class Solution {
    public int solution(int[] nums) {
        int answer = 0;

        boolean b=true;
        for(int i=0; i<nums.length-2 ;i++)
        {
            for (int j=i+1;j<nums.length-1;j++)
            {
                for(int p=j+1; p<nums.length; p++)
                {
                    int sum=nums[i]+nums[j]+nums[p];
                    for(int k=2; k<sum ; k++)
                    {
                        b=true;
                        if(sum % k==0)
                        {
                            b=false;
                            break;
                        }
                    }
                    if(b)
                        answer++;
                }
            }
        }
        return answer;
    }
}

