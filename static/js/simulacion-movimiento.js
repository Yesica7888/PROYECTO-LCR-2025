function mover(accion) {
  // ruta del back
  fetch('/movimiento/' + accion, {
    method: "POST"
  })
  .then(function(response) {
    return response.json();
  })
  //parrafo donde se muestra el estado en movimiento-bot.html
  .then(function(data) {
    document.getElementById("estadoMotor").innerText =
      'Estado: ' + data.estado + ' | Velocidad: ' + data.velocidad;
  })
  .catch(function(error) {
    console.error("Error:", error);
    alert("Error al mover el motor");
  });
}