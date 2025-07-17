import React, { useState } from 'react';

function JsonEditor({ initialValue, onSave }) {
  const [jsonString, setJsonString] = useState(JSON.stringify(initialValue, null, 2));

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (event) => {
      setJsonString(event.target.result);
    };
    reader.readAsText(file);
  };

  const handleSave = () => {
    try {
      const parsedJson = JSON.parse(jsonString);
      onSave(parsedJson);
    } catch (error) {
      alert('Invalid JSON format!');
    }
  };

  return (
    <div>
      <textarea 
        value={jsonString} 
        onChange={(e) => setJsonString(e.target.value)} 
        rows={10} 
        cols={50} 
      />
      <input type="file" accept=".json" onChange={handleFileChange} />
      <button onClick={handleSave}>Save Narrative</button>
    </div>
  );
}

export default JsonEditor;
