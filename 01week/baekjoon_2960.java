import java.util.Scanner;
public class Main{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int cnt=0;
        boolean[] list=new boolean[n+1];
        // 자신의 배수 지우기 -> 지우면 true
        for(int i=2; i<=n;i++)
        {
            if(list[i])
                continue;
            list[i]=true;
            cnt++;
            if (cnt==k)
            {
                System.out.println(i);
                break;
            }
            for(int j=i*2; j<=n ; j+=i)
            {
                if(!list[j])
                {
                    list[j]=true;
                    cnt++;
                }
                if (cnt==k)
                {
                    System.out.println(j);
                    break;
                }
            }   
        }
    }
} 
