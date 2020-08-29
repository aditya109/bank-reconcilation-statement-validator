import React from "react";
import "./result.css";
import Card from "./Card";

function Result() {
    return (
        <div className="results__section" id="result">

            {/*Header Text*/}

            <div className="results__header">
                <span className="head__text">Results</span>
            </div>

            {/*Cards Panel*/}
            <div className="results__content">
                <div className="result__cards">
                    <div className="result__card">
                        <Card
                            eta="6 seconds ago"
                            title_head_short="CPNC"
                            title_head_full="Cheques Paid Not Cashed"
                        />
                        <Card
                            eta="6 seconds ago"
                            title_head_short="CDA"
                            title_head_full="Cheques Dishonor Action"
                        />
                        <Card
                            eta="6 seconds ago"
                            title_head_short="CR"
                            title_head_full="Credits"
                        />
                        <Card
                            eta="6 seconds ago"
                            title_head_short="Dr"
                            title_head_full="Debits"
                        />
                    </div>
                </div>
            </div>

            {/*File Buttons*/}

            <div className="results__btn">

                {/*Save BRS File Button*/}

                <div className="container">
                    <div className="button">
                        <div className="icon">
                            <i className="fas fa-save"></i>
                        </div>
                    </div>
                    <p>Save Generated BRS file</p>
                </div>

                {/*Save Compiled File Button*/}

                <div className="container">
                    <div className="button">
                        <div className="icon">
                            <i className="fas fa-book-reader"></i>
                        </div>
                    </div>
                    <p>View File Compilation</p>
                </div>

                {/*View Chord Analysis*/}

                <div className="container">
                    <div className="button">
                        <div className="icon">
                            <i className="fas fa-chart-pie"></i>
                        </div>
                    </div>
                    <p>View Chord Diagram</p>
                </div>
            </div>
        </div>
    );
}

export default Result;
