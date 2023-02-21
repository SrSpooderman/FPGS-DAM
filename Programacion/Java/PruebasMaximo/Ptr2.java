public class Ptr2 {
    int ejex;
    int ejey;
    int area;
    /*Programa constructor*/
    public Ptr2(int ejex, int ejey){
        this.ejex = ejex;
        this.ejey = ejey;
        this.area = ejex * ejey;
    }
    public void SetEjeX(int x){
        this.ejex = x;
        this.area = this.ejex * this.ejey;
    }
}