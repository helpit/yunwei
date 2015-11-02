class Msg{
	private String txt;
	public Msg(String s){
		txt = s;
		}
	public void print(){
		System.out.println(txt);
		}
}

public class hello{
	public static void main(String args[]){
		Msg M = new Msg("hello world");
		M.print();
    int i = 0;
		}
}

