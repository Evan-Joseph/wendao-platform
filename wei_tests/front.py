import networkx as nx
from pyvis.network import Network
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# 创建图数据
G = nx.Graph()

# 添加节点
nodes = [
    ("AI", {"group": 1}),
    ("Machine Learning", {"group": 1}),
    ("Deep Learning", {"group": 1}),
    ("Neural Networks", {"group": 2}),
    ("Computer Vision", {"group": 2}),
    ("Natural Language Processing", {"group": 2}),
    ("Reinforcement Learning", {"group": 2}),
    ("Supervised Learning", {"group": 3}),
    ("Unsupervised Learning", {"group": 3}),
    ("Semi-supervised Learning", {"group": 3}),
]
G.add_nodes_from(nodes)

# 添加边
edges = [
    ("AI", "Machine Learning"),
    ("AI", "Deep Learning"),
    ("Machine Learning", "Supervised Learning"),
    ("Machine Learning", "Unsupervised Learning"),
    ("Machine Learning", "Semi-supervised Learning"),
    ("Deep Learning", "Neural Networks"),
    ("Deep Learning", "Computer Vision"),
    ("Deep Learning", "Natural Language Processing"),
    ("Deep Learning", "Reinforcement Learning"),
]
G.add_edges_from(edges)

# 创建Pyvis网络
net = Network(height="600px", width="100%", bgcolor="#ffffff", font_color="black")

# 从NetworkX图添加节点到Pyvis网络
for node, node_attrs in G.nodes(data=True):
    net.add_node(node, label=node, group=node_attrs.get("group", 0))

# 添加边
for source, target in G.edges():
    net.add_edge(source, target)

# 保存图形为HTML文件
net.save_graph("templates/graph.html")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/graph')
def get_graph():
    nodes = [{"id": node, "group": data["group"]} for node, data in G.nodes(data=True)]
    links = [{"source": source, "target": target} for source, target in G.edges()]
    return jsonify({"nodes": nodes, "links": links})

if __name__ == '__main__':
    app.run(debug=True)