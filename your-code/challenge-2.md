![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Challenge 2: Tensorflow Hyperparameter Tuning

## Getting Started

From the lesson and Challenge 1 you should have noticed that understanding the concepts in neural network analysis such as *learning rate*, *epoch*, *optimizer*, *loss function* and so on is essential for you to optimize the neural network models you build. In this challenge you will study several learning pieces that discuss the hyperparameters in Tensorflow. 

**[Neural Networks: Structure](https://developers.google.com/machine-learning/crash-course/introduction-to-neural-networks/anatomy)**

**[Understanding Deep Learning with TensorFlow Playground](https://medium.com/@andrewt3000/understanding-tensorflow-playground-c20cdb7a250b)**

After that, complete [this exercise](https://developers.google.com/machine-learning/crash-course/introduction-to-neural-networks/playground-exercises) on tuning the Tensorflow hyperpamameters in the [Tensorflow Playground](https://playground.tensorflow.org/).

Finally, using what you have learned, try tuning the hyperparameters for the spiral dataset in order to reach training and test loss <0.05 as shown in the following:

![spiral output](challenge-2.png)

After you're done, submit a screenshot of your Playground including the following information:

* Epoch
* Learning rate
* Activation function
* Features included
* Hidden layers and neurons
* Test and training loss

**Do not google for the end solution!**

MY ANSWER!!!!
# Challenge 2 - Tensorflow Hyperparameter Tuning
 
Dataset: Spiral
 
Configuration:
 
- Epoch: 500
- Learning Rate: 0.03
- Activation Function: Tanh
- Hidden Layers: 4
- Neurons per Layer: 8
- Features:
- X1
- X2
- X1²
- X2²
- X1X2
- sin(X1)
- sin(X2)
 
Results:
 
- Training Loss: 0.005
- Test Loss: 0.001
 
The model successfully achieved training and test loss below 0.05. I added the screenshot here in a sub file titled "TensorFlow Hyperparameter Test_Lab Challange 2"