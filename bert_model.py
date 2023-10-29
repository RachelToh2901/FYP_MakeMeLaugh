import tensorflow as tf
import numpy as np
import transformers
import pandas as pd

checkpoint_path = './bert_model/finalcheckpoint.ckpt'
model = tf.keras.models.load_model(checkpoint_path)


def bert_rating(jokes):
    '''
    This function computes BERT-based ratings for a list of jokes.

    Parameters:
    jokes (list of str): A list of jokes for which ratings are to be computed.

    Returns:
    ndarray: An array of BERT-based ratings for the input jokes.
    '''
    df_jokes = pd.DataFrame(np.array(jokes), columns=['joke'])
    preds = make_predictions(model = model,submit_df = df_jokes)
    result_array = np.concatenate([arr.flatten() for arr in preds])
    return result_array

def make_predictions(model, submit_df):
    '''
    This function generates predictions using a BERT model for a provided DataFrame.

    Parameters:
    model: The BERT model used for predictions.
    submit_df (pd.DataFrame): The DataFrame containing text data for prediction.

    Returns:
    list: A list of predictions.
    '''
    submit_data = BertDataGenerator(
        submit_df["joke"].values.astype("str"),
        None,  # Replace with your input mask data if necessary
        batch_size=1,
        shuffle=False,
        include_targets=False,
    )

    predictions = []
    for data in submit_data:
      pred = model.predict(data, verbose=0)
      predictions.append(pred)
    return predictions

def top_5_jokes(a, b):
    '''
    This function sorts and returns the top 5 jokes based on a given list of values.

    Parameters:
    a: The list of jokes.
    b: The list of values associated with the jokes.

    Returns:
    list: The top 5 jokes based on the values.
    list: The corresponding top 5 values.
    '''
    pairs = list(zip(a, b))

    # Sort pairs based on values in b in descending order
    sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

    # Separate the sorted pairs back into separate lists a and b
    a, b = zip(*sorted_pairs)

    # Convert the sliced results into arrays
    a_array = np.array(a[:5]).tolist()
    b_array = np.array(b[:5]).tolist()

    return a_array, b_array


class BertDataGenerator(tf.keras.utils.Sequence):
    '''
    This class implements a data generator for BERT model input data.

    Parameters:
    full_texts (list of str): The input text data.
    labels (list of labels): The associated labels (if available).
    batch_size (int): The batch size for data generation.
    shuffle (bool): Whether to shuffle the data.
    include_targets (bool): Whether to include labels as targets in the generator.
    '''
    def __init__(
        self,
        full_texts,
        labels,
        batch_size=256,
        shuffle=True,
        include_targets=True,
    ):
        self.full_texts = full_texts
        self.labels = labels
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.include_targets = include_targets
        self.tokenizer = transformers.BertTokenizer.from_pretrained("bert-base-uncased", do_lower_case=True)
        self.indexes = np.arange(len(self.full_texts))
        self.on_epoch_end()

    def __len__(self):
        return len(self.full_texts) // self.batch_size

    def __getitem__(self, idx):
        indexes = self.indexes[idx * self.batch_size : (idx + 1) * self.batch_size]
        batch_texts = self.full_texts[indexes]

        encoded = self.tokenizer.batch_encode_plus(
            batch_texts.tolist(),
            add_special_tokens=True,
            max_length=512,
            return_attention_mask=True,
            return_token_type_ids=True,
            return_tensors="tf",
            truncation=True,
            padding='max_length'
        )

        input_ids = np.array(encoded["input_ids"], dtype="int32")
        attention_masks = np.array(encoded["attention_mask"], dtype="int32")
        token_type_ids = np.array(encoded["token_type_ids"], dtype="int32")

        if self.include_targets:
            labels = np.array(self.labels[indexes], dtype="float32")
            return [input_ids, attention_masks, token_type_ids], labels
        else:
            return [input_ids, attention_masks, token_type_ids]
        



if __name__ == "__main__":
    from chatgpt import chatgpt
    prompt = 'give me 7 jokes about monash for a 22 years old male who is chinese and stays in Malaysia'
    jokes = chatgpt(prompt)
    ratings = bert_rating(jokes)
    print(ratings)
    print(len(ratings))
    for i in range(len(jokes)):
        print(jokes[i])
        print(ratings[i])

    jokes, ratings = top_5_jokes(jokes, ratings)
    print(jokes)
    print(ratings)
    print(len(ratings))
    for i in range(len(jokes)):
        print(jokes[i])
        print(ratings[i])

    # model.summary()
    
