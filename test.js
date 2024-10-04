// Create a button element
const button = document.getElementById("button");
const progressDiv = document.getElementById("progress");
button.innerText = "Click Me";

// Append the button to the body
document.body.appendChild(button);

const widthList = ["_30", "_70", "_100"];
const current = 0;
// Add an event listener to the button
button.addEventListener("click", function () {
  // Loop list of widths when clicking button
  const current = widthList.indexOf(progressDiv.className);
  progressDiv.className = widthList[current + 1];
});
