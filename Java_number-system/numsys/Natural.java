public class Natural {
	
	private int n;

	public Natural() {
		this.n = 1;
	}

	public Natural(int n){
		if (n < 1) {
			System.out.println("Natural number > 0");
		}
		this.n = n;
	}

	public int add(Natural a, Natural b){
		System.out.println(a.n+b.n);
		return a.n + b.n;
	}

	public int sub(Natural a, Natural b){
		return a.n - b.n;
	}

	public int mul(Natural a, Natural b){
		return a.n * b.n;
	}

	public int div(Natural a, Natural b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return a.n / b.n;
	}

	public static void main(String[] args){
		Natural a = new Natural(2);
		Natural b = new Natural(5);
		Natural ret = new Natural();
		ret.add(a, b);
	}

}