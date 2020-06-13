import React from "react";

import "../styles/css/components/disclaimer_content.css";

function DisclaimerContent() {
  return (
    <div className="warning-text-div">
      <span className="warning-text-low">
        This is to inform you as an end-user that{" "}
      </span>
      <span className="warning-text-high">
        this application is in alpha-phase
      </span>
      <span className="warning-text-low"> and is meant for </span>
      <span className="warning-text-high">
        automating the laborious work done to detect erroneous transactions done
        manually
      </span>
      <span className="warning-text-low">
        . So it is an earnest request to{" "}
      </span>
      <span className="warning-text-high">
        bear with simple-minded UI or noticeable server-response latencies
      </span>
      <span className="warning-text-low">, since the </span>
      <span className="warning-text-high">
        focus majored on the use-cases and not on the UI
      </span>
      <span className="warning-text-low">. This application is </span>
      <span className="warning-text-high">
        not supposed to be hosted on net unless approved by the dev
      </span>
      <span className="warning-text-low">. Please do not try to </span>
      <span className="warning-text-high">
        tamper with the code or induce malicious code in any manner.
      </span>
    </div>
  );
}

export default DisclaimerContent;
