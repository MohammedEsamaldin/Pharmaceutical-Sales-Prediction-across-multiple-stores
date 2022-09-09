import imp
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer
#from scripts.data_cleaning import logger

class DataTransformer:
    """
    provides transformer functions for machine learning.
    """
    def __init__(self) -> None:
        pass

        logger.info('Function DataTransformer successfully added!!!')
        


    def sep_cat_num(self, df):
        """
        separates categorical and numerical variables
        """
        categorical_columns = df.select_dtypes(include='object')
        numerical_columns = df.select_dtypes(exclude='object')

        logger.info('Separating catagorical and numerical variables successfuly done!!!')

        return categorical_columns, numerical_columns


    
    def cat_labeler(self, df, cat_cols):
        """
        assigns a numerical label to categorical values
        """
        for column in cat_cols:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
        
        print("catagories successfully labeled")

        logger.info('Labeling the catagorical columns using label encoder successfuly done!!!')

        return df


    def scaler(self, df):
        """
        transforms values within 0 to 1 range
        """
        scaling = MinMaxScaler()
        df[:] = scaling.fit_transform(df[:])

        print("Data successfully scaled")

        logger.info('Scaling the data successfuly done!!!')
        
        return df

    def normalizer(self, df):
        """
        normalizing. turning mean to 0 and SD to 1
        """
        # define standard scaler
        scaler = StandardScaler()
        # transform data
        scaled = pd.DataFrame(scaler.fit_transform(df))

        print("Data successfully normalized")

        logger.info('Normalizing the data successfuly done!!!')

        return scaled

    def target_feature(self, df,t):
        """
        target and feature separator
        """
        features = (df.drop(df.columns[[t]], axis = 1)).values
        target = df.iloc[:,t].values

        print("target and features separated")

        logger.info('Separating target features successfuly done!!!')

        return features, target

    def set_splitter(self, input, test, val, rand_state):
        """
        splits dataset into specified percentages.
        """
        features, target = input
        per_1 = test
        per_2 = (1-test)*val
        x_train, x_test, y_train, y_test = train_test_split(features, target,test_size= per_1,shuffle = True, random_state = rand_state )
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,test_size= per_2, shuffle = True, random_state = rand_state)

        print("data successfully splitted")

        logger.info('Splitting successfuly done!!!')

        return [x_train, y_train, x_test, y_test, x_val, y_val]