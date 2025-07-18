# League-of-Legends-Win-Prediction

Machine Learning model evaluation for Multiplayer Online Battle Arena (MOBA) video game win
predictors require a vast amount of dedicated training time when large datasets are provided. As
Machine Learning models and algorithms are made of different structures and do not abide by the
same learning rules, it is probable that accuracy scores deviate from each other. This work has been
carried out to examine the performance of Machine Learning models in order to detect those which are
most suitable for video game win predictors. Orthogonal to evaluating model accuracy, this study also
proposes another algorithm, based on the Pearson correlation coefficient, to compute the probability
of a team winning in MOBA video games. The Pearson Correlation Coefficient-Based Algorithm
(PCCBA) has been implemented to analyze its performance and compare it to its Machine Learning
counterparts. Moreover, it is notable to include that the dataset comprises data points of a vast
number of video game matches from the MOBA League of Legends, which was created and published
by the game developer company Riot Games in 2009. The dataset from this study was acquired by
utilizing the Riot API.

The Machine Learning models which were applied onto the datasets are the following: Logistic Re-
gression, Decision Tree, Random Forest, K-Nearest-Neighbor, Naive Bayes, Support Vector Machine,
Neural Network, Ada Boost and Gradient Boosting. The implementation of the respective models
required the scikit-learn Python library (cf. Pedregosa et al. 2011), while other libraries, such as numpy
(cf. Harris et al. 2020), matplotlib (cf. Hunter 2007), pandas (cf. McKinney 2010), and seaborn (cf.
Waskom 2021) were used to facilitate data preparation. This work has put its focus on comparing the
accuracies of the Machine Learning models and plotted multiple graphs to visualize the data. During
the evaluation of the different models, the findings suggest that the algorithm which relies on input
and output variable relationships should be capable of predicting game outcomes.