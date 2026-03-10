document.addEventListener("DOMContentLoaded", () => {

    let chart = null
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

                let html = `<h5>${data.mensaje}</h5>`;

                if (data.diagnosticos) {

                    html += `<canvas id="graficoDashboard"></canvas>`;
                }

                // Actualizar contenido y abrir

                contenedor.innerHTML = html;

                collapse.show();
                
                // "diagnosticos" nombre del return en formato JSON del controlador (ruta /detalle(tipo))
                if (data.diagnosticos) {

                    const ctx = document.getElementById("graficoDashboard");

                    // destruir gráfico si existe
                    if (chart) {
                        chart.destroy();
                    }

                    // Creacion del grafico de barras 
                    chart = new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: data.diagnosticos,
                            datasets: [{
                                data: data.total,
                                backgroundColor: "rgba(2,117,216,1)",
                                borderColor: "rgba(2,117,216,1)",
                                barThickness: 13,
                                maxBarThickness: 20

                            }],

                        },
                        options: {
                            responsive: true,
                            scales: {
                                x: [{
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
                                y: [{
                                    ticks: {
                                        min: 0,
                                        maxTicksLimit: 10
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


            } catch (error) {
                contenedor.innerHTML = "Error cargando el detalle.";
                console.error(error);
            }
        });
    });
});

//arreglar en JS si esta abierto que cambie el contenido. No que lo cierre 