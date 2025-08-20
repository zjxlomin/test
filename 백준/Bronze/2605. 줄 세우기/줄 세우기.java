import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        List<Integer> line = new LinkedList<>();
        int[] num = new int[n];
        for(int i=0;i<n;i++){
            num[i]=sc.nextInt();
        }

        for(int i=0;i<n;i++){
            line.add(i-num[i],i+1);
        }

        for(int i=0;i<n;i++){
            System.out.print(line.get(i)+" ");
        }
    }
}