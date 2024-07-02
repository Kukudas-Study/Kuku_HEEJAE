import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        Queue<Integer> bridge=new LinkedList<>();
        // time : 경과 시간, sum : 다리에 올라간 총 트럭의 무게
        int time=0, sum=0;
        
        for(int i=0;i<truck_weights.length;i++)
        {
            int add_truck = truck_weights[i];
            while(true)
            {
                if(bridge.isEmpty())
                {
                    bridge.add(add_truck);
                    sum +=add_truck;
                    time++;
                    break;
                }
                else if(bridge.size()==bridge_length)
                    sum -=bridge.poll();
                else
                {
                    if(sum+add_truck <= weight)
                    {
                        bridge.add(add_truck);
                        sum += add_truck;
                        time++;
                        break;
                    }
                    else
                    {
                        bridge.add(0);
                        time++;
                    }
                }
            }
        }
        answer=time + bridge_length;
        
        return answer;
    }
}

