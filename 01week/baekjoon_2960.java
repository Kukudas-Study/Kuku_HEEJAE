import java.util.Scanner;
public class Main{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int cnt=0;
        boolean[] list=new boolean[a+1];
        // 자신의 배수 지우기 -> 지우면 true
        for(int i=2; i<=a;i++)
        {
            if(list[i])
                continue;
            list[i]=true;
            cnt++;
            if (cnt==b)
            {
                System.out.println(i);
                break;
            }
            for(int j=i*i; j<=a ; j+=i)
            {
                if(!list[j])
                {
                    list[j]=true;
                    cnt++;
                }
                if (cnt==b)
                {
                    System.out.println(j);
                    break;
                }
            }   
        }
    }
} 

