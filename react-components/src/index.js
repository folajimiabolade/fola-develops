import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Anchor from './components/Anchor';
import CartLength from './components/CartLength';

const root = ReactDOM.createRoot(document.getElementById('react-root'));
root.render(
  <React.StrictMode>
    {/* <App /> */}
    <CartLength />
  </React.StrictMode>
);

// const tuber = ReactDOM.createRoot(document.getElementById('react-tuber'));
// tuber.render(
//   <React.StrictMode>
//     <Anchor />
//   </React.StrictMode>
// );

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
