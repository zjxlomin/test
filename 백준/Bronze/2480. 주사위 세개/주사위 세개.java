import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] dice= {0,0,0,0,0,0};
        int max=0;
        for(int i=0;i<3;i++){
            int n=sc.nextInt();
            dice[n-1]++;
            if(n>max){
                max=n;
            }
        }
        int res=0;
        for(int i=0;i<6;i++){
            if(dice[i]==3){
                res=10000+(i+1)*1000;
                break;
            }
            else if(dice[i]==2){
                res=1000+(i+1)*100;
                break;
            }
        }
        if(res==0){
            res=max*100;
        }
        System.out.println(res);
    }
}