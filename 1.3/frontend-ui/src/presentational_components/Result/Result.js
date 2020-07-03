import React from "react";
import "./result.scss";
import Card from "./Card";

function Result() {
  return (
    <section className="results-section">
      <h1 className="results-header">
        <span className="head-text">Results</span>
      </h1>
      <div className="results-content">
        <div className="result-cards">
          <div className="result-card">
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
      <div className="results-btn">
        <div className="container">
          <div className="button">
            <div className="icon">
              <i className="fas fa-save"></i>
            </div>
          </div>
          <p>Save Generated BRS file</p>
        </div>
        <div className="container">
          <div className="button">
            <div className="icon">
              <i className="fas fa-book-reader"></i>
            </div>
          </div>
          <p>View File Compilation</p>
        </div>
        <div className="container">
          <div className="button">
            <div className="icon">
              <i className="fas fa-chart-pie"></i>
            </div>
          </div>
          <p>View Chord Diagram</p>
        </div>
      </div>
    </section>
  );
}

export default Result;
