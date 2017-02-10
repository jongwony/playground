public class Intege {
	
	private int n;

	public Intege() {
		this.n = 0;
	}

	public Intege(int n){
		this.n = n;
	}

	// 제너릭을 적용하게 되면 많이 골치아파질듯 
	public int add(Intege a, Intege b){
		return a.n + b.n;
	}
	public int add(Natural a, Intege b){
		return a.n + b.n;
	}
	public int add(Intege a, Natural b){
		return a.n + b.n;
	}


	public int sub(Intege a, Intege b){
		return a.n - b.n;
	}
	public int sub(Intege a, Natural b){
		return a.n - b.n;
	}
	public int sub(Natural a, Intege b){
		return a.n - b.n;
	}



	public int mul(Intege a, Intege b){
		return a.n * b.n;
	}
	public int mul(Intege a, Natural b){
		return a.n * b.n;
	}
	public int mul(Natural a, Intege b){
		return a.n * b.n;
	}


	public int div(Intege a, Intege b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return a.n / b.n;
	}
	public double div

	public static void main(String[] args){
		Intege a = new Intege(-22);
		Intege b = new Intege(4);
		System.out.println(ret.div(a, b));
	}

}