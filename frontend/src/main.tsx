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
            <div className='titlestuff'>
      <h1>CodeRoast</h1>
      Where code meets humor! 🚀
      </div>
      <div></div>
        </Container>
      </Navbar>
    <App />
  </React.StrictMode>,
)
