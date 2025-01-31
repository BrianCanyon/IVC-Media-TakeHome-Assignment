## Workbook Overview:
### The purpose of this workbook is to give a easily digestable example of text based categorization. It
### will include sample text data that is preprocessed, split into training and testing groups, and trained
### against a logisctial regression ML model. The accuracy percentage along with a few examples of predictions
### will be printed as output. Code comments will provide a high level overview of the steps to accomplish 
### this goal. 
### For this workbook to run locally on your machine, be sure to install 'nltk' and 'sklearn', this can be
### done by executing the following commands:
###     - 'pip install nltk'
###     - 'pip install scikit_learn'

# Libraries used throughout
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
# Necessary NLTK data
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# A ton of sample data I copy/pasted from ChatGPT
texts = [
    "The detective carefully examined the crime scene, searching for any clues.",
    "As they danced under the moonlight, they realized their love for each other.",
    "The spaceship landed on the strange alien planet, ready for exploration.",
    "The wizard cast a powerful spell, illuminating the dark forest.",
    "She found the ancient artifact hidden beneath the old oak tree.",
    "The robot uprising threatened the future of humanity.",
    "The pirate ship sailed across the seven seas in search of treasure.",
    "Their romance blossomed during the summer vacation.",
    "The hero embarked on a quest to save the kingdom.",
    "The scientist made a groundbreaking discovery in the lab.",
    "The detective carefully examined the crime scene, searching for any clues.",
    "As they danced under the moonlight, they realized their love for each other.",
    "The spaceship landed on the strange alien planet, ready for exploration.",
    "The wizard cast a powerful spell, illuminating the dark forest.",
    "She found the ancient artifact hidden beneath the old oak tree.",
    "The robot uprising threatened the future of humanity.",
    "The pirate ship sailed across the seven seas in search of treasure.",
    "Their romance blossomed during the summer vacation.",
    "The hero embarked on a quest to save the kingdom.",
    "The scientist made a groundbreaking discovery in the lab.",
    "The detective carefully examined the crime scene, searching for any clues.",
    "As they danced under the moonlight, they realized their love for each other.",
    "The spaceship landed on the strange alien planet, ready for exploration.",
    "The wizard cast a powerful spell, illuminating the dark forest.",
    "She found the ancient artifact hidden beneath the old oak tree.",
    "The robot uprising threatened the future of humanity.",
    "The pirate ship sailed across the seven seas in search of treasure.",
    "Their romance blossomed during the summer vacation.",
    "The hero embarked on a quest to save the kingdom.",
    "The scientist made a groundbreaking discovery in the lab.",
    "The detective carefully examined the crime scene, searching for any clues.",
    "As they danced under the moonlight, they realized their love for each other.",
    "The spaceship landed on the strange alien planet, ready for exploration.",
    "The wizard cast a powerful spell, illuminating the dark forest.",
    "She found the ancient artifact hidden beneath the old oak tree.",
    "The robot uprising threatened the future of humanity.",
    "The pirate ship sailed across the seven seas in search of treasure.",
    "Their romance blossomed during the summer vacation.",
    "The hero embarked on a quest to save the kingdom.",
    "The scientist made a groundbreaking discovery in the lab."
]
# The labels (genres) associated with the above text, indexed properly (again, thanks ChatGPT)
labels = [
    "Mystery", "Romance", "Science Fiction", "Fantasy", "Mystery", "Science Fiction", 
    "Adventure", "Romance", "Fantasy", "Science Fiction", "Mystery", "Romance", 
    "Science Fiction", "Fantasy", "Mystery", "Science Fiction", "Adventure", 
    "Romance", "Fantasy", "Science Fiction", "Mystery", "Romance", "Science Fiction", 
    "Fantasy", "Mystery", "Science Fiction", "Adventure", "Romance", "Fantasy", 
    "Science Fiction", "Mystery", "Romance", "Science Fiction", "Fantasy", "Mystery", 
    "Science Fiction", "Adventure", "Romance", "Fantasy", "Science Fiction"
]

# Text preprocessing function
def preprocess_text(text):
    # Tokenize the text (ie. converts a long string to a list of strings, also known as individual 'tokens')
    words = word_tokenize(text)
    
    # Remove stopwords (and, the, ect.)
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Lemmatize the words (converts each token (word) to its base form)
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word.lower()) for word in words]
    
    # Join words back into a single string
    return ' '.join(words)

# Loop that applies the above function to each value in the list of text strings
preprocessed_texts = [preprocess_text(text) for text in texts]

# Splitting data for testing and training
X_train, X_test, y_train, y_test = train_test_split(preprocessed_texts, labels, test_size=0.2, random_state=42)

# Vectorize the text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test_vec)

# Evaluate the model and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Print the predicted labels
for text, pred in zip(X_test, y_pred):
    print(f"Text: {text} -> Predicted Genre: {pred}")

## Conclusion:
### Note in the printed output of strings, they look very difficult to read! Recall the preprocessing steps
### against the text data, while it supports ML analysis, it does burdon a human reader. The accuracy of 100%
### is largely to be expected given made up chatGPT examples, real world data is much more messy and larger in
### scale. This workbook is just meant to be an example of how text categorization can be accomplished using 
### python and relevant frameworks.

# Saving the model and vectorizer so it can be imported in a different script
import pickle
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)
