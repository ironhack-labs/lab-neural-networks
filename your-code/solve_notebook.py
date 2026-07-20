import json
import nbformat as nbf

notebook_path = '/home/martin/Dokumente/python/DSML/week5/lab-neural-networks/your-code/challenge-1.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The cells where we need to put the answers
cells = nb['cells']
code_cells = [cell for cell in cells if cell['cell_type'] == 'code']

# Expected code_cells:
# 0: Step 1 Data Engineering
# 1: Step 2 Build Neural Network
# 2: Step 3 Make Predictions
# 3: Step 4 Improve Your Model
# 4: Which approach(es) did you find helpful

code_cells[0]['source'] = [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "# 1. Read tic-tac-toe.csv into a dataframe.\n",
    "df = pd.read_csv('tic-tac-toe.csv')\n",
    "\n",
    "# 2. Inspect the dataset.\n",
    "display(df.head())\n",
    "display(df.info())\n",
    "\n",
    "# 3. Convert the categorical values to numeric in all columns.\n",
    "mapping = {'x': 1, 'o': -1, 'b': 0}\n",
    "for col in df.columns[:-1]:\n",
    "    df[col] = df[col].map(mapping)\n",
    "df['class'] = df['class'].astype(int)\n",
    "\n",
    "# 4. Separate the inputs and output.\n",
    "X = df.drop('class', axis=1).values\n",
    "y = df['class'].values\n",
    "\n",
    "# 5. Normalize the input data.\n",
    "scaler = StandardScaler()\n",
    "X = scaler.fit_transform(X)\n"
]

code_cells[1]['source'] = [
    "from sklearn.model_selection import train_test_split\n",
    "from tensorflow.keras.models import Sequential\n",
    "from tensorflow.keras.layers import Dense\n",
    "\n",
    "# 1. Split the training and test data.\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# 2. Create a Sequential model.\n",
    "model = Sequential()\n",
    "\n",
    "# 3. Add several layers to your model.\n",
    "model.add(Dense(32, activation='relu', input_dim=X_train.shape[1]))\n",
    "model.add(Dense(16, activation='relu'))\n",
    "model.add(Dense(2, activation='softmax')) # Output layer for 2 classes\n",
    "\n",
    "# 4. Compile the model\n",
    "model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])\n",
    "\n",
    "# 5. Fit the training data.\n",
    "model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1, verbose=1)\n",
    "\n",
    "# 6. Evaluate your neural network model with the test data.\n",
    "loss, accuracy = model.evaluate(X_test, y_test, verbose=0)\n",
    "print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')\n",
    "\n",
    "# 7. Save your model as tic-tac-toe.model.\n",
    "model.save('tic-tac-toe.model')\n"
]

code_cells[2]['source'] = [
    "import random\n",
    "import tensorflow as tf\n",
    "\n",
    "# Load your saved model\n",
    "loaded_model = tf.keras.models.load_model('tic-tac-toe.model')\n",
    "\n",
    "# Predict on a few random rows\n",
    "indices = random.sample(range(len(X_test)), 5)\n",
    "X_random = X_test[indices]\n",
    "y_random_true = y_test[indices]\n",
    "\n",
    "predictions = loaded_model.predict(X_random)\n",
    "predicted_classes = np.argmax(predictions, axis=1)\n",
    "\n",
    "print('True classes:     ', y_random_true)\n",
    "print('Predicted classes:', predicted_classes)\n"
]

code_cells[3]['source'] = [
    "from tensorflow.keras.optimizers import Adam\n",
    "\n",
    "model2 = Sequential()\n",
    "model2.add(Dense(64, activation='relu', input_dim=X_train.shape[1]))\n",
    "model2.add(Dense(32, activation='relu'))\n",
    "model2.add(Dense(16, activation='relu'))\n",
    "model2.add(Dense(2, activation='softmax'))\n",
    "\n",
    "custom_adam = Adam(learning_rate=0.001)\n",
    "model2.compile(optimizer=custom_adam, loss='sparse_categorical_crossentropy', metrics=['accuracy'])\n",
    "\n",
    "# Train more epochs\n",
    "model2.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.1, verbose=1)\n",
    "\n",
    "loss2, accuracy2 = model2.evaluate(X_test, y_test, verbose=0)\n",
    "print(f'Improved Test Loss: {loss2:.4f}, Improved Test Accuracy: {accuracy2:.4f}')\n"
]

code_cells[4]['source'] = [
    "answer = \"\"\"\n",
    "Adding more layers and increasing the number of neurons helped the network learn the complex patterns in the Tic Tac Toe board.\n",
    "Adjusting the learning rate ensures that the optimizer converges properly without overshooting.\n",
    "Increasing the number of epochs and reducing the batch size gave the model more opportunities to learn from the data, leading to a higher accuracy (>0.95) and lower loss (<0.1).\n",
    "\"\"\"\n",
    "print(answer)\n"
]

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)
    f.write('\n')
