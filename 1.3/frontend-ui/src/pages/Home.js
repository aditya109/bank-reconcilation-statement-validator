import React from "react";
import * as ReactBoostStrap from "react-bootstrap";

import TutorialCarousel from "../components/TutorialCarousel";
import CustomModal from "../components/CustomModal";
import DisclaimerContent from "../components/DisclaimerContent";

import "../../src/styles/css/pages/home.css";

class Home extends React.Component {
  render() {
    return (
      <div className="main-home-container">
        <div className="main-home-header">
          <span className="header-text">
            Bank Reconcilation Statement Validator
          </span>
          <div className="tutorials-component">
            <CustomModal
              variant="info"
              modal_title="App Walkthrough"
              button_text="Click to view Application in 5 Simple Steps"
              component={<TutorialCarousel />}
            />
          </div>
          <div className="diclaimer-content">
            <CustomModal
              variant="warning"
              modal_title="Disclaimer"
              button_text="View Disclaimer"
              component={<DisclaimerContent />}
            />
            <ReactBoostStrap.Button variant="outline-danger">
              Continue{" "}
              <ReactBoostStrap.Spinner
                as="span"
                animation="border"
                size="sm"
                role="status"
              />
            </ReactBoostStrap.Button>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;
