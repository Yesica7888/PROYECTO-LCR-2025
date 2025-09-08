// fuente 
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

/*
// Ejemplo 
  var ctx = document.getElementById("myAreaChart");
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ["Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
      datasets: [{
        label: "Sessions",
        lineTension: 0.3,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [10000, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
      }],
    },
    options: {
      scales: {
        xAxes: [{
          time: {
            unit: 'date'
          },
          gridLines: {
            display: false
          },
          ticks: {
            maxTicksLimit: 7
          }
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: 40000,
            maxTicksLimit: 5
          },
          gridLines: {
            color: "rgba(0, 0, 0, .125)",
          }
        }],
      },
      legend: {
        display: false
      }
    }
  });
*/
console.log("Mi script se está ejecutando");

var ctx = document.getElementById("pic").getContext("2d");

//valores aleatorios entre 15 y 40 la pic en hidrocefalia va normalmente entre 20-40mmHg

function simulacionPic(min,max,length){
  var valores = [];
    for (var i = 0; i < length; i++) {
        valores.push(Math.floor(Math.random() * (max - min + 1)) + min);  
    }
    return valores;
  }

var valoresPic = simulacionPic(15, 40, 7); //min de pic en hidrocefalia en 60s 

var myAreaChart = new Chart(ctx, {
    type: 'line', // tipo de gráfico 

    data: {
        labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"], // eje X tiempo
        datasets: [{
            label: "Presión intracraneal (mmHg)", // nombre de la serie
            data: valoresPic,   // PIC en hidrocefalia generados aleatoriamente

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
                text: "Simulación de presión intracraneal en hidrocefalia" 
            }
        },

        scales: {
            y: {
                min: 5,  // valor mínimo del eje Y valor min de pic
                max: 40, // valor máximo del eje Y valor max en hidrocefalia
                ticks: {
                    stepSize: 5 // separación de las marcas (cada 5 mmHg)
                },
                grid: {
                    color: "rgba(0, 0, 0, .125)" //eje y lineas
                },
                title: {
                    display: true, // eje y titulo
                    text: "mmHg"   
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

