<div align="center">


<h3>INTELLIGENT CHATBOT USING 
NATURAL LANGUAGE PROCESSING
</h3>

</div>


<div align="center">

Digitization is transforming society into a mobile-first population. As messaging   applications grow in popularity, chatbots are increasingly playing an important role in this mobility-driven transformation. Chatbots allow businesses to connect with customers in a personal way without the expense of human representatives. Chatbots have become popular as a time and money saver for businesses  and an added convenience for customers.


<b>The project aims to have a fully functional personal assistant, making the world a more efficient and connected place to live and work.</b>



</div>

### CHATBOT

Chatbots have come a long way , but building a Chatbot using Natural Language Processing would be a challenging task. Chatbot is a computer program that simulates and processes human conversation, allowing humans to interact with digital devices as if they were communicating with a real person. 


### OBJECTIVE OF THE PROJECT

Chatbot could be implemented and be perfect for :

- Delivering more natural experiences with a virtual agents. 

- Provides rich and flexible interactions as they happen in the real world. 

- Improve customer engagement.

- Technological advantages to stay competitive in the market.

- Reduces cost and boost operational efficiency.

### APLLICATION OF THE PROJECT

Interesting applications of chatbots in various industries:
- Travel such as Book Flights
- Health Care
- E-commerce
- Education
- Finance




#### Let’s see how the Training Data is being loaded

Here we will be using libraries like JSON, Natural Language Toolkit (NLTK), pickle for serialization, Numpy, TensorFlow and Keras. 

<b>Tokenization</b> means to split up the text into individual words.

<b>Lemmatizer</b> we will lemmatize the individual words by creating a lemmatizer. Lemmatizer reduces the words to its stem or lemma.

<b>Sequential Model</b> a Deep Learning model from Keras. Sequential model is being used to build the neural network.

### SEQUENTIAL MODEL

The Sequential model is a linear stack of layers. It allows us to specify a neural network, precisely, sequentially from input to output, passing through a series of neural layers, one after the other.


#### LAYERS USED IN SEQUENTIAL MODEL

- Input Layer that is a Dense Layer with 128 & 64 neurons and input shape dependent on the size of the training data and activation function is Rectified Linear Unit (ReLU).
- Dropout Layer that randomly drops 50% of the previous layer's outputs during training to further reduce overfitting.
- Dense Layer with the number of neurons equal to the number of classes in the output layer.
- Softmax activation function to obtain the probability distribution of the classes.


#### BUILDING A CHATBOT APPLICATION THAT USES THE TRAINED MODEL

We create a Chatbot application that uses the trained model.
Four different functions are used:
- <b>Cleaning up sentence</b>
This function returns the preprocessed sentence as a list of words.
- <b>Getting Bag of Words</b>
The second function is used for converting a sentence into a bag of words that is a list full of 0’s and 1’s that indicates that the word is there or not. It returns the bag of words vector as a Numpy array.
- <b>Predicting the classes from sentences</b>
 Returns the list of tuples as the predicted classification for the input sentence. 
- <b>Function to get response</b>
         The response() method is used to predict the intent of the input sentence and 
       then returns a response based on the predicted intent.


<b>Finally we can run the Chatbot and we will be able to chat with the Chatbot.</b>

### INFERENCE

The expected outcome of this project is to build a Chatbot. Following a logical process, with neural networks, and limited amount of lines of code, we can understand the natural language very well for Chatbot environments.
- Chatbot helps in enhancing the processes and elevates experiences to the next level while also increasing the overall growth and profitability.

- Technological advantages to stay competitive in the market.

- It saves time, effort, and costs that further leads to increased customer satisfaction and increased engagement in any business.









