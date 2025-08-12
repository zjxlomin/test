import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        int[] res = new int[n];
        for(int i=0;i<n;i++){
            String quiz = sc.nextLine();
            int c = 0;
            int score = 0;
            for(int j=0;j<quiz.length();j++){
                if(quiz.charAt(j)=='O'){
                    c++;
                    score+=c;
                }
                else{
                    c=0;
                }
            }
            res[i]=score;
        }
        for(int s: res){
            System.out.println(s);
        }
    }
}