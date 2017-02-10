public class Complex {
	
	private double real;
	private double imag;
	// Side Effect가 이걸 말하는건가 
	private String z;

	public Complex() {
		this.real = 0;
		this.imag = 0;
	}

	public Complex(double real, double imag) {
		this.real = real;
		this.imag = imag;
	}

	// 제너릭 필요함
	private String complex2string(double real, double imag) {
		return Double.toString(real) +"+"+ Double.toString(imag)+"i";
	}

	public String add(Complex a, Complex b) {
		this.real = a.real + b.real;
		this.imag = a.imag + b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String add(Complex a, Real b) {
		this.real = a.real + b.real;
		this.imag = a.imag + b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String add(Complex a, Intege b) {
		this.real = a.real + (double)b.real;
		this.imag = a.imag + (double)b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String add(Complex a, Natural b) {
		this.real = a.real + (double)b.real;
		this.imag = a.imag + (double)b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String add(Real a, Complex b) {
		this.real = a.real + b.real;
		this.imag = a.imag + b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String add(Intege a, Complex b) {
		this.real = (double)a.real + b.real;
		this.imag = (double)a.imag + b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String add(Natural a, Complex b) {
		this.real = (double)a.real + b.real;
		this.imag = (double)a.imag + b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}


	public String sub(Complex a, Complex b) {
		this.real = a.real - b.real;
		this.imag = a.imag - b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String sub(Complex a, Real b) {
		this.real = a.real - b.real;
		this.imag = a.imag - b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String sub(Complex a, Intege b) {
		this.real = a.real - (double)b.real;
		this.imag = a.imag - (double)b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String sub(Complex a, Natural b) {
		this.real = a.real - (double)b.real;
		this.imag = a.imag - (double)b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String sub(Real a, Complex b) {
		this.real = a.real - b.real;
		this.imag = a.imag - b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String sub(Intege a, Complex b) {
		this.real = (double)a.real - b.real;
		this.imag = (double)a.imag - b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}
	public String sub(Natural a, Complex b) {
		this.real = (double)a.real - b.real;
		this.imag = (double)a.imag - b.imag;
		String ret = this.complex2string(this.real, this.imag); 
		System.out.println(ret);
		return ret;
	}



	public String mul(Complex a, Complex b) {
		this.real = a.real * b.real - a.imag * b.imag;
		this.imag = a.real * b.imag + a.imag * b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}
	public String mul(Complex a, Real b) {
		this.real = a.real * b.real - a.imag * b.imag;
		this.imag = a.real * b.imag + a.imag * b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}	
	public String mul(Complex a, Intege b) {
		this.real = a.real * (double)b.real - a.imag * (double)b.imag;
		this.imag = a.real * (double)b.imag + a.imag * (double)b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}
	public String mul(Complex a, Natural b) {
		this.real = a.real * (double)b.real - a.imag * (double)b.imag;
		this.imag = a.real * (double)b.imag + a.imag * (double)b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}
	public String mul(Real a, Complex b) {
		this.real = a.real * b.real - a.imag * b.imag;
		this.imag = a.real * b.imag + a.imag * b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}
	public String mul(Intege a, Complex b) {
		this.real = (double)a.real * b.real - (double)a.imag * b.imag;
		this.imag = (double)a.real * b.imag + (double)a.imag * b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}
	public String mul(Natural a, Complex b) {
		this.real = (double)a.real * b.real - (double)a.imag * b.imag;
		this.imag = (double)a.real * b.imag + (double)a.imag * b.real;
		String ret = this.complex2string(this.real, this.imag);
		System.out.println(ret);
		return ret;
	}




	public String div(Complex a, Complex b) {
		// if b.real==0 and b.imag==0
		this.real = (a.real * b.real + a.imag * b.imag)*(b.real * b.real + b.imag * b.imag);
		this.imag = (a.imag * b.real - a.real * b.imag)*(b.real * b.real + b.imag * b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}
	public String div(Complex a, Real b) {
		// if b.real==0 and b.imag==0
		this.real = (a.real * b.real + a.imag * b.imag)*(b.real * b.real + b.imag * b.imag);
		this.imag = (a.imag * b.real - a.real * b.imag)*(b.real * b.real + b.imag * b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}
	public String div(Complex a, Intege b) {
		// if b.real==0 and b.imag==0
		this.real = (a.real * (double)b.real + a.imag * (double)b.imag)*((double)b.real * (double)b.real + (double)b.imag * (double)b.imag);
		this.imag = (a.imag * (double)b.real - a.real * (double)b.imag)*((double)b.real * (double)b.real + (double)b.imag * (double)b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}
	public String div(Complex a, Natural b) {
		// if b.real==0 and b.imag==0
		this.real = (a.real * (double)b.real + a.imag * (double)b.imag)*((double)b.real * (double)b.real + (double)b.imag * (double)b.imag);
		this.imag = (a.imag * (double)b.real - a.real * (double)b.imag)*((double)b.real * (double)b.real + (double)b.imag * (double)b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}
	public String div(Real a, Complex b) {
		// if b.real==0 and b.imag==0
		this.real = (a.real * b.real + a.imag * b.imag)*(b.real * b.real + b.imag * b.imag);
		this.imag = (a.imag * b.real - a.real * b.imag)*(b.real * b.real + b.imag * b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}
	public String div(Intege a, Complex b) {
		// if b.real==0 and b.imag==0
		this.real = ((double)a.real * b.real + (double)a.imag * b.imag)*(b.real * b.real + b.imag * b.imag);
		this.imag = ((double)a.imag * b.real - (double)a.real * b.imag)*(b.real * b.real + b.imag * b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}
	public String div(Natural a, Complex b) {
		// if b.real==0 and b.imag==0
		this.real = ((double)a.real * b.real + (double)a.imag * b.imag)*(b.real * b.real + b.imag * b.imag);
		this.imag = ((double)a.imag * b.real - (double)a.real * b.imag)*(b.real * b.real + b.imag * b.imag);
		String ret = this.complex2string(this.real, this.imag);
		return ret;
	}

	public String toString() {
		return this.z;
	}

	public static void main(String[] args){
		Complex a = new Complex(2,3);
		Complex b = new Complex(1,2);
		Complex ret = new Complex();
		ret.mul(a,b);
	}
}

