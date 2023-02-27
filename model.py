import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from gensim.models import Word2Vec
import tensorflow as tf
import pickle
from tensorflow.keras.models import load_model

def find_missing(df):
    findex_list_rating = df[df['Rating'].isnull()].index.tolist()

    findex_list_Anime_id = df[~df['Anime_id'].astype(str).str.isdigit()].index.tolist()
    findex_list_rating_str = df[~df['Rating'].astype(str).str.isdigit()].index.tolist()

    findex_list = findex_list_rating + findex_list_Anime_id+findex_list_rating_str
    findex_list = list(set(findex_list))

    return findex_list

def drop_missing(train):
    missingrow_40 = find_missing(train)
    train.drop(missingrow_40, axis=0)
    return train

def Aligning_data(df):

    df1 = df.drop(['Anime_id','Genre','Type','Rating'],axis=1)
    df2 = df['Rating']
    app_train, app_test,train_labels,test_labels = train_test_split(df1,df2,test_size=0.2, random_state=42)


    print('Training Features shape: ', app_train.shape)
    print('Testing Features shape: ', app_test.shape)


    print('Training Features shape: ', app_train.shape)
    print('Testing Features shape: ', app_test.shape)

    return app_train, app_test, train_labels,test_labels


def create_model(input_shape):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=64, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(units=32, activation='relu'),
        tf.keras.layers.Dense(units=1)
    ])
    model.compile(loss='mean_squared_error',
                  optimizer=tf.keras.optimizers.Adam(0.01))
    return model

def generatedata():
    n = 1000  # 数据集大小
    features = np.random.randn(n, 100)
    labels = np.random.randint(0, 10, n)
    df = pd.DataFrame(features)  # 将 feature 转换为 DataFrame
    df['label'] = labels

    return df



def main():
    df = pd.read_csv('Anime_data.csv')
    application = df[["Anime_id","Title","Genre","Synopsis","Type","Producer","Studio","Rating"]]
    application_pre = drop_missing(application)

    # dummies  =  df['Genre'].str.split(",")
    #
    # dummies_Genre = pd.get_dummies(dummies, prefix='', prefix_sep='')

    dummies_Genre  = pd.get_dummies(application_pre['Genre'])
    dummies_Type  = pd.get_dummies(application_pre['Type'])

    application_pre_dummy = pd.concat([application_pre,dummies_Genre,dummies_Type], axis=1)

    sts_Synopsis= application_pre_dummy['Synopsis'].apply(lambda x: str(x).split(' ')).tolist()
    sts_Title= application_pre_dummy['Title'].apply(lambda x: str(x).split(' ')).tolist()
    sts_Producer= application_pre_dummy['Producer'].apply(lambda x: str(x).split(' ')).tolist()
    sts_Studio= application_pre_dummy['Studio'].apply(lambda x: str(x).split(' ')).tolist()


    sts_Synopsis_df= df['Synopsis'].apply(lambda x: str(x).split(' ')).tolist()
    sts_Title_df= df['Title'].apply(lambda x: str(x).split(' ')).tolist()
    sts_Producer_df= df['Producer'].apply(lambda x: str(x).split(' ')).tolist()
    sts_Studi_df= df['Studio'].apply(lambda x: str(x).split(' ')).tolist()

    sts=sts_Synopsis+sts_Title+sts_Producer+sts_Studio+sts_Synopsis_df+sts_Title_df+sts_Producer_df+sts_Studi_df
    # model = Word2Vec(sentences=sts, vector_size=100, window=5, min_count=1, workers=4)
    # model.save("word2vec.model")
    # with open('word2vec.pkl', 'wb') as f:
    #     pickle.dump(model, f)
    model = Word2Vec.load("word2vec.model")

    application_pre_dummy['Synopsis'] = application_pre_dummy['Synopsis'].apply(lambda x: str(x).split(' '))
    application_pre_dummy['Synopsis'] = application_pre_dummy['Synopsis'].apply(lambda x: [model.wv.get_vector(str(j)) for j in x ])

    application_pre_dummy['Title'] = application_pre_dummy['Title'].apply(lambda x: str(x).split(' '))
    application_pre_dummy['Title'] = application_pre_dummy['Title'].apply(lambda x: [ model.wv.get_vector(str(j))for j in x  ])

    application_pre_dummy['Producer'] = application_pre_dummy['Producer'].apply(lambda x: str(x).split(' '))
    application_pre_dummy['Producer'] = application_pre_dummy['Producer'].apply(lambda x: [ model.wv.get_vector(str(j)) for j in x ])

    application_pre_dummy['Studio'] = application_pre_dummy['Studio'].apply(lambda x: str(x).split(' '))
    application_pre_dummy['Studio'] = application_pre_dummy['Studio'].apply(lambda x: [ model.wv.get_vector(str(j)) for j in x ])

    application_pre_dummy['Rating'].to_csv('application_pre_dummy_label.csv',header=None)
    application_pre_dummy.drop(columns=['Rating']).to_csv('application_pre_dummy_feature.csv',header=None)
    # application_pre_dummy = application_pre_dummy.applymap(lambda x: np.asarray(x).astype('float32'))


    #######################################################################
    df = pd.read_csv('application_pre_dummy_feature.csv')
    y = df1.values
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model_csv = keras.Sequential([
        keras.layers.Dense(128, input_shape=(X_train.shape[1],), activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])

    model_csv.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model_csv.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)
    ##################################################################
    app_train, app_test,train_labels,test_labels = Aligning_data(application_pre_dummy)
    # for col_name, length in application_pre_dummy.items():
    #     print(length)


    # model_dl = create_model((100,))
    # X = app_train
    # Y = train_labels
    #
    # simdata = generatedata()
    # app_train, app_test,train_labels,test_labels = train_test_split(simdata.drop('label', axis=1), simdata['label'], test_size=0.2, random_state=42)
    #
    # history = model_dl.fit(app_train, train_labels, epochs=10, verbose=1)
    #
    # model_dl.save('outputmodel')
    # with open('outputmodel.pkl', 'wb') as f:
    #     pickle.dump(model_dl, f)
    #
    # test_loss = model_dl.evaluate(app_test, test_labels)
    # print('Test Loss:', test_loss)
    # test_predictions = model_dl.predict(app_test)
    # print(test_predictions)
    # print(tf.__version__)




main()