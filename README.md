# mcq-randomizer

This program randomizes multiple choice tests to create multiple version of
a test.

It takes in a test and answer key, and produces randomized test with a matching answer key.

Currently the input files are hardcoded, so you must place them in the same
folder as the script and name them input_test.txt and input_answers.txt. This may be more convenient for people using not using this script from the command line. Or you are welcome to modify the program.

Each time you execute the program a new random version is generated.

The generated output files have a unique id postfix, so you can identify
the question/answerkey pair.

It has not been generalized yet, so your input test and answers must meet some formating
requirements:
- The input files must be text files.
- Questions must be identified by a unique number, and the number must be followed by a '.'
- Choices must be indentified by a letter [a:f, A:F], followed by a '.' Choice identifiers
  must be unique for that question.
- Each choice must be on a new line.
- Your answer key must have the same number of answers as your test.
- Your answers in your answer key must be one of the choice identifiers in your
  question.

example question format (question order, spacing and indentation don't matter):

3.  Question text  
a.  choice text  
b.  choice text  
c.  choice text  

example answer key (answer order, spaceing, case, indentation don't matter):

1. A
2. b
3. c
4. B


