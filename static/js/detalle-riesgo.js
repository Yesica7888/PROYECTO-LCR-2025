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
                const html = await response.text();

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

                // Actualizar contenido y abrir
                contenedor.innerHTML = html;
                collapse.show();

            } catch (error) {
                contenedor.innerHTML = "Error cargando el detalle.";
                console.error(error);
            }
        });
    });
});

//arreglar en JS si esta abierto que cambie el contenido. No que lo cierre 