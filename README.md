Question-MCQS-Generator-Using-Machine-learning-NLP
Introduction:

Our project aims to generate multiple-choice questions (MCQs) using machine learning and natural language processing (NLP) techniques. MCQs are widely used in educational assessments to evaluate students' understanding of a given topic. By automating the generation of MCQs, educators can save time and effort while ensuring the quality and relevance of the questions.

INFORMATION
Initialize List for MCQs: It starts by creating an empty list to store the generated MCQs.

Generate MCQs for Each Sentence: It iterates through each sentence in the selected_sentences list.

Process Sentence with spaCy: It uses spaCy (nlp) to process each sentence and tokenize it.

Extract Nouns: It extracts nouns from the sentence by filtering tokens with the part-of-speech tag "NOUN".

Ensure Enough Nouns: It checks if there are at least two nouns in the sentence. If not, it continues to the next sentence.

Count Noun Occurrences: It counts the occurrence of each noun in the sentence.

Select Subject: It selects the most common noun in the sentence as the subject of the question.

Generate Question Stem: It creates the question stem by replacing the subject noun with a blank ("_______").

Generate Answer Choices: It generates answer choices by including the subject noun as one choice and randomly selecting three

distractors from the other nouns in the sentence.

Shuffle Answer Choices: It shuffles the answer choices to avoid any bias.

Append MCQ to List: It appends the generated MCQ (question stem, answer choices, and correct answer) to the list of MCQs.

Return MCQs: Finally, it returns the list of generated MCQs.

This code can to be a useful tool for automatically generating multiple-choice questions from text data, which could be helpful for educational purposes or generating practice quizzes. You can discuss how this functionality can save time for educators or content creators and how it leverages natural language processing techniques to automate the process. Additionally, you can mention potential improvements or customization options, such as adjusting the number of distractors or incorporating more sophisticated language processing techniques.

https://github.com/kartikmongia/MCQ-Generator-Application/issues/1#issue-2383865982
