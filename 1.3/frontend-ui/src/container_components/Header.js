import React from "react";
import './styles/header.scss';

class Header extends React.Component {
  render() {
    return (
      <div className="header">
        <div className="container">
          <nav>
            <h1 className="brand">
              <a href="index.html">
                BRSV
              </a>
            </h1>
            <ul>
              <li>
                <a href="/">Upload</a>
              </li>
              <li>
                <a href="/">Results</a>
              </li>
              <li>
                <a className="signin-signup" href="/">Sign Up/Sign In</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    );
  }
  
}

export default Header;
