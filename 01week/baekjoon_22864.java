import java.util.*;
public class Main{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
        // tired : 시간당 피로도 , work : 시간당 처리량, recover : 시간당 회복도 , max_tired : 최대 피로도
        int tired=sc.nextInt();
        int work=sc.nextInt();
        int recover=sc.nextInt();
        int max_tired=sc.nextInt();
        // curr_tired : 현재 피로도 , sum_work : 총 처리량
        int curr_tired=0;
        int sum_work=0;
        // 하루 24시간
        for(int i=0;i<24;i++)
        {
            // 일을 하려 할때 최대 피로도를 넘지 않으면 일하기
            if(curr_tired+tired <=max_tired)
            {
                curr_tired += tired;
                sum_work += work;
            }
            // 일을 하려 할때 최대 피로도를 넘으면 일하지 않고 휴식
            else if(curr_tired + tired > max_tired)
            {
                curr_tired -= recover;
                if(curr_tired<0)
                    curr_tired=0;
            }
        }
        System.out.println(sum_work);
    }
} 

