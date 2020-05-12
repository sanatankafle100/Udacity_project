//To add or remove color to cells
document.getElementById("pixelCanvas").addEventListener("click", function (event)
{
   var color = document.getElementById("colorPicker").value;
   var click = event.target.id;
   var item = document.getElementById(click);
   var is_occupied = item.hasAttribute("style");
   if (is_occupied === true)
   {
       item.removeAttribute("style");
   }
   else
   {
       item.style.backgroundColor = color;
   }
});

//To take height and width from user and pass it to makeGrid
var tableSize = document.querySelector("#sizePicker");
tableSize.addEventListener("submit", function (event)
{
   event.preventDefault();
   var widthElm = document.getElementById("inputWidth").value;
   var heightElm = document.getElementById("inputHeight").value;
   makeGrid(heightElm, widthElm);
});

function makeGrid(ht, wd)
{
    //To reset the table
   var boxs = 1;
   var row = document.getElementById("table" + boxs);
   while (row !== null)
   {
       ++boxs;
       row.remove();
       row = document.getElementById("table" + boxs);
   }

   //to create take of given dimension
   var table = document.querySelector("#pixelCanvas");
   for (var i = 1; i <= ht; i++)
   {
       table.insertAdjacentHTML("afterbegin", "<tr id = table" + i + "></tr>");
       var line = document.querySelector("#table" + i);
       for (var j = 1; j <= wd; j++)
       {
           line.insertAdjacentHTML("afterbegin","<td id = cell" + i + j +"></td>");
       }
   }

}
