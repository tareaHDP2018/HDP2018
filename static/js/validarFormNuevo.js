function validaDatos() {
	var nombreSimula = document.getElementById("nombreSimulacion").value;
	var lineas = document.getElementById("ex1").value;
	var temperaturaMax = document.getElementById("temperaturaMax").value;
	var temperaturaMin = document.getElementById("temperaturaMin").value;
	var humedad = document.getElementById("humedad").value;
	var altitud = document.getElementById("altitud").value;
	var luminosidad = document.getElementById("luminosidad").value;
	var distancia = document.getElementById("distanciaL").value;

	if(nombreSimula == ""){
		alert("Nombre requerido");
		return false;
	}

	if(lineas== ""){
		alert("Lineas requeridas");
		return false;
	}

	if(lineas > 99){
		alert("Ingrese un valor maximo de 99 lineas");
		return false;
	}

	if(temperaturaMax.value == ""){
		alert("Lineas requeridas");
		return false;
	}

	if(temperaturaMax.value > 45){
		alert("Ingrese un valor maximo de 45 grados centigrados");
		return false;
	}
	if(temperaturaMax.value < 25){
		alert("Ingrese un valor minimo de 25 grados centigrados")
	}
	for (i = 0;i< temperaturaMax.value.length; i++ ){
		if(isNaN(parseInt(temperaturaMax.value.charAt(i)))==true){
			alert("Solamente se permiten numeros en temperaturaMax");
			return false;
		}
	}

	if(temperaturaMin.value == ""){
		alert("Lineas requeridas");
		return false;
	}

	if(temperaturaMin.value.length < 5){
		alert("Ingrese un valor minimo de 5 grados centigrados");
		return false;
	}

	if(humedad.value == ""){
		alert("Lineas requeridas");
		return false;
	}

	if(humedad.value >= 1000 ){
		alert("Ingrese un valor maximo de 1000 ml");
		return false;
	}

	if(altitud.value == ""){
		alert("Lineas requeridas");
		return false;
	}

	if(altitud.value.length > 4500 ){
		alert("Ingrese un valor maximo de 4500 msnm");
		return false;
	}

	if(luminosidad.value == ""){
		alert("Lineas requeridas");
		return false;
	}

	if(luminosidad.value > 99){
		alert("Ingrese un valor maximo de 99");
		return false;
	}

	if(distancia.value == ""){
		alert("distancia requerida");
		return false;
	}

	if(distancia.value > 50 ){
		alert("Ingrese un valor maximo de 50 cm");
		return false;
	}
	


}