from collections import deque

def bfs_find_answer(faq_graph, question):
    queue = deque([question])  
    visited = set()  
    
    while queue:
        current = queue.popleft()
        
        if current in faq_graph.get("answers", {}):  
            return faq_graph["answers"][current]
        
        if current not in visited:
            visited.add(current)
            queue.extend(faq_graph.get(current, []))  
    
    return "Answer not found."


faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}


print(bfs_find_answer(faq_graph, "What is AI?"))
