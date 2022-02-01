var fwd = document.getElementById("fwd");
var bwd = document.getElementById("bwd");
var left = document.getElementById("left");
var right = document.getElementById("right");
var halt = document.getElementById("halt");

fwd.onclick = function () {
  fetch("/fwd")
    .then((response) => response.json())
    .then((data) => console.log(data));
};

halt.onclick = function () {
  fetch("/halt")
    .then((response) => response.json())
    .then((data) => console.log(data));
};

right.onclick = function () {
  fetch("/right")
    .then((response) => response.json())
    .then((data) => console.log(data));
};

left.onclick = function () {
  fetch("/left")
    .then((response) => response.json())
    .then((data) => console.log(data));
};
bwd.onclick = function () {
  fetch("/bwd")
    .then((response) => response.json())
    .then((data) => console.log(data));
};
