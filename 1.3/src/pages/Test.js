import React, { useState, useEffect } from "react";

import * as ReactBoostStrap from "react-bootstrap";

import "../styles/css/pages/test.css";

export default class Test extends React.Component {
  render() {
    return (
      <div className="main-home-container">
        <div className="main-home-header">
          <span className="header-text">
            Bank Reconcilation Statement Validator
          </span>
          </div>
        <div className="intro-text">
          Simple Solution for Detection of Bad BRS Transactions 
        </div>



      </div>
    );
  }
}
