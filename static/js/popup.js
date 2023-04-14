const popup = document.querySelector(".popup");
const popupContent = popup.querySelector(".popup-content");
const popupImage = popup.querySelector(".popup-image");
const popupText = popup.querySelector(".popup-text");
const popupClose = popup.querySelector(".popup-close");
const popupLink = document.querySelectorAll(".popup-link");

popupLink.forEach((link) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const imgSrc = link.querySelector("img").getAttribute("src");
    const imgAlt = link.querySelector("img").getAttribute("alt");
    const map = link.querySelector("map");
    const mapName = map.getAttribute("name");
    const mapAreas = map.querySelectorAll("area");
    let coords = "";

    mapAreas.forEach((area) => {
      if (area.getAttribute("shape") === "rect") {
        coords = area.getAttribute("coords");
      }
    });

    popupImage.setAttribute("src", imgSrc);
    popupImage.setAttribute("alt", imgAlt);
    popupImage.setAttribute("usemap", "#" + mapName);

    popupText.textContent = imgAlt;

    const [x1, y1, x2, y2] = coords.split(",");

    const imgWidth = parseInt(x2) - parseInt(x1);
    const imgHeight = parseInt(y2) - parseInt(y1);

    if (imgWidth > imgHeight) {
      popupImage.style.maxWidth = "40%";
      popupImage.style.maxHeight = "30%";
    } else {
      popupImage.style.maxWidth = "30%";
      popupImage.style.maxHeight = "40%";
    }
    popup.style.display = "block";
  });
});

popupClose.addEventListener("click", () => {
  popup.style.display = "none";
});

popup.addEventListener("click", (e) => {
  if (e.target === popup) {
    popup.style.display = "none";
  }
});
