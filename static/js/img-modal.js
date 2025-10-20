document.addEventListener('DOMContentLoaded', () => {
    // referencia al modal y la imagen interna con los id 
  const modal = document.getElementById('img-modal');
  const modalImg = document.getElementById('img-modal-js');

  modal.addEventListener('show.bs.modal', (event) => {
    // Boton que hace que se ejecute el modal
    const trigger = event.relatedTarget;
    const imgSrc = trigger.getAttribute('data-img');
    modalImg.src = imgSrc;
  });
 });

 