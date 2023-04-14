function converter(){
  if (sessionStorage.getItem("buttonClicked") == 1){
      const myDiv = document.getElementById("PRZYCISK");
      myDiv.setAttribute("class", "btn btn-outline-danger");
      const alertPlaceholder = document.getElementById('ALERT')
      const appendAlert = (message, type) => {
        const wrapper = document.createElement('div')
        wrapper.innerHTML = [
          `<div class="alert alert-danger alert-dismissible" role="alert">`,
          `   <div>Błędne dane</div>`,
          '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
          '</div>'
        ].join('')
        alertPlaceholder.append(wrapper)
        }
      appendAlert();
  }else{
  const button = document.getElementById("PRZYCISK");
  button.addEventListener("click", function() {
    sessionStorage.setItem("buttonClicked", 1);
  });
  }
 }
function clearSessionStorage(){
    sessionStorage.setItem("buttonClicked", 0);
}
function onDollar(){
    const text = "Bony dolarowe to ciekawy element życia PRL. Były drukowanymi przez władze komunistyczne banknotami USD.\n Więcej informacji: https://pl.wikipedia.org/wiki/Bon_towarowy_PeKaO";
    alert(text)
}
function updateValue(slider){
    console.log("Slider value: " + slider.value);
	if(slider.value == 0){
		slider.classList.remove("slider-track-blue");
		slider.classList.remove("slider-track-green");
		slider.classList.add("slider-track-gold");
	}else if(slider.value == 1){
		slider.classList.remove("slider-track-blue");
        slider.classList.add("slider-track-green");
        slider.classList.remove("slider-track-gold");
	}else if(slider.value == 2){
        slider.classList.add("slider-track-blue");
        slider.classList.remove("slider-track-green");
        slider.classList.remove("slider-track-gold");
	}
}


