// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  //e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?

//Predict, then test...
//Prediction: when all are set to true, the information will be displayed in original order -> cell, row, table
//Actual: went in table, row, cell order. From first part of the "tree" to last.
//Q: What effect does the boolean arg have in each? When the boolean is set to true, the parent event is activated first before the
// events of the child tags of that event. Additionally, child events with the boolean set to true will also activate before the parent
// events that have it set to false, but will activate after the parent evetns that have it set to true.
//   (Leave exactly 1 version uncommented to test...)

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  //tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  //trs[x].addEventListener('click', clicky, false);
}

table.addEventListener('click', clicky, true);
//table.addEventListener('click', clicky, false);
