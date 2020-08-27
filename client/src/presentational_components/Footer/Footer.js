import React from "react";
import "./footer.scss";

function Footer() {
  return (
    <div>
      <footer>
        <div className="footer">
          <div className="row">
            <div className="description">
              <h2>
                <span>B</span>ank <span>R</span>econcilation 
                <span> S</span>tatement <span>V</span>alidator
              </h2>
            </div>
            <div className="pages">
              <ul>
                <li>
                  <a className="pages-link" href="/">
                    Home
                  </a>
                </li>
                <li>
                  <a className="pages-link" href="/">
                    Uploads
                  </a>
                </li>
                <li>
                  <a className="pages-link" href="/">
                    Results
                  </a>
                </li>
                <li>
                  <a className="pages-link" href="/">
                    Know More
                  </a>
                </li>
              </ul>
            </div>
            <div className="socio">
              <h3>Follow us</h3>
              <div className="links">
                <ul>
                  <li>
                    <button>
                      <i className="fab fa-github"></i>
                    </button>
                  </li>
                  <li>
                    <button>
                      <i className="fab fa-linkedin-in"></i>
                    </button>
                  </li>
                  <li>
                    <button>
                      <i className="fab fa-twitter"></i>
                    </button>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default Footer;
