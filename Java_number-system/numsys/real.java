public class Real {
	
	private double n;

	public Real() {
		this.n = 0;
	}

	public Real(double n){
		this.n = n;
	}

	public double add(Real a, Real b){
		return a.n + b.n;
	}
	public double add(Real a, Intege b){
		return a.n + (double)b.n;
	}
	public double add(Intege a, Real b){
		return (double)a.n + b.n;
	}
	public double add(Real a, Natural b){
		return a.n + (double)b.n;
	}
	public double add(Natural a, Real b){
		return (double)a.n + b.n;
	}

	public double sub(Real a, Real b){
		return a.n - b.n;
	}
	public double sub(Real a, Intege b){
		return a.n - (double)b.n;
	}
	public double sub(Intege a, Real b){
		return (double)a.n - b.n;
	}
	public double sub(Real a, Natural b){
		return a.n - (double)b.n;
	}
	public double sub(Natural a, Real b){
		return (double)a.n - b.n;
	}


	public double mul(Real a, Real b){
		return a.n * b.n;
	}
	public double mul(Real a, Intege b){
		return a.n * (double)b.n;
	}
	public double mul(Intege a, Real b){
		return (double)a.n * b.n;
	}
	public double mul(Real a, Natural b){
		return a.n * (double)b.n;
	}
	public double mul(Natural a, Real b){
		return (double)a.n * b.n;
	}

	public double div(Real a, Real b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return a.n / b.n;
	}
	public double div(Real a, Intege b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return a.n / (double)b.n;
	}
	public double div(Intege a, Real b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return (double)a.n / b.n;
	}
	public double div(Real a, Natural b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return a.n / (double)b.n;
	}
	public double div(Natural a, Real b){
		if (b.n.equal(0)){ System.out.println("Divide 0!"); }
		return (double)a.n / b.n;
	}

}