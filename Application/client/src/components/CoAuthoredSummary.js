import React, { useState } from 'react';

function CoAuthoredSummary({ initialSummary, onSave }) {
  const [summary, setSummary] = useState(initialSummary);

  const handleGetSuggestion = async () => {
    // API call to a new backend endpoint: /ai/suggest-summary
    // const suggestion = await getAiSummarySuggestion(); 
    // setSummary(summary + "\n\nAI Suggestion:\n" + suggestion);
  };

  return (
    <div>
      <h3>Global Summary</h3>
      <textarea 
        value={summary} 
        onChange={(e) => setSummary(e.target.value)} 
        rows={8}
      />
      <button onClick={handleGetSuggestion}>Get AI Suggestion</button>
      <button onClick={() => onSave(summary)}>Save Summary</button>
    </div>
  );
}

export default CoAuthoredSummary;
