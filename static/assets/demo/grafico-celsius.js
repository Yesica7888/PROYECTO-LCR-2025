// fuente 
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';


console.log("Mi script se está ejecutando");

var ctx = document.getElementById("celsius").getContext("2d");

//temperatura base normal 36.8 y 37.2
function temperaturaRectal() {

    return parseFloat((36.8 + Math.random() * 0.4).toFixed(1));

}

//diferencia de temperatura ventricular y rectal rango de hidrocefalia
function deltaVentricular() {

return parseFloat((0.4 + Math.random() * 0.8).toFixed(1));

}

//ruidoMax= 0.05 , pasos = cuantos grados de temp va a subir 7 cada 10min 

function simulacionTemperaturaVentricular(pasos, ruidoMax ) {
  var tempRectal = temperaturaRectal();
  var deltaVR = deltaVentricular();

  var tempVentricularMax = tempRectal + deltaVR;
  var valores = [];

  var incremento = (tempVentricularMax - tempRectal) / (pasos - 1);

  //temperatura aumenta progresivamente pero tiene variantes por refresh
  for (var i = 0; i < pasos; i++) {
    var tempBase = tempRectal + incremento * i;

    // ruido fisiológico
    var ruido = (Math.random() * 2 - 1) * ruidoMax;
    var tempFinal = tempBase + ruido;

    // asegurar coherencia fisiológica
    tempFinal = Math.min(tempVentricularMax, Math.max(tempRectal, tempFinal));

    valores.push(Number(tempFinal.toFixed(1)));
  }

  return valores;
  
}

var valoresCelsius = simulacionTemperaturaVentricular(7,0.05); 

var myAreaChart = new Chart(ctx, {
    type: 'line', // tipo de gráfico 

    data: {
        labels: ["0 min", "10 min", "20 min ", "30 min", "40 min", "50 min ", "60 min"], // eje X tiempo
        datasets: [{
            label: "Temperatura °C", // nombre de la serie
            data: valoresCelsius,   // temperatura generados aleatoriamente

            // Estilo de la línea
            lineTension: 0.3, // bordes suavizados
            backgroundColor: "rgba(2,117,216,0.2)", // color de relleno bajo la línea
            borderColor: "rgba(2,117,216,1)",       // color de la línea

            // puntos
            pointRadius: 5,                        // tamaño
            pointBackgroundColor: "rgba(2,117,216,1)",
            pointBorderColor: "rgba(255,255,255,0.8)",
            pointHoverRadius: 5,                   // accion dinamica al pasar mouse
            pointHoverBackgroundColor: "rgba(2,117,216,1)",
            pointHitRadius: 50,                    // área sensible al mouse (hover/click)
            pointBorderWidth: 2,                   // grosor del borde del punto

            fill: true // rellena debajo de la línea
        }]
    },

    options: {
        responsive: true, // ajusta el gráfico al tamaño del contenedor responsive

        plugins: {
            legend: {
                display: true, // descripcion
                position: "top"
            },
            title: {
                display: true, // título
                text: "Temperatura °C"
            }
        },

        scales: {
            y: {
                min: 36.5,  // valor mínimo del eje Y valor min de pic
                max: 38.5, // valor máximo del eje Y valor max en hidrocefalia
                ticks: {
                    stepSize: 1 // separación de las marcas (cada grado °C)
                    
                },
                grid: {
                    color: "rgba(0, 0, 0, .125)" //eje y lineas
                },
                title: {
                    display: true, // eje y titulo
                    text: "°C"
                }
            },
            x: {
                grid: {
                    display: false // oculta la grilla vertical
                },
                title: {
                    display: true, // título del eje X
                    text: "Tiempo"
                }
            }
        }
    }
});

