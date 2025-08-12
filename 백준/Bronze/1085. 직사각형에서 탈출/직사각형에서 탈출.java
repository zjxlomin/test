import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x=sc.nextInt();
        int y=sc.nextInt();
        int w=sc.nextInt();
        int h=sc.nextInt();
        sc.nextLine();

        int[] d={x,w-x,y,h-y};
        int min=d[0];
        for(int i=0;i<4;i++){
            if(d[i]<min){
                min=d[i];
            }
        }
        System.out.println(min);
    }
}