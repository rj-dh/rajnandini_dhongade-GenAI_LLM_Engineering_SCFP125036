# Activity 2 — Tokenization Practical

## 1. What is Tokenization?

Tokenization is the process of breaking text into smaller units called tokens. These tokens can be words, parts of words, numbers, or punctuation marks. Language models convert text into tokens before processing it.

## 2. Practical Example

Sentence: `Hello, how are you?`

Example tokens:
- `Hello`
- `,`
- ` how`
- ` are`
- ` you`
- `?`

The exact tokens depend on the tokenizer used by the model.

## 3. Is One Word Always One Token?

No, one word is not always one token. Some words are represented by a single token, while longer or less common words may be divided into multiple tokens.

For example, a word like `playing` might be represented as one token or split into smaller parts, depending on the tokenizer.

## 4. Why Are Some Words Split?

Some words are split because tokenizers often use smaller, reusable units of text called subwords. This helps the model handle uncommon words, new words, and different word forms without needing a separate token for every possible word.

For example, a long or unfamiliar word may be divided into smaller parts that the tokenizer already recognizes.

## 5. What Happens to Punctuation?

Punctuation marks such as commas, full stops, question marks, and exclamation marks are also processed as tokens. Depending on the tokenizer, punctuation may receive its own token or be combined with nearby text.

For example, in `Hello!`, the word and the exclamation mark may be represented by separate tokens.

## 6. Why Does the Model Need Token IDs?

Language models cannot directly process text as humans read it. Therefore, each token is mapped to a numerical identifier called a token ID.

For example, a tokenizer might represent the text `Hello` using a token ID such as `15496`. This is only an illustrative example; actual IDs depend on the tokenizer.

The model processes these numerical representations to understand patterns in text and generate responses.

## 7. Conclusion

Tokenization converts text into smaller units that a language model can process. One word can correspond to one or multiple tokens, punctuation is also tokenized, and token IDs allow the model to work with numerical representations of text. Tokenization is an important step in how large language models process and generate language.
