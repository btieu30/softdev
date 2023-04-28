// demo 1
// JS event propagation

// Prediction: 2 row table with 3 items in each row. When you click on a table cell, it will print the content in the cell 1 time.
// Actual: opens a box with the text of the cell inside of it.
var tds = document.getElementsByTagName('td');

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}
