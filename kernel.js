//epanechnikov kernel
function parabolic(u){
    if (Math.abs(u)<=1) return 0.75*(1-u*u)
    return 0
};

gauss = u=>Math.exp(-u*u/2)/Math.sqrt(2*3.14159265)


//n is parameter of choice
function smooth(x,y,n){
    var tmpy =[],tmp=0;
    for (let xx of x){
        let num=0, dem =0;
        for(let i=0; i<x.length; i++){
            tmp = gauss((x[i]-xx)/n);
            num+= tmp*y[i];
            dem+= tmp;
        };
        tmpy.push(num/dem);
    }
    return tmpy;
};

