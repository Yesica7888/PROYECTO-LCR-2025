function mover(direccion) {
    fetch(`/movimiento/${direccion}`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("estadoMotor").innerText =
            `Estado: ${data.estado} | Velocidad: ${data.velocidad}`;
    })
    .catch(err => {
        console.error(err);
        alert("Error al mover el motor");
    });
}