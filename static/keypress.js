let i = 0;  //columns
let j = 0;  //rows
let guess = "";
let colors = [];
let win = ['green', 'green', 'green', 'green', 'green'];

// https://stackoverflow.com/questions/40120915/javascript-function-that-returns-true-if-a-letter
// checks if a character is a letter
var isAlpha = function (ch) {
    return /^[A-Z]$/i.test(ch);
}

function checkWin(input) {
    for (var i = 0; i < 5; i++) {
        if (input[i] != "green") {
            return false;
        }
    }
    return true;
}

// https://pythonise.com/series/learning-flask/flask-and-fetch-api
function submit_message() {

    fetch(`${window.origin}/`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(guess),
        cache: "no-cache",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then(function (response) {
            if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                return;
            }
            response.json().then(function (data) {
                if (data["message"] == "invalid") {
                    console.log("Invalid");
                }
                else {
                    console.log(data);
                    colors = data["message"];
                    console.log(colors);
                    for (var k = 0; k < 5; k++) {
                        letter_id = j.toString().concat("/", k.toString());
                        console.log(letter_id);
                        document.getElementById(letter_id).style.background = colors[k];
                    }
                    // Reset column and move down 1 row
                    i = 0;
                    j++;
                    guess = "";

                    // If we win, stop taking guesses
                    if (checkWin(colors)) {
                        j = -1;
                        return;
                    }
                }
            });
        })
        .catch(function (error) {
            console.log("Fetch error: " + error);
        });

}


// referenced from https://stackoverflow.com/questions/1846599/how-to-find-out-what-character-key-is-pressed
// get input key
document.onkeydown = function (evt) {
    let id = j.toString().concat(",", i.toString());
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var charStr = String.fromCharCode(charCode);

    // if backspace or delete are pressed, delete previous character
    // and move back a position
    if (charCode == 8 || charCode == 46) {
        // ensure we don't go out of range for i
        if (i == 4) {
            if (document.getElementById(id).textContent == "_") {
                i--;
            }
            document.getElementById(id).textContent = "_";
        }
        else
            // ensure we don't go out of range for i
            if (i > 0) {
                i--;
            }
        id = j.toString().concat(",", i.toString());
        document.getElementById(id).textContent = "_";
        guess = guess.slice(0, -1);

    }
    else
        // if we press enter, move down a row
        if (charCode == 13) {
            if (j < 6 && i == 4 && guess.length == 5) {
                submit_message();
            }
        }
        else
            if (isAlpha(charStr)) {
                // Display character in correct box
                document.getElementById(id).textContent = charStr;
                if (guess.length < 5) {
                    guess = guess.concat(charStr);
                }
                else {
                    guess = guess.slice(0, -1);
                    guess = guess.concat(charStr);
                }

                // ensure we don't go out of range for i
                if (i < 4) {
                    i++;
                }
            }
};