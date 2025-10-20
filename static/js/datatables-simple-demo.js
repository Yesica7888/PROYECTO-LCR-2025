window.addEventListener('DOMContentLoaded', event => {
   
    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple, {
            labels: {
                placeholder: "Buscar diagnosticos...",
                perPage: "registros por página",
                noResults: "No se encontraron registros",
                info: "Mostrando {start} a {end} de {rows} registros"
            }
        });
    }
});
