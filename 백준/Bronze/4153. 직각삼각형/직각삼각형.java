import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        StringBuilder sb = new StringBuilder();
        while(true){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            if(a==0 && b==0 && c==0){
                break;
            }
            if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a){
                sb.append("right ");
            }
            else {
                sb.append("wrong ");
            }
        }
        String[] res = sb.toString().split(" ");
        for(String s: res){
            System.out.println(s);
        }
    }
}