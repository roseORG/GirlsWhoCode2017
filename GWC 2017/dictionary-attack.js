var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "dictionary.txt";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {

var pw = document.getElementBy("pw").value.toLowerCase();


for (i = 0; i < wordsList.length; i++){
  if(pw == wordsList[0])
  { var pw = document.getElementBy break;  
  }
  text += ""

  }


}

}
