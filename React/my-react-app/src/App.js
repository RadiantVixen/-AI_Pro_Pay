import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append("file", file);
    await axios.post("http://127.0.0.1:8000/upload/", formData);
    alert("File uploaded successfully!");
  };

  const askQuestion = async () => {
    const res = await axios.post("http://127.0.0.1:8000/ask/", { question });
    setAnswer(res.data.answer);
  };


  return (
    <div className="p-10 max-w-lg mx-auto">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-2" />
      <button onClick={uploadFile} className="bg-blue-500 p-2 rounded text-white">Upload</button>
      
      <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} className="border p-2 mt-4 w-full" placeholder="Ask a question..." />
      <button onClick={askQuestion} className="bg-green-500 p-2 mt-2 rounded text-white">Ask</button>
      <PaymentButton />
      {answer && <p className="mt-4 p-2 bg-gray-200 rounded">{answer}</p>}
    </div>
  );
}

export default App;

