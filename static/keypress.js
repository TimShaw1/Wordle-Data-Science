let i = 0;  //columns
let j = 0;  //rows

// referenced from https://stackoverflow.com/questions/1846599/how-to-find-out-what-character-key-is-pressed
// get input key
document.onkeydown = function(evt) {
    let id = j.toString().concat(",",i.toString());
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;

        // if backspace or delete are pressed, delete previous character
        // and move back a position
        if (charCode == 8 || charCode == 46)
        {
            // ensure we don't go out of range for i
            if (i == 4)
            {
                if (document.getElementById(id).textContent == "_")
                {
                    i--;
                }
                document.getElementById(id).textContent = "_";
            }
            else
            // ensure we don't go out of range for i
            if (i > 0)
            {
                i--;
            }
            id = j.toString().concat(",",i.toString());
            document.getElementById(id).textContent = "_";


        }
        else
        // if we press enter, move down a row
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
            // Display character in correct box
            var charStr = String.fromCharCode(charCode);
            document.getElementById(id).textContent = charStr;
            // ensure we don't go out of range for i
            if (i < 4)
            {
                i++;
            }
        }
};