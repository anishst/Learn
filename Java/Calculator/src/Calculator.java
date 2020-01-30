
// this is the class
public class Calculator {

	//class constructor - method having same name as the class
	// get called automatically
	public Calculator() {
		
		System.out.println("Calling contructor");
		
	}
	
	public void add() {
		// add method
		System.out.print("adding number");
	}

	public void substract() {
		// add method
		System.out.print("subtracting number");
	}

	public static void main(String[] args) {
		// this is the main program - all programs should have this

		
		Calculator calc = new Calculator();
		calc.add();
		
		new Calculator().add();

	}

}
