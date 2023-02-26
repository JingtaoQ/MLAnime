from flask import Flask, request, jsonify, render_template
from gensim.models import Word2Vec
import pickle
import numpy as np

app = Flask(__name__)

# 加载训练好的模型
with open('word2vec.pkl', 'rb') as f:
    model = pickle.load(f)

with open('outputmodel.pkl', 'rb') as f:
    model_op = pickle.load(f)

@app.route('/')
def Home():
    return render_template("index.html")

# 定义路由
@app.route('/predict', methods=['POST'])
def predict():
    # 获取前端输入
    features = request.form.to_dict()

    # 检查是否有空值
    if not features:
        return jsonify({'error': 'Title fields are required.'})

    # 将输入的特征转换为向量
    features_vector = []
    for feature in features.values():
        try:
            feature_vector = model.wv[feature]
        except KeyError:
            feature_vector = np.zeros(model.vector_size)
        features_vector.append(feature_vector)
    final_features = np.mean(features_vector, axis=0).reshape(1, -1)

    # 预测并返回结果
    predictions = model_op.predict(final_features)
    print(predictions)
    rating = predictions[0][0]
    preferences = 'yes' if rating >= 6 else 'no'

    # return jsonify({'rating': rating, 'preferences': preferences})
    return render_template('index.html', rating=round(rating,2), preferences=preferences)

if __name__ == '__main__':
    app.run(debug=True)
