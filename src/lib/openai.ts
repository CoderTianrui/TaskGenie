// Deepseek API client implementation
export const generateTaskSuggestions = async (taskTitle: string): Promise<string[]> => {
  try {
    const response = await fetch('/api/deepseek/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: "deepseek-chat",
        messages: [
          {
            role: "system",
            content: "You are a helpful task management assistant. Generate 3 specific subtasks for the given task. Each subtask should start with a dash (-) and be clear and actionable."
          },
          {
            role: "user",
            content: `Generate 3 specific subtasks for: ${taskTitle}`
          }
        ],
        temperature: 0.7,
        max_tokens: 150
      })
    });

    if (!response.ok) {
      const errorData = await response.text();
      console.error('API Error:', errorData);
      throw new Error(`API request failed with status ${response.status}`);
    }

    const data = await response.json();
    
    if (!data.choices?.[0]?.message?.content) {
      throw new Error('Invalid API response format');
    }

    const content = data.choices[0].message.content;
    const suggestions = content
      .split('\n')
      .map(line => line.trim())
      .filter(line => line.startsWith('-'))
      .map(line => line.substring(1).trim())
      .filter(Boolean);

    return suggestions.length > 0 ? suggestions : ['No suggestions available'];

  } catch (error) {
    console.error('Error generating task suggestions:', error);
    throw error;
  }
};