import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] num = new int[10];
        int[] res = new int[42];
        int count = 0;
        Arrays.fill(res, 0);
        for(int i=0;i<10;i++){
            num[i] = sc.nextInt();
            sc.nextLine();
            int k = num[i]%42;
            if(res[k]==0){ res[k]=1; }
        }
        for(int i=0;i<42;i++){
            if(res[i]==1) count++;
        }
        System.out.println(count);
    }
}