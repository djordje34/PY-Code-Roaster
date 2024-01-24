import './App.css'
import React, { useState } from 'react';
import axios from 'axios';
import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vs2015 } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import ReactMarkdown from 'react-markdown';


function App() {
  const [code, setCode] = useState<string>('');
  const [roastedResult, setRoastedResult] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  const handleCodeChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setCode(e.target.value);
  };

  const [displayMode, setDisplayMode] = useState<'syntax' | 'markdown'>('syntax');

  const handleToggleDisplayMode = () => {
    setDisplayMode((prevMode) => (prevMode === 'syntax' ? 'markdown' : 'syntax'));
  };

  const handleRoastCode = async () => {
    try {
      if (!code.trim()) {
        console.error('No code provided');
        return;
      }
  
      setLoading(true);
  
      const response = await axios.post('http://127.0.0.1:5000/getRoasted', { code });
  
      if (response.data && response.data.summary !== undefined) {
        setRoastedResult(response.data.summary);
      } else {
        console.error('Invalid response format from the server');
      }
    } catch (error) {
      console.error('Error roasting code:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className='parent'>
      <Row style={{ minWidth: '80%', position: 'relative', borderRadius: '5px', padding: '10px', marginBottom: '10%' }}>
      <textarea
      placeholder="Enter your code here"
      value={code}
      onChange={handleCodeChange}
      style={{ 
        color:'#e3e3e3',
        width: '100%', 
        minHeight: '200px', 
        fontSize: '16px', 
        fontFamily: 'monospace',
        resize: 'none',
        border: 'none', 
        outline: 'none', 
        whiteSpace: 'pre-wrap',
        overflow: 'auto',
        borderRadius: '10px',
      }}
          />
      <div style={{ textAlign: 'left' }}>
      {code && (
        <SyntaxHighlighter language="jsx" style={vs2015} showLineNumbers wrapLines={true} lineNumberStyle={{ paddingRight: '10px' }}>
          {code}
        </SyntaxHighlighter>
        )}
      </div>
      <button onClick={handleToggleDisplayMode}>
        Toggle Display ({displayMode === 'syntax' ? 'Markdown' : 'Syntax Highlighting'})
      </button>
        <button onClick={handleRoastCode}>Roast Away!</button>
        </Row>
      <Row className="roasted-box" style={{ minWidth: '80%', position: 'relative', borderRadius: '5px', padding: '10px', marginBottom: '10%' }}>
        {!loading && <h2 style={{ color: '#f8f8f2' }}>Roasted Code</h2>}
        {loading && <div className="loading-spinner m-2"></div>}
        <div style={{ textAlign: 'left' }}>
          {!loading && displayMode === 'syntax' && (
            <SyntaxHighlighter
              language="python"
              style={vs2015}
              showLineNumbers
              wrapLines={true}
              lineNumberStyle={{ paddingRight: '10px' }}
              customStyle={{}}
              className="custom-comment"
              lineProps={{ style: { whiteSpace: 'pre-wrap' } }}
            >
              {`# ${roastedResult.split('\n').join('\n# ')}`}
            </SyntaxHighlighter>
          )}
          {!loading && displayMode === 'markdown' && (
            <ReactMarkdown>{roastedResult}</ReactMarkdown>
          )}
        </div>
        </Row>
      </Container>
  );
}

export default App;