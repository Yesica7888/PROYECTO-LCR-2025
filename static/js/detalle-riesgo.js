document.addEventListener("DOMContentLoaded", () => {
    const contenedor = document.getElementById("det-dinamico");
    const collapseLog = document.getElementById("collapse-det");
    const collapse = new bootstrap.Collapse(collapseLog, { toggle: false });

    document.querySelectorAll("[data-detalle]").forEach(btn => {
        btn.addEventListener("click", async () => {
            const tipo = btn.dataset.detalle;
            contenedor.innerHTML = "Cargando...";

            try {
                const response = await fetch(`/detalle/${tipo}`);
                const data = await response.json();

                //ver si esta llegando la informacion
                console.log(data);


                // Si el collapse está abierto:
                if (collapseLog.classList.contains("show")) {
                    // Cerrar primero
                    collapse.hide();

                    // Esperar a que termine de cerrarse antes de continuar
                    const waitForHidden = new Promise(resolve => {
                        collapseLog.addEventListener(
                            "hidden.bs.collapse",
                            () => resolve(),
                            { once: true } // se ejecuta una sola vez
                        );
                    });

                    await waitForHidden; // esperamos el cierre completo
                }

                let html = `<h5>${data.mensaje}</h5>`;

                if (data.diagnosticos) {

                   html += `<canvas id="graficoDashboard"></canvas>`;
                }

                // Actualizar contenido y abrir

                contenedor.innerHTML = html;
                collapse.show();

                // "diagnosticos" nombre del return en formato JSON del controlador (ruta /detalle(tipo))
                if(data.diagnosticos){

                    const ctx = document.getElementById("graficoDashboard");

                    // destruir gráfico si existe
                    if (chart) {
                        chart.destroy();
                    }

                    // Creacion del grafico de barras 
                    var chart = new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: data.diagnosticos,
                            datasets: [{
                                data: data.total,
                                backgroundColor: "rgba(2,117,216,1)",
                                borderColor: "rgba(2,117,216,1)",

                            }],

                        },
                        options: {
                            scales: {
                                xAxes: [{
                                    time: {
                                        unit: 'diagnosticos'
                                    },
                                    gridLines: {
                                        display: false
                                    },
                                    ticks: {
                                        maxTicksLimit: 11
                                    }
                                }],
                                yAxes: [{
                                    ticks: {
                                        min: 0,
                                        maxTicksLimit: 5
                                    },
                                    gridLines: {
                                        display: true
                                    }
                                }],
                            },
                            legend: {
                                display: false
                            }
                        }
                    });
                }
     
                    
            }catch (error) {
                contenedor.innerHTML = "Error cargando el detalle.";
                console.error(error);
            }
        });
    });
});

//arreglar en JS si esta abierto que cambie el contenido. No que lo cierre 