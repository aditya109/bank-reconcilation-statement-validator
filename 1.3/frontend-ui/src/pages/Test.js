import React from "react";
import * as ReactBoostStrap from "react-bootstrap";

import CustomModal from "../components/CustomModal";
import DisclaimerContent from "../components/DisclaimerContent";

import "../styles/css/pages/test.css";

export default class Test extends React.Component {
  render() {
    return (
      <div className="main-home-container">
        <div className="main-home-header">
          <div className="header-text">
            Bank Reconcilation Statement Validator
          </div>
          <div className="intro-text">
            Simple Solution for Filtering of BRS Transactions
          </div>
        </div>
        <div className="main-home-content-container">
          <div className="diclaimer-content">
            <CustomModal
              variant="outline-warning"
              modal_title="Disclaimer"
              button_text="View Disclaimer"
              component={<DisclaimerContent />}
            />
            <div className="get-started">
              <span className="span-class">
                <p className="p-class">Get Started</p>
              </span>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
