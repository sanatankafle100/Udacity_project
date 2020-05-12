var heightElm, widthElm, color, table, line;
var tableSize = document.querySelector("#sizePicker");

document.getElementById("pixelCanvas").addEventListener("click", function ()
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

document.querySelector("#sizePicker")tableSize.addEventListener("submit", function (event)
{
    event.preventDefault();
    heightElm = document.getElementById("inputHeight").value;
    widthElm = document.getElementById("inputWidth").value;
    makeGrid(heightElm, widthElm);
});

function makeGrid(ht, wd)
{

    var boxs = 1;
    var row = document.getElementById("table" + boxs);
    while (row !== null)
    {
        ++boxs;
        row.remove();
        row = document.getElementById("table" + boxs);
    }

    table = document.querySelector("#pixelCanvas");
    for (var i = 1; i <= ht; i++)
    {
        table.insertAdjacentHTML("afterbegin", "<tr id = table" + i + "></tr>");
        line = document.querySelector("#table" + i);
        for (var j = 1; j <= wd; j++)
        {
            line.insertAdjacentHTML("afterbegin","<td id = box" + i + j +"></td>");
        }
    }

}
