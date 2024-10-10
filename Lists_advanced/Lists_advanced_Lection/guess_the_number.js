function numberGuessingGame() {
    // Step 1: Generate a random number
    const randomNumber = Math.floor(Math.random());

    let guess = null; // User's guess
    let attempts = 0; // Count of attempts

    // Step 2: Loop until the guess is correct
    while (guess !== randomNumber) {
        // Prompt the user for their guess
        guess = Number(prompt("Guess the number: "));

        attempts++;

        // Step 3: Provide feedback based on the guess
        if (guess > randomNumber) {
            console.log("Too high! Try again.");
        } else if (guess < randomNumber) {
            console.log("Too low! Try again.");
        } else {
            console.log(`Congratulations! You guessed the number in ${attempts} attempts!`);
        }
    }

    // Step 4: Ask if the user wants to play again
    const playAgain = prompt("Do you want to play again? (y/n)");
    // If yes, restart the game
}

// To start the game, call the function:
numberGuessingGame();