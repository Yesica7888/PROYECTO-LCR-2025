document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btnConectar").addEventListener("click", conectar);
  document.getElementById("btnDesconectar").addEventListener("click", desconectar);

  consultarEstado();
});

async function consultarEstado() {
  const res = await fetch("/bluetooth/estado");
  const data = await res.json();
  actualizarEstado(data.estado);
}

async function conectar() {
  const res = await fetch("/bluetooth/conectar", { method: "POST" });
  const data = await res.json();
  actualizarEstado(data.estado);
}

async function desconectar() {
  const res = await fetch("/bluetooth/desconectar", { method: "POST" });
  const data = await res.json();
  actualizarEstado(data.estado);
}

function actualizarEstado(estado) {
  const estadoBluetooth = document.getElementById("estado");
  const btnConectar = document.getElementById("btnConectar");
  const btnDesconectar = document.getElementById("btnDesconectar");

  if (estado === "conectado") {
    estadoBluetooth.innerText = "Estado: Conectado ";
    estadoBluetooth.className = "mt-3 text-success";
    btnConectar.disabled = true;
    btnDesconectar.disabled = false;
  } else {
    estadoBluetooth.innerText = "Estado: Desconectado";
    estadoBluetooth.className = "mt-3 text-danger";
    btnConectar.disabled = false;
    btnDesconectar.disabled = true;
  }
}