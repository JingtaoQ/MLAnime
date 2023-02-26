from flask import Flask, request, jsonify, render_template
from gensim.models import Word2Vec
import pickle
import numpy as np

app = Flask(__name__)

# 加载训练好的模型
with open('Project/word2vec.pkl', 'rb') as f:
    model = pickle.load(f)

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
    predictions = model.wv.similar_by_vector(final_features.flatten(), topn=1)
    rating = predictions[0][1]
    preferences = 'yes' if rating >= 0.6 else 'no'

    # return jsonify({'rating': rating, 'preferences': preferences})
    return render_template('index.html', rating=rating, preferences=preferences)

if __name__ == '__main__':
    app.run(debug=True)
