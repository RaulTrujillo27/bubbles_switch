var indice= 0;

AFRAME.registerComponent('change-data', {
    init: function(){
      this.el.addEventListener('click', function(){
            var burbujas = document.querySelector('#bubblesrealdata');
            var datos = document.querySelectorAll('[babia-queryjson]');
            indice = indice +1;
            if(indice==datos.length){
                indice = 0;
            }
            burbujas.setAttribute('babia-bubbles','from',datos[indice].id);
      })
      
    }             
  });