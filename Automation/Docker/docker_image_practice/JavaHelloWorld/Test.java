public class Test {
	// program will output Hello World if no args are provided

	public static void main(String[] args) {
		// if name arg is provided then show Hello name 
		if(args.length == 0) {
			System.out.println("Hello world!");
		} else {
			System.out.println("Hello " + args[0] + "!");
		}
		

	}
}