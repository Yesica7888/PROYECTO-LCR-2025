function mover(accion) {
  // ruta del back
  fetch('/movimiento/' + accion, {
    method: "POST"
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    document.getElementById("estadoMotor").innerText =
      'Estado: ' + data.estado + ' | Velocidad: ' + data.velocidad;
  })
  .catch(function(error) {
    console.error("Error:", error);
    alert("Error al mover el motor");
  });
}