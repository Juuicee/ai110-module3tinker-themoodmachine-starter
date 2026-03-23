# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

I compared using both models.

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

The rule-based model uses token scoring, and negation rules, while the ML model trains a logistic regression classifier on a bag-of-words representation.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).

Rule-based scoring rules: The rule-based model converts text into lowercase tokens, adds +1 for each positive word, subtracts -1 for each negative word, flips sentiment after negations,, and assigns “mixed” when conflicting signals appear near zero.

ML version: The ML model converts text posts into numeric vectors using a bag-of-words representation and trains a logistic regression classifier to predict labels based on patterns learned from the dataset.


## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

The dataset contains 14 short posts with slang, emojis, sarcasm, and mixed emotions, manually labeled as positive, negative, neutral, or mixed.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

The rule-based model scores positive words +1, negative words -1, applies negation, and assigns mixed labels when scores conflict near zero, performing well on obvious sentiment but failing on sarcasm, subtlety, or unfamiliar slang.

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

The ML model uses a bag-of-words representation trained on SAMPLE_POSTS and TRUE_LABELS, automatically learning patterns but overfitting on small data and misclassifying rare words or punctuation differently from the rule-based model.

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

The models are limited by small dataset size, inability to handle sarcasm or complex context, heavy reliance on word lists or labels, and testing only on short casual English posts.

## 7. Ethical Considerations

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

Misclassifying posts could be harmful, slang or dialects may be misinterpreted, and the models should not be used for decision-making or sensitive applications involving personal messages.

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only

Future improvements include expanding the labeled dataset, using TF-IDF or embeddings, enhancing rule-based preprocessing, implementing neural or transformer models, adding a proper test set, and exploring sarcasm-aware sentiment analysis.