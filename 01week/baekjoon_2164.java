import java.util.*;
public class Main{
    public static void main(String[]args){
        Scanner sc= new Scanner(System.in);
        int a=sc.nextInt();
        int n=0;
        Queue <Integer> q= new LinkedList<Integer>();

        for(int i=1;i<a+1;i++)
            q.add(i);
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

