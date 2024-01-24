import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
          <Navbar className="bg-body-tertiary rstbrnd nav">
        <Container>
            <img
              alt=""
              src="/logonbg.png"
              width="60"
              height="60"
              className="brand"
            />{' '}
        </Container>
      </Navbar>
    <App />
  </React.StrictMode>,
)
