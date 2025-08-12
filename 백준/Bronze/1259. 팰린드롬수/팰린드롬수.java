import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        StringBuffer sb = new StringBuffer();
        while(true){
            String str = sc.nextLine();
            if(str.equals("0")) {
                break;
            }
            else {
                str+=" ";
                sb.append(str);
            }
        }
        String[] words =  sb.toString().split(" ");
        for(String word: words){
            StringBuffer wb = new StringBuffer(word);
            if(word.equals(wb.reverse().toString())){
                System.out.println("yes");
            }
            else {
                System.out.println("no");
            }
        }
    }
}