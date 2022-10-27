public class operation {
    static int counter=0;
    public static boolean isMandelbrot(double[] array,float power,int count,double[] offset){
        if(Math.sqrt(Math.pow(array[0],2)+Math.pow(array[1],2))<=2 && count>100){
            counter=count;
            return true;
        }else if(Math.sqrt(Math.pow(array[0],2)+Math.pow(array[1],2))>2){
            counter=count;
            return false;
        }else{
            array=computePower(array,power);
            array[0]=array[0]+offset[0];
            array[1]=array[1]+offset[1];
            count+=1;
            counter=count;
            return isMandelbrot(array,power,count,offset); 
        }
    }
    public static double[] computePower(double[] array,double power){
        double modulus=Math.sqrt(Math.pow(array[0],2)+Math.pow(array[1],2));
        if (modulus!=0){
            double angle=Math.atan2(array[1],array[0]);
            array[0]=Math.pow(modulus,power)*(Math.cos(power*angle));
            array[1]=Math.pow(modulus,power)*(Math.sin(power*angle));
            return array;
        }
        return array;
    }
}
