import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine();

        String[] psList = new String[n];
        for(int i = 0; i < n; i++){
            psList[i] = sc.nextLine();
        }

        String[] res = new String[n];
        for(int i=0; i<n; i++){
            Stack<Integer> opened = new Stack<>();
            for(int j=0;j<psList[i].length();j++){
                char x = psList[i].charAt(j);
                if(x=='('){
                    opened.push(j);
                }
                else{
                    if(opened.isEmpty()){
                        opened.push(j);
                        break;
                    }
                    else{
                        opened.pop();
                    }
                }
            }
            if(opened.isEmpty()){ 
                res[i] = "YES";
            }
            else{
                res[i] = "NO";
            }
        }

        for(String s: res){
            System.out.println(s);
        }
    }
}