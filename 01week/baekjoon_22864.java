import java.util.*;
public class Main{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
        int tired=sc.nextInt();
        int work=sc.nextInt();
        int recover=sc.nextInt();
        int max_tired=sc.nextInt();

        int curr_tired=0;
        int sum_work=0;
        
        for(int i=0;i<24;i++)
        {
            if(curr_tired+tired <=max_tired)
            {
                curr_tired += tired;
                sum_work += work;
            }
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

