import React from "react";
import "./hero.css";

function Hero() {
    return (
        <div className="hero__section">
            <div className="hero">
                <div className="head__text__container">
                    <span>B</span>ank <span>R</span>econcilation
                    <br/>
                    <span>S</span>tatement <span>V</span>alidation
                </div>
                <div className="subtitle__text__container">
                    Simple Solution To Tedious BRS Solving Process
                </div>
                <div className="get__started__container">
                    <button className="get__started__btn">
						<span>
						Upload Files <i className="fas fa-cloud-upload-alt"></i>
						</span>
                    </button>
                </div>
                <div className="description__container">
                    <div className="nav-to-tutorial">

                        <span className="content-text"><i class="fas fa-question-circle"></i>&nbsp; Learn More</span>
                    </div>
                </div>
            </div>
            <div className="wave"/>
        </div>
    );
}

export default Hero;
