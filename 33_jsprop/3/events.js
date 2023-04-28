// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented? It will stop the row info from being displayed after the cell info is displayed
  e.stopPropagation();
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)

//table.addEventListener('click', clicky, true); // Boolean might be the cancellable parameter I saw in the documentation when looking at preventDefault()
table.addEventListener('click', clicky, false); // Prediction: maybe false will make it not cancellable by stopPropagation(), so it will run like that wasn't there.
// Actual: the true makes it so the tables info is shown first. False is the default (if nothing is specified) and the order will be cell, row, table.

// Q: When user clicks on a cell, in what order will the pop-ups appear?
// For some reason now it now goes in table, cell, row order. It seems that the true parameter causes this
// as the one with the false parameter runs like previously in cell, row, table order.