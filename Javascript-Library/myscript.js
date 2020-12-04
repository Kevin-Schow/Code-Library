document.getElementById("demo").innerHTML = "Javascript!"

function hello(firstName) {
	return "𝙷𝚎𝚕𝚕𝚘 " + firstName;
}

function isNumber(searchValue) {
    var found = searchValue.search(/^(\d*\.?\d*)$/);
    if(found > -1) {
        return true;
    }
    else {
        return false;
    }
}

function addition() {
	var ourAnswer = document.getElementById("answer").value;
	isNaN(ourAnswer);

	if (!isNumber(ourAnswer)) {
		document.getElementById("output").innerHTML = ourAnswer + " Is Not A Number!";
	} else {
		if (ourAnswer == correctAnswer) {
			document.getElementById("output").innerHTML = "Correct! " + numOne + " + " + numTwo + " = " + correctAnswer;
		} else {
			document.getElementById("output").innerHTML = "Incorrect!";
		}
	}
}

function newCard() {
	document.getElementById("output").innerHTML = ""
	document.getElementById("answer").value = ""
	numOne = Math.floor(Math.random() * 10)+1
	numTwo = Math.floor(Math.random() * 10)+1
	correctAnswer = numOne + numTwo;
	document.getElementById("flashcard").innerHTML = numOne + " + " + numTwo;

}