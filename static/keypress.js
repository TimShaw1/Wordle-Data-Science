// get input key
let i = 0;
let j = 0;

document.onkeydown = function(evt) {
    let id = j.toString().concat(",",i.toString());
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;

        if (charCode == 8 || charCode == 46)
        {
            if (i == 4)
            {
                if (document.getElementById(id).textContent == "_")
                {
                    i--;
                }
                document.getElementById(id).textContent = "_";
            }
            else
            if (i > 0)
            {
                i--;
            }
            id = j.toString().concat(",",i.toString());
            document.getElementById(id).textContent = "_";


        }
        else
        if (charCode == 13)
        {
            if (j < 5)
            {
                i = 0;
                j++;
            }
        }
        else
        {

            var charStr = String.fromCharCode(charCode);
            document.getElementById(id).textContent = charStr;
            if (i < 4)
            {
                i++;
            }
        }
};