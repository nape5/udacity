const wrapper = document.querySelector('.wrapper');
const form = wrapper.querySelectorAll('.form');
const submitInput = form[0].querySelector('input[type="submit"]');
const tableLoc= document.getElementById("pixelCanvas");

//calls the function to get the form object
function getDataForm(e){

// stops the default behaviour of submit input refreshing page
  e.preventDefault();

  var formData = new FormData(form[0]);

  var inputHeight=  formData.get('height');

  var inputWidth= formData.get('width');

//calls loop function to dynamically create table
  var tb = createTable(inputWidth, inputHeight);

  tableLoc.appendChild(tb);
}

//Waits for Dom to finish loading then adds an event listener to the submit button.

document.addEventListener('DOMContentLoaded',function(){

  submitInput.addEventListener('click',getDataForm, false);

},false);



function createTable(inputWidth, inputHeight) {

//clears out existing table element html
  tableLoc.innerHTML= "";

//creates new table, the attribute is not necessary but used for console.log testing.
  var tb = document.createElement('table');
  tb.setAttribute("id","userTable");

  for (var i = 0; i < inputWidth; i++) {
    var row = document.createElement('tr');
    for (var j = 0; j < inputHeight; j++) {
      var column = document.createElement('td');
      row.appendChild(column);
    }
    tb.appendChild(row);
  }
  return tb;
}

// adds eventlistener to document and searched for specific target match based on nodeName.
//This is to allow for dyanmic creation of table cells.
document.addEventListener('click',function(e){
   if(e.target.nodeName =='TD'){
     e.target.style.backgroundColor= selectColor();
    }
    })
;

//created a function for getting the color input value.
selectColor = function () {
  const inputColor = document.getElementById('colorPicker');
  return inputColor.value;
}
