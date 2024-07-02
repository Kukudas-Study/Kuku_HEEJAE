import java.util.*;
public class Main{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
        int a=sc.nextInt();
        int n=0;
        Queue <Integer> q= new LinkedList<Integer>();
        // 큐에 순서대로 추가
        for(int i=1;i<a+1;i++)
            q.add(i);
        // 제일 위에 있는 거 버리고, 다음 거 맨밑으로 옮기기
        for(int j=a;j>1;j--)
        {
            q.poll();
            n=q.peek();
            q.add(n);
            q.poll();
        }
        System.out.println(q.poll());
    }
} 

