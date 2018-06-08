function myFunction() {
	var x = document.getElementById("id_fechaNacimiento_day");
     var y = document.getElementById("id_fechaNacimiento_month");
     var z= document.getElementById("id_fechaNacimiento_year");
      var botton = document.getElementById("registrar");
      var anio=parseInt(z.value);
      var comprobar=((anio%4 == 0) && (anio%100 != 0)) || (anio%400 == 0);
      var i=0;
     
    if((x.value=="31" && y.value=="2")){
     botton.disabled = true;
     alert("el dia no existe para el mes correspondiente");
     botton.disabled = false;
         }
    else if ((x.value=="29" && y.value=="2")&&(comprobar==false)){
	botton.disabled=true;
	alert("el año no es bisiesto");
	botton.disabled = false;
    }
    else if((x.value=="31" && y.value=="4")){
     botton.disabled = true;
    alert("el dia no existe para el mes correspondiente")
     botton.disabled = false;
    }
    else if((x.value=="31" && y.value=="6")){
     botton.disabled = true;
    alert("el dia no existe para el mes correspondiente")
     botton.disabled = false;
    }
    else if((x.value=="31" && y.value=="9")){
     botton.disabled = true;
     alert("el dia no existe para el mes correspondiente")
     botton.disabled = false;
     
    }
    else if((x.value=="31" && y.value=="11")){
     botton.disabled = true;
     alert("el dia no existe para el mes correspondiente")
     botton.disabled = false;
     
    }
    
    else{
    	botton.disabled=false;
    }





 
}


