$(document).ready(function(){
		$("#grafico").submit(function(e){
			e.preventDefault();
			$.ajax({
				url: $(this).attr('action'),
				type: $(this).attr('method'),
				data: $(this).serialize(),

				success:function(json){
                    var arrayColor = ['rgba(255, 99, 132, 0.5)','rgba(54, 162, 235, 0.5)','rgba(255, 206, 86, 0.5)','rgba(75, 192, 192, 0.5)','rgba(153, 102, 255, 0.5)','rgba(255, 159, 64, 0.5)','rgba(255, 100, 70, 0.5)','rgba(200, 120, 30, 0.5)','rgba(220, 70, 90, 0.5)'];
                    var arrayBorderColor = ['rgba(255,99,132,1)','rgba(54, 162, 235, 1)','rgba(255, 206, 86, 1)','rgba(75, 192, 192, 1)','rgba(153, 102, 255, 1)','rgba(255, 159, 64, 1)','rgba(255, 100, 70, 0.5)','rgba(200, 120, 30, 0.5)','rgba(220, 70, 90, 0.5)'];
					console.log(json['nodos']);
                    console.log(json.valida);
	                console.log(json.hidrico);
                    if(json.valida[0]==1){
                    var germi = json.nodos[0];
                    var germi2 = germi/5;
                    var germi3 = germi2;
                    var crecimiento = []
                    for(var i=0;i<5;i++){
                        crecimiento[i]=germi2;
                        germi2+=germi3;
                    }
                    var canvas = document.getElementById("chart").getContext('2d');
                    var myChart = new Chart(canvas, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2","Dia 3","Dia 4","Dia 5"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });
                    }
                    
                    if(json.valida[1]==1){
                    var emer = json.nodos[1];
                    var emer2 = emer/2;
                    var emer3 = emer2;
                    var crecimiento2 = [];
                    for(var i=0;i<2;i++){
                        crecimiento2[i]=emer2;
                        emer2+=emer3;
                    }
                    var canvas2 = document.getElementById("chart2").getContext('2d');
                     var myChart2 = new Chart(canvas2, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento2,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });
                    }

                    
                    if(json.valida[2]==1){
                    var hojaP = json.nodos[2];
                    var hojaP2 = hojaP/4;
                    var hojaP3 = hojaP2;
                    var crecimiento3 = [];
                    for(var i=0;i<4;i++){
                        crecimiento3[i]=hojaP2;
                        hojaP2+=hojaP3;
                    }
                    var canvas3 = document.getElementById("chart3").getContext('2d');
                    var myChart3 = new Chart(canvas3, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2","Dia 3","Dia 4"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento3,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });
                    }

                    
                    if(json.valida[3]==1){
                    var priHoja = json.nodos[3];
                    var priHoja2 = priHoja/5;
                    var priHoja3 = priHoja2;
                    var crecimiento4 = [];
                    for(var i=0;i<5;i++){
                        crecimiento4[i]=priHoja2;
                        priHoja2+=priHoja3;
                    }
                    var canvas4 = document.getElementById("chart4").getContext('2d');
                    var myChart4 = new Chart(canvas4, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2","Dia 3","Dia 4","Dia 5"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento4,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });
                    }

                    
                    if(json.valida[4]==1){
                    var terHoja = json.nodos[4];
                    var terHoja2 = terHoja/7;
                    var terHoja3 = terHoja2;
                    var crecimiento5 = [];
                    for(var i=0;i<7;i++){
                        crecimiento5[i]=terHoja2;
                        terHoja2+=terHoja3;
                    }  
                     var canvas5 = document.getElementById("chart5").getContext('2d');
                       var myChart5 = new Chart(canvas5, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2","Dia 3","Dia 4","Dia 5","Dia 6","Dia 7"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento5,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });
  
                    }

                    
                    if(json.valida[5]==1){
                    var preflo = json.nodos[5];
                    var preflo2 = preflo/9;
                    var preflo3 = preflo2;
                    var crecimiento6 = [];
                    for(var i=0;i<9;i++){
                        crecimiento6[i]=preflo2;
                        preflo2+=preflo3;
                    }
                      var canvas6 = document.getElementById("chart6").getContext('2d');  
                      var myChart6 = new Chart(canvas6, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2","Dia 3","Dia 4","Dia 5","Dia 6","Dia 7","Dia 8","Dia 9"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento6,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });

                    }

                    
                    if(json.valida[6]==1){
                    var flo = json.nodos[6];
                    var flo2 = flo/5;
                    var flo3 = flo2;
                    var crecimiento7 = [];
                    for(var i=0;i<4;i++){
                        crecimiento7[i]=flo2;
                        flo2+=flo3;
                    }

                     var canvas7 = document.getElementById("chart7").getContext('2d');  
                     var myChart7 = new Chart(canvas7, {
                        type: 'bar',
                        data: {
                            labels: ["Dia 1","Dia 2","Dia 3","Dia 4"],
                            datasets: [{
                                label: 'Crecimiento',
                                data: crecimiento7,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    }); 
                  }

                  if(true){
                    var ctx2 = document.getElementById('chart8').getContext('2d');
                    var chart2 = new Chart(ctx2,{
                        type: 'bar',
                        data: {
                            labels: json.fase,
                            datasets: [{
                                label: 'Crecimiento General',
                                data: json.nodos ,
                                backgroundColor: arrayColor,
                                borderColor: arrayBorderColor,
                                borderWidth: 1
                            }]
                        },
                        options: {
                            scales: {
                                yAxes: [{
                                    ticks: {
                                      beginAtZero:true
                                    }
                                }]
                            }
                        }
                    });
                  }

                  if(true){
                  var humedad = json.humedad;
                  var humedad2 = humedad/10;
                  var humedad3 = [];
                    for(var i =0;i<6;i++){
                        humedad3[i]=humedad2;
                    }
                    var ctx = document.getElementById('myChart').getContext('2d');
                    var chart = new Chart(ctx, {
                       type: 'line',
                          data: {
                              labels: ['0 a 10','11 a 20','21 a 30','31 a 40'],
                              datasets: [{
                                   label: 'Hidricos simulados',
                                   fill: false,
                                   backgroundColor: 'rgb(255, 99, 132)',
                                   borderColor: 'rgb(255, 99, 132)',
                                   data: humedad3,
                              }, {
                                   label: 'Hidricos optimo',
                                   fill: false,
                                   backgroundColor: 'rgb(40, 105, 220)',
                                   borderColor: 'rgb(40, 105, 220)',
                                   data: json.hidrico, 
                             }]
                          },
                        options: {
                           responsive: true,
                             title: {
                               display: true,
                                 text: 'Hidricos por periodo'
                            },
                        }
                    });
                  }                      
				}
			})
		})
	});