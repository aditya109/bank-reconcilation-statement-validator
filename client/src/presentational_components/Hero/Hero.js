import React from "react";
import "./hero.scss";
import LeftImage from "../assets/left-place.svg";
function Hero() {
  return (
    <div className="hero-section">
      <div className="hero">
        <div className="head">
          <span className="head-text">
            <span>B</span>ank <span>R</span>econcilation
            <br />
            <span>S</span>tatement <span>V</span>alidation
          </span>
          <span className="subtitle-text">
            Simple Solution To Tedious BRS Solving Process
          </span>
          <div className="content">
            <div className="nav-to-tutorial">
              <i class="fas fa-question-circle"></i>&nbsp;
              <span className="content-text">Learn More</span>
            </div>
          </div>
        </div>
        <img src={LeftImage} alt="bg" />
      </div>
      <div className="wave" />
    </div>
  );
}

export default Hero;
