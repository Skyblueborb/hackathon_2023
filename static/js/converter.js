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


