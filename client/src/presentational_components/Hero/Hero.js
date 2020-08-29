import React from "react";
import "./hero.css";
import {Link} from "react-scroll";

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
                        <Link
                            activeClass="active"
                            to="upload"
                            spy={true}
                            smooth={true}
                            offset={250}
                            duration={700}
                        >
						<span>
						Get Started
						</span></Link>

                    </button>
                </div>
                <div className="description__container">
                    <div className="nav-to-tutorial">
                        <span className="content-text">
                            <i className="fas fa-question-circle"/>&nbsp; Learn More</span>
                    </div>
                </div>
            </div>
            <div className="wave"/>
        </div>
    );
}

export default Hero;
