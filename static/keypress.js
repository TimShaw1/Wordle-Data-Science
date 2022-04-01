let i = 0;  //columns
let j = 0;  //rows
let guess = "";

// https://stackoverflow.com/questions/40120915/javascript-function-that-returns-true-if-a-letter
// checks if a character is a letter
var isAlpha = function(ch){
    return /^[A-Z]$/i.test(ch);
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
          console.log(data);
        });
      })
      .catch(function (error) {
        console.log("Fetch error: " + error);
      });

  }


// referenced from https://stackoverflow.com/questions/1846599/how-to-find-out-what-character-key-is-pressed
// get input key
document.onkeydown = function(evt) {
    let id = j.toString().concat(",",i.toString());
    evt = evt || window.event;
    var charCode = evt.keyCode || evt.which;
    var charStr = String.fromCharCode(charCode);

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
            guess = guess.slice(0,-1);

        }
        else
        // if we press enter, move down a row
        if (charCode == 13)
        {
            if (j < 5 && i == 4 && guess.length == 5)
            {
                i = 0;
                j++;
                submit_message();
                guess = "";
            }
        }
        else 
        if (isAlpha(charStr))
        {
            // Display character in correct box
            document.getElementById(id).textContent = charStr;
            if (guess.length < 5)
            {
                guess = guess.concat(charStr);
            }
            else
            {
                guess = guess.slice(0,-1);
                guess = guess.concat(charStr);
            }

            // ensure we don't go out of range for i
            if (i < 4)
            {
                i++;
            }
        }
};