import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // int
        System.out.print("Enter an Integer: ");
        int i = sc.nextInt();

        // long
        System.out.print("Enter a Long: ");
        long l = sc.nextLong();

        // float
        System.out.print("Enter a Float: ");
        float f = sc.nextFloat();

        // double
        System.out.print("Enter a Double: ");
        double d = sc.nextDouble();

        // boolean
        System.out.print("Enter a Boolean (true/false): ");
        boolean b = sc.nextBoolean();

        // char
        System.out.print("Enter a Character: ");
        char ch = sc.next().charAt(0);

        // String (one word)
        System.out.print("Enter one word: ");
        String word = sc.next();

        // String (full line)
        sc.nextLine(); // Buffer clear
        System.out.print("Enter a full sentence: ");
        String line = sc.nextLine();

        // Output
        System.out.println("\n----- OUTPUT -----");
        System.out.println("Integer : " + i);
        System.out.println("Long    : " + l);
        System.out.println("Float   : " + f);
        System.out.println("Double  : " + d);
        System.out.println("Boolean : " + b);
        System.out.println("Character: " + ch);
        System.out.println("Word    : " + word);
        System.out.println("Sentence: " + line);

        sc.close();
    }
}