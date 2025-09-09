// fuente 
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';


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

