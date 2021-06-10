var starClassArray = ["O", "B", "A", "F", "F", "F", "G", "G", "G", "G", "G", "G", "G", "K", "K", "K", "K", "K", "K", "K", "K", "K", "K", "K", "K", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M"];

function generateStarfield(starCount, containerSelector, avgFreq) {
  for (i = 0; i < starCount; i++) {
    x = Math.random() * 100;
    y = Math.random() * 100;
    magnitude = Math.random();
    starClass = starClassArray[Math.floor(Math.random() * starClassArray.length)];
    new Star(x, y, magnitude, starClass, i, containerSelector);
  }
  twinkleEvent(avgFreq, starCount);
}

function twinkleEvent(avgFreq, elementCount) {
  // -> removing the class
  var element = document.querySelector("#no" + Math.floor(Math.random() * elementCount));
  element.classList.remove("twinkle");

  // -> triggering reflow /* The actual magic */
  // without this it wouldn't work. Try uncommenting the line and the transition won't be retriggered.
  element.offsetWidth = element.offsetWidth;

  // -> and re-adding the class
  element.classList.add("twinkle");
  setTimeout(function() {
    twinkleEvent(avgFreq, elementCount);
  }, Math.random() * 1000 + 1000 / avgFreq);
}

function Star(x, y, magnitude, classString, number, containerSelector) {
  var starObject = document.createElement("div");
  var container = document.querySelector(containerSelector);
  starObject.className = "star " + classString;
  starObject.id = "no" + number;
  starObject.style.left = x + "%";
  starObject.style.top = y + "%";

  starObject.style.opacity = magnitude;

  starObject.style.position = "absolute";
  container.appendChild(starObject);
}

(function init() {
  generateStarfield(300, '.starfield', 500000);
})();
