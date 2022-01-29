# Frequency_guesser

This program uses two algorythms to crack passwords that are English words. The first algorythm systematically goes through all the letter combinations untill it gets the password, while the second makes educated gueses about each letter based on the commonallity of that letter in English and the position of it in the word as well as the previous letter. The goal of this demo is to show yo uhow important it is not to make your passwords English words or even modifications of them.

Clone the repo and run make to test the simulation. By default, it cracks 500 4-character-or-less passwords with both algorythms and then shows you the time it took each and the ratio between them. If you go into the code, you can edit the length of the passwords as well as the number of tests (keep in mind that every new character will dramatically increase the time it takes to crack)
