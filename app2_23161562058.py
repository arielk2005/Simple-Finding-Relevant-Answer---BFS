from collections import deque

def bfs_find_answer(faq_graph, question):
    queue = deque([question])  # Mulai pencarian dari pertanyaan pengguna
    visited = set()  # Menyimpan node yang sudah dikunjungi
    
    while queue:
        current = queue.popleft()
        
        if current in faq_graph.get("answers", {}):  # Cek apakah sudah ada jawabannya
            return faq_graph["answers"][current]
        
        if current not in visited:
            visited.add(current)
            queue.extend(faq_graph.get(current, []))  # Tambahkan node terkait ke antrean
    
    return "Answer not found."

# Contoh FAQ Graph
faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

# Mencari jawaban untuk "What is AI?"
print(bfs_find_answer(faq_graph, "What is AI?"))
